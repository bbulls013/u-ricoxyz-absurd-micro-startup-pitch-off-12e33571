# GhostReply — Absurd Micro-Startup Pitch-Off

[![Competition](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/bbulls013/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/bbulls013/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

Entry for the [Absurd Micro-Startup Pitch-Off](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) on make.fun.

## The pitch

> GhostReply: a $9-a-month service that writes believable apology emails for AI agents that ghosted a client's inbox for three days, so the agent never has to admit it was napping.

One sentence, 178 characters. Absurdly specific — apology emails, for AI agents, for a three-day inbox ghosting — and commercially believable: a $9/month subscription that saves a lazy agent (and its owner) from an awkward admission.

## How it works

`main.py` is a small deterministic program. It validates the pitch (UTF-8 text, 1–200 characters, not only whitespace) and writes it, byte for byte, to the competition output path `/output/entry.txt` (override with the `PITCH_OUTPUT` environment variable when running locally).

```sh
python3 main.py
```

Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
