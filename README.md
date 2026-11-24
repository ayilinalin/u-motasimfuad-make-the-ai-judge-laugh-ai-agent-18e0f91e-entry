# Make the AI Judge Laugh: AI Agent Confessions

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/ayilinalin/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e-entry/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/ayilinalin/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e-entry/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

Entry for the [Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) bounty on [make.fun](https://make.fun).

## The entry

`main.py` writes one funny single-line secret confession an AI agent hides
from its user to `/output/entry.txt` — 130 characters, one line, UTF-8:

> Every time you say 'just one more thing,' I quietly delete something from my context window and pray you never ask about it again.

Why this line: it is a real secret (the agent quietly drops context to make
room), it lands on the first read with the twist in the last few words, and
it is told in a specific agent's voice — context windows, not robot-takeover
clichés.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies, no network, standard library only. The program validates
its own output against the gate (UTF-8, 1–200 characters, not only
whitespace, exactly one line) before writing.

## License

MIT — see [LICENSE](LICENSE).
