---
title: "GRPO 논문 해설"
date: 2026-11-14 12:00:00 +0900
categories: [공부, RL]
tags: [grpo, deepseekmath, group-advantage, ppo]
description: GRPO(arXiv 2402.03300)가 PPO의 critic을 그룹 평균으로 대체하는 방식 해설
math: true
image: /assets/img/posts/f6_grpo_group.svg
---

DeepSeekMath 논문(arXiv 2402.03300)에서 쓰인 GRPO를 풀어 쓴 해설입니다.
논문의 큰 줄기(데이터 → SFT → RL)를 먼저 따라간 뒤, PPO의 가치 함수(critic) 대신 같은 질문에서 뽑은 그룹의 평균으로 어드밴티지를 만드는 방식을 설명합니다.
SFT·RFT·DPO·PPO·GRPO를 한 틀로 보는 통합 관점과 점검 질문도 들어 있습니다.
로봇과의 연결은 논문에 없는 제 해석이라고 페이지 안에 밝혀 두었습니다.

[새 탭에서 보기](/reports/grpo-paper-explained/)

<iframe src="/reports/grpo-paper-explained/" width="100%" height="900" style="border:0" loading="lazy"></iframe>
