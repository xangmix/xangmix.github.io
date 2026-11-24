---
title: "LGPO 논문 해설"
date: 2026-11-14 13:00:00 +0900
categories: [공부, RL]
tags: [lgpo, likelihood-gate, grpo, llm-rl]
description: LGPO(arXiv 2611.15404)의 likelihood gate와 속도 이득을 GRPO와 비교한 해설
math: true
image: /assets/img/posts/f7_lgpo_gate.svg
---

"Is the Importance Ratio Necessary for Stable Reinforcement Learning in LLMs?"를 풀어 쓴 해설입니다.
PPO·GRPO의 확률비가 하는 일을 신뢰구역과 보정으로 나눠 보고, 보정은 없어도 되며 신뢰구역이 필요하다는 논문의 주장을 따라갑니다.
옛 정책의 확률을 계산하지 않는 대안 LGPO(가능도 게이팅)와 실험(Table 1, Figure 3~8)을 GRPO와 비교해 정리했습니다.
논문에 대한 제 해석은 페이지의 마지막 절에 따로 적었습니다.

[새 탭에서 보기](/reports/lgpo-paper-explained/)

<iframe src="/reports/lgpo-paper-explained/" width="100%" height="900" style="border:0" loading="lazy"></iframe>
