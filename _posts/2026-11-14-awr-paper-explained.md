---
title: "AWR 논문 해설"
date: 2026-11-14 10:00:00 +0900
categories: [공부, RL]
tags: [awr, advantage-weighted-regression, offline-rl, td-lambda]
description: AWR(arXiv 1910.00177) 식을 MC·TD(λ)·β 예시로 풀어 쓴 해설. PPO·GRPO 앞 단계
math: true
image: /assets/img/posts/f8_awr_loop.svg
---

Advantage-Weighted Regression(arXiv 1910.00177)을 Abstract부터 부록 C까지 순서대로 풀어 쓴 해설입니다.
강화학습을 지도학습 회귀 두 번(점수 예측기 V 학습, 어드밴티지만큼 가중한 행동 따라 하기)으로 만든다는 핵심을 다루고, 논문의 식 (1)~(57)을 모두 설명합니다.
MC·TD(λ), β 크기에 따른 변화 같은 숫자는 설명용 예시이며, 논문에 없는 해석은 주황색 상자로 구분했습니다.

[새 탭에서 보기](/reports/awr-paper-explained/)

<iframe src="/reports/awr-paper-explained/" width="100%" height="900" style="border:0" loading="lazy"></iframe>
