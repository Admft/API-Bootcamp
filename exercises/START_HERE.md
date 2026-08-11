# Type-Along Exercises — Start Here

You learn by **typing**, not filling in blanks. Each guide walks you line-by-line through building a real script.

## How it works

1. Open the guide in `exercises/guides/`
2. Create a **new empty file** in `exercises/my-work/` (name given in each guide)
3. Type each step — don't copy-paste whole files; type the code yourself
4. Run your script after every step
5. Run the verifier when the guide tells you to

```powershell
# Example after finishing guide 02:
python exercises/my-work/02_basics.py
python exercises/verify/verify_02.py
```

## Order

| # | Guide | You create | Time |
|---|-------|------------|------|
| 1 | `guides/01_http_type_along.md` | `my-work/01_answers.txt` | 30 min |
| 2 | `guides/02_python_type_along.md` | `my-work/02_basics.py` | 45 min |
| 3 | `guides/03_get_filter_type_along.md` | `my-work/03_get_incidents.py` | 45 min |
| 4 | `guides/04_sync_type_along.md` | `my-work/04_sync.py` | 60 min |
| 5 | `guides/05_reliability_type_along.md` | `my-work/05_reliability.py` | 45 min |
| 6 | `guides/06_capstone_type_along.md` | `my-work/06_sync_incidents.py` | 90 min |

## Rules

- **Type it** — muscle memory matters. Stuck on one line? Peek at the hint, then type it yourself.
- **Run often** — every 5–10 lines, save and run. Errors teach you faster than reading.
- **Don't open solutions** until you've run the verifier and it failed twice.

## Prerequisites (every API exercise)

Terminal 1:
```powershell
python mock-apis/run_servers.py
```

Terminal 2:
```powershell
.\venv\Scripts\Activate.ps1
```
