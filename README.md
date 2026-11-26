# Needle sales agent: learning notes

Research for an outbound solar sales call agent. Needle, a small tool-calling model, only labels what the caller said. A StateSmith state machine does everything else: what is said, prices, commitments and compliance.

Start with the plan, then the call states. The debate and the design are the reasoning behind them.

## Read in this order

1. [The plan](plan/final-plan.md): runtime, call structure, safety gates, certification and the open items.
2. [The 96 call states](states/doc.md): every state a call can be in, in 9 groups. The same states are in [states.json](states/states.json) as data and in [call-state-atlas.html](states/call-state-atlas.html) as a page (download it and open it in a browser).
3. [The debate rounds](debate/rounds.md): every round, with its attack, defence and verdict.
4. [The design](design/design.md): the full design as it grew round by round. [base-design.md](design/base-design.md) is where it started.

## Folders

| Folder | What is in it |
|---|---|
| [`plan/`](plan/) | `final-plan.md`, the plan as it stands |
| [`states/`](states/) | the 96 call states: `doc.md`, `states.json`, `call-state-atlas.html` |
| [`design/`](design/) | `design.md` (the full design) and `base-design.md` (the starting design) |
| [`debate/`](debate/) | `rounds.md`, the merged round log |
| [`debate/briefs/`](debate/briefs/) | the briefs the attacking side worked from, first and second version |
| [`debate/batches/`](debate/batches/) | the raw rounds in 30 batches, described below |

## The raw batches

Each of the 30 batches (`b01` to `b30`) has one file of each kind:

| File | What it is |
|---|---|
| `attacks-bNN.md` | the attacks for that batch |
| `defenses-bNN.md` | the answers to them |
| `verdicts-bNN.md` | the judge's verdict on each round |
| `posts-bNN.md` | the short summary of each round |
| `log-bNN.md` | the whole batch merged in one file |
| `merged-bNN` | an empty marker: the batch was merged into the log |

Also in that folder: `BREAKER.md`, `DEFENDER.md`, `JUDGE.md` and `POSTER.md` (the role instructions), `summary.tsv` (one line per round), and `merge.py`, `add_topics.py` and `fixnum.py` (the scripts that merged the batches; they point at the folder they ran in, not this repo).

The state machines are in a separate repo, `needle-sales-demo`.
