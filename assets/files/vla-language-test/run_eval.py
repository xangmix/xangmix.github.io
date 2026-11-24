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
