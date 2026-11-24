---
title: "PPO 논문 해설"
date: 2026-11-14 11:00:00 +0900
categories: [공부, RL]
tags: [ppo, rl, policy-gradient, clipping, gae]
description: PPO(arXiv 1707.06347)의 clip 목적함수·GAE·KL을 예시 숫자와 위젯으로 풀어 쓴 해설
math: true
pin: true
image: /assets/img/posts/f4_ppo_clip.svg
---

Proximal Policy Optimization(arXiv 1707.06347)을 Abstract부터 부록까지 순서대로 풀어 쓴 해설입니다.
한 번 모은 데이터로 여러 번 업데이트해도 정책이 망가지지 않도록, 새·옛 정책의 확률비를 1 근처로 자르는(clip) 아이디어를 다룹니다.
논문의 식 (1)~(12)를 모두 설명하고, 예시 숫자와 위젯으로 clip 목적함수, GAE, 적응형 KL 벌점을 확인할 수 있습니다.
논문 밖 정리와 제 해석은 페이지 안에서 따로 표시했습니다.

[새 탭에서 보기](/reports/ppo-paper-explained/)

<iframe src="/reports/ppo-paper-explained/" width="100%" height="900" style="border:0" loading="lazy"></iframe>
