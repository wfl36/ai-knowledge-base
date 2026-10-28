# 3, 7, 14, 17, 42: Instruction Tuning Installs and Sharpens Number-Choice Heuristics in Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-28  
**来源：** rss  

## 项目描述
arXiv:2610.36178v1 Announce Type: new Abstract: We measure, without sampling error, the probability a language model assigns to each integer from 1 to N when asked for a random number. For a fixed prompt the model defines one probability vector, which we compute by summing over each integer's scored spellings rather than estimate by sampling, removing the noise that limits earlier studies [1, 4]. We evaluate 18 open-weight model lines at five ranges up to N = 100, under 29 decoding configurations, on two inference stacks; 15 of them have matched base and instruction-tuned checkpoints that both give usable answers. Instruction tuning makes the distribution less uniform in all 15 pairs. It installs one heuristic, round-number avoidance, and sharpens another, endpoint avoidance. Base checkpoints do not avoid round numbers once the endpoints are removed from those sets; tuned checkpoints avoid them, multiples of 10 almost completely. Base checkpoints return the endpoints 1 and N at 0.30 to 0.60 of the interior rate; tuned checkpoints almost never return them. A preference for odd numbers is consistent across tuned checkpoints only at N = 100, where base checkpoints also show it weakly. Endpoint avoidance and the odd preference fit the account Kubovy and Psotka [6] proposed for human number choice; round-number avoidance is not part of that account, and the midpoint avoidance it predicts is essentially absent, with one slight exception at N = 100. Tuning does not install a new favourite integer shared across models: above N = 10 no modal integer is shared by more than 42 percent of tuned conditions, and P (17) rises in 10 of 15 pairs and falls in 5. The concentration is present in the model's own distribution: at temperature 1.0, nucleus truncation at top-p 0.95 adds a median of 0.035 to the total variation distance.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.36178
