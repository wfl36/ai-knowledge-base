"""Version management: snapshot, list, prune, and diff knowledge base versions."""

import difflib
import os
import shutil
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from .models import VersionInfo, DiffResult


class VersionManager:
    """Manage versioned snapshots of the knowledge base directory."""

    # -----------------------------------------------------------------------
    # Snapshot
    # -----------------------------------------------------------------------

    def snapshot(self, knowledge_dir: str, versions_dir: str) -> VersionInfo:
        """Create a timestamped snapshot of *knowledge_dir* into *versions_dir*.

        The snapshot directory is named with the pattern ``YYYYMMDD_HHMMSS``
        (local time). All files under *knowledge_dir* are recursively copied.

        Parameters
        ----------
        knowledge_dir : str
            Source knowledge directory to snapshot.
        versions_dir : str
            Destination versions root directory.

        Returns
        -------
        VersionInfo
            Metadata about the newly created snapshot.
        """
        os.makedirs(versions_dir, exist_ok=True)

        now = datetime.now()
        version_id = now.strftime("%Y%m%d_%H%M%S")
        version_path = os.path.join(versions_dir, version_id)

        if os.path.exists(version_path):
            raise FileExistsError(f"Version snapshot already exists: {version_id}")

        shutil.copytree(knowledge_dir, version_path)

        return VersionInfo(
            version_id=version_id,
            created_at=now,
            path=os.path.abspath(version_path),
        )

    # -----------------------------------------------------------------------
    # List versions
    # -----------------------------------------------------------------------

    def list_versions(self, versions_dir: str) -> List[VersionInfo]:
        """List all version snapshots sorted by creation time (oldest first).

        Parameters
        ----------
        versions_dir : str
            Root versions directory.

        Returns
        -------
        List[VersionInfo]
        """
        if not os.path.isdir(versions_dir):
            return []

        entries: List[VersionInfo] = []
        for name in sorted(os.listdir(versions_dir)):
            full = os.path.join(versions_dir, name)
            if not os.path.isdir(full):
                continue
            try:
                dt = datetime.strptime(name, "%Y%m%d_%H%M%S")
            except ValueError:
                continue
            entries.append(
                VersionInfo(
                    version_id=name,
                    created_at=dt,
                    path=os.path.abspath(full),
                )
            )

        return entries

    # -----------------------------------------------------------------------
    # Prune old versions
    # -----------------------------------------------------------------------

    def keep_last_n(self, versions_dir: str, n: int = 5) -> List[str]:
        """Keep only the *n* most recent snapshots, delete the rest.

        Parameters
        ----------
        versions_dir : str
        n : int
            Number of recent versions to retain (default 5).

        Returns
        -------
        List[str]
            List of deleted version IDs.
        """
        versions = self.list_versions(versions_dir)
        if len(versions) <= n:
            return []

        # versions are already sorted oldest-first
        to_remove = versions[:-n]
        removed_ids: List[str] = []
        for v in to_remove:
            shutil.rmtree(v.path, ignore_errors=True)
            removed_ids.append(v.version_id)

        return removed_ids

    # -----------------------------------------------------------------------
    # Diff two versions
    # -----------------------------------------------------------------------

    def diff_versions(
        self,
        v1: str,
        v2: str,
        *,
        context_lines: int = 3,
    ) -> DiffResult:
        """Compare two version snapshot directories.

        Parameters
        ----------
        v1 : str
            Path to the older version directory.
        v2 : str
            Path to the newer version directory.
        context_lines : int
            Number of context lines in the unified diff output.

        Returns
        -------
        DiffResult
        """
        files_v1 = self._collect_files(v1)
        files_v2 = self._collect_files(v2)

        set_v1 = set(files_v1.keys())
        set_v2 = set(files_v2.keys())

        added = sorted(set_v2 - set_v1)
        removed = sorted(set_v1 - set_v2)
        common = sorted(set_v1 & set_v2)

        modified: List[str] = []
        diff_details: List[str] = []

        for rel in common:
            f1 = files_v1[rel]
            f2 = files_v2[rel]
            if self._files_differ(f1, f2):
                modified.append(rel)
                diff_details.append(
                    self._unified_diff(f1, f2, rel, context_lines=context_lines)
                )

        for rel in added:
            diff_details.append(f"+++ {rel} (added)")

        for rel in removed:
            diff_details.append(f"--- {rel} (removed)")

        return DiffResult(
            v1=os.path.basename(v1),
            v2=os.path.basename(v2),
            added_files=added,
            removed_files=removed,
            modified_files=modified,
            detail="\n".join(diff_details),
        )

    # -----------------------------------------------------------------------
    # Multi-version comparison (up to 3)
    # -----------------------------------------------------------------------

    def compare_versions(
        self,
        version_paths: List[str],
        *,
        context_lines: int = 3,
    ) -> List[DiffResult]:
        """Compare up to 3 consecutive version snapshots.

        Parameters
        ----------
        version_paths : List[str]
            Two or three version directory paths (ordered oldest → newest).
        context_lines : int

        Returns
        -------
        List[DiffResult]
            Pairwise diffs between consecutive versions.

        Raises
        ------
        ValueError
            If fewer than 2 or more than 3 paths are provided.
        """
        if not (2 <= len(version_paths) <= 3):
            raise ValueError("compare_versions requires 2 or 3 version paths")

        results: List[DiffResult] = []
        for i in range(len(version_paths) - 1):
            results.append(
                self.diff_versions(
                    version_paths[i],
                    version_paths[i + 1],
                    context_lines=context_lines,
                )
            )
        return results

    # -----------------------------------------------------------------------
    # Internal helpers
    # -----------------------------------------------------------------------

    @staticmethod
    def _collect_files(base_dir: str) -> Dict[str, str]:
        """Walk *base_dir* and return {relative_path: absolute_path} for regular files."""
        result: Dict[str, str] = {}
        for root, _dirs, files in os.walk(base_dir):
            for fname in files:
                abs_path = os.path.join(root, fname)
                rel_path = os.path.relpath(abs_path, base_dir)
                result[rel_path] = abs_path
        return result

    @staticmethod
    def _files_differ(path_a: str, path_b: str) -> bool:
        """Quick check whether two files have different content."""
        try:
            with open(path_a, "rb") as fa, open(path_b, "rb") as fb:
                return fa.read() != fb.read()
        except OSError:
            return True

    @staticmethod
    def _unified_diff(
        path_a: str,
        path_b: str,
        rel_path: str,
        context_lines: int = 3,
    ) -> str:
        """Produce a unified diff string for a single file pair."""
        try:
            with open(path_a, "r", encoding="utf-8", errors="replace") as fa:
                lines_a = fa.readlines()
            with open(path_b, "r", encoding="utf-8", errors="replace") as fb:
                lines_b = fb.readlines()
        except OSError as exc:
            return f"Error reading {rel_path}: {exc}"

        diff = difflib.unified_diff(
            lines_a,
            lines_b,
            fromfile=f"a/{rel_path}",
            tofile=f"b/{rel_path}",
            n=context_lines,
        )
        return "".join(diff)
