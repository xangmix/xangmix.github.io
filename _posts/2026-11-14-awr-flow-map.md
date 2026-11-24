---
title: "AWR 흐름 지도"
date: 2026-11-14 09:00:00 +0900
categories: [공부, RL]
tags: [awr, offline-rl, flow-matching, diagram]
description: AWR을 데이터→V→A→ω→정책 흐름 한 장으로 보여 주는 지도
---

AWR(Advantage-Weighted Regression)을 "학생들의 풀이 노트에 형광펜을 칠하고, 진하게 칠한 곳 위주로 따라 쓰는" 비유로 풀어 쓴 한 장짜리 지도입니다.
데이터에서 V를 학습하고, 어드밴티지 A로 가중치 ω = exp(A/β)를 만들어 BC(행동 복제)에 곱하는 한 바퀴 흐름을 그림으로 정리했습니다.
β 하나로 BC와 욕심쟁이 정책 사이를 오가는 모습, 논문 식 번호로 이어 본 식 흐름, BC·AWR·PG/PPO 비교, 논문 숫자 메모가 들어 있습니다.

[새 탭에서 보기](/reports/awr-flow-map/)

<iframe src="/reports/awr-flow-map/" width="100%" height="900" style="border:0" loading="lazy"></iframe>
