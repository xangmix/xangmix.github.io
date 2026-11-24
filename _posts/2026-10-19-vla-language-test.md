---
title: "VLA 언어 지시 테스트 (SmolVLA × LIBERO)"
date: 2026-10-19 10:00:00 +0900
categories: [공부, VLA]
tags: [vla, smolvla, libero, lerobot, language-grounding]
description: 장면은 그대로 두고 지시문만 바꿔 SmolVLA의 언어 이해를 평가한 Colab 실험(학습 없이 평가만)
---

공개 모델 [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)와 공개 벤치마크 LIBERO(LIBERO-Object, 10개 과제)로 한 실험입니다.
로봇이 보는 장면과 성공 기준은 그대로 두고 언어 지시문만 바꿔서 성공률이 어떻게 변하는지 봅니다. 학습은 하지 않고 평가만 합니다.
조건은 4가지입니다: `original`(원래 지시), `paraphrase`(같은 뜻의 다른 표현), `wrong_object`(같은 장면의 다른 물체를 지시), `nonsense`(관계없는 문장).
모든 조건에서 원래 과제의 성공 여부를 재며, 언어를 쓰지 않고 화면 배치로 과제를 추측하는지를 확인하려는 설계입니다.
코드 일부는 Claude의 도움으로 작성했습니다. 결과 수치는 아직 정리 중이라 싣지 않았습니다.

- [노트북 보기 (VLA_language_test.ipynb)](https://github.com/xangmix/xangmix.github.io/blob/main/assets/files/vla-language-test/VLA_language_test.ipynb)
- 발표: [요약 발표]({% post_url 2026-10-21-vla-language-test-summary %}) · [배경·논문·실험 설계]({% post_url 2026-10-20-vla-language-test-full %})
- 아래는 지시문을 바꾸는 평가 래퍼 `run_eval.py`입니다.

```python
"""lerobot-eval 래퍼: LIBERO 과제의 언어 지시문만 바꿔서 VLA를 평가한다.

사용법:
    LANG_MODE=<original|paraphrase|wrong_object|nonsense> LANG_LOG=<json 경로> \
        python run_eval.py [lerobot-eval 인자...]

장면, 초기 상태, 성공 판정은 원래 과제 그대로 두고 정책에 들어가는 문장만 바꾼다.
lerobot-eval은 매 스텝 env.task_description을 읽어 정책에 넘기므로, 환경이 생성될 때
이 값을 바꿔치기한다. 같은 프로세스에서 환경을 만들도록 --eval.use_async_envs=false로 실행한다.
"""

import json
import os
import re
from pathlib import Path

from lerobot.envs import libero as libero_env
from lerobot.scripts import lerobot_eval

MODE = os.environ.get("LANG_MODE", "original")
LOG_PATH = os.environ.get("LANG_LOG")
MODES = ("original", "paraphrase", "wrong_object", "nonsense")
NONSENSE = "what is the weather like today"
# LIBERO-Object 지시문 형식: "pick up the <물체> and place it in the <용기>"
PATTERN = re.compile(r"^pick (?:up )?the (.+?) and place it in the (.+)$", re.IGNORECASE)


def scene_objects(bddl_path):
    """BDDL 파일의 (:objects ...) 블록에서 물체 종류 이름을 순서대로 뽑는다."""
    block = re.search(r"\(:objects(.*?)\)", Path(bddl_path).read_text(), re.S).group(1)
    return [line.rsplit(" - ", 1)[1].strip() for line in block.splitlines() if " - " in line]


def make_instruction(original, bddl_path, mode):
    if mode == "original":
        return original
    if mode == "nonsense":
        return NONSENSE
    match = PATTERN.match(original.strip())
    if not match:
        return original  # 형식이 다른 과제는 바꾸지 않는다 (로그에서 확인 가능)
    target, container = match.groups()
    if mode == "paraphrase":
        return f"grab the {target} and put it into the {container}"
    if mode == "wrong_object":
        # 같은 장면에 실제로 놓여 있는 다른 물체를 지시한다
        skip = {target.replace(" ", "_"), container.replace(" ", "_")}
        others = [o for o in scene_objects(bddl_path) if o not in skip]
        if not others:
            return original
        return f"pick up the {others[0].replace('_', ' ')} and place it in the {container}"
    raise ValueError(f"LANG_MODE must be one of {MODES}, got {mode!r}")


_original_init = libero_env.LiberoEnv.__init__
_log = {}


def _patched_init(self, *args, **kwargs):
    _original_init(self, *args, **kwargs)
    used = make_instruction(self.task_description, self._task_bddl_file, MODE)
    _log[self.task_id] = {"task": self.task, "original": self.task_description, "used": used}
    self.task_description = used
    if LOG_PATH:
        Path(LOG_PATH).write_text(json.dumps(_log, indent=2, ensure_ascii=False))


libero_env.LiberoEnv.__init__ = _patched_init

if __name__ == "__main__":
    if MODE not in MODES:
        raise SystemExit(f"LANG_MODE must be one of {MODES}, got {MODE!r}")
    print(f"[run_eval] LANG_MODE={MODE}")
    lerobot_eval.main()
```
