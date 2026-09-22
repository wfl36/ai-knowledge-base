# A framework for recipe data structure with applications for culinary and nutritional insights

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.22099v1 Announce Type: new Abstract: Cooking is a complex process that transforms raw ingredients into delicious and nutritious dishes, yet the recipes that encode this process remain largely free text; readable by people but not directly computable. Existing recipe collections capture fragments of this information, but no shared representation links a recipe's structured ingredient composition, its geo-cultural provenance, and its nutritional profile within a single queryable schema. We address this representation gap by formalizing a framework for recipe data structure that decomposes each recipe into typed ingredient entities, grounds those entities in a reference nutritional database, and annotates them with geo-cultural and dietary context. We present RecipeDB2, a structured compilation of 128,942 recipes with 35,474 ingredients from 32 regions and 99 countries. Ingredient phrases are parsed into seven culinary attributes using a transformer-based named-entity model; ingredients are linked to the USDA reference tables through a BERT embedding strategy (F1 = 87.90 on a manually adjudicated set of the 200 most frequent ingredients), yielding 148 nutritional parameters per mapped ingredient; a Random Forest classifier propagates 34 ingredient categories across the full vocabulary; and a deterministic, conservative rule set assigns each recipe a dietary style. Through RecipeDB2 (https://cosylab.iiitd.edu.in/recipedb2/), we demonstrate a scalable framework for making recipes computable, turning culinary heritage (long treated as an artistic rather than a quantitative object) into a data-driven analysis.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.22099
