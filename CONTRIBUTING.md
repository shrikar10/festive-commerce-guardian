# Contributing (hackathon, 2–3+ people working in parallel)

## Ownership
| Area | Path | Owner |
|---|---|---|
| Backend, Flagsmith, NudgeBee | `backend/` | Owner 1 (shrikar10) |
| Frontend, voice, demo/README | `frontend/`, `demo/` | Teammate |

Stay in your folder to avoid merge conflicts. Changes to the API contract (README table) need a heads-up in chat first.

## Workflow
1. `git pull origin main`
2. `git checkout -b <area>/<short-topic>` (e.g. `frontend/voice-input`)
3. Commit small and often; `git pull --rebase origin main` before pushing.
4. Open a PR to `main`; merge quickly (self-merge OK if CI passes) — no long-lived branches.
5. Never commit `.env`; share keys privately.

## Setup
```
cp .env.example .env
cd backend && uv venv --python 3.12 && uv pip install -r requirements.txt && uv run uvicorn app.main:app --reload
cd frontend && npm install && npm run dev
```
The backend works without keys (in-memory flags, canned transcript), so the frontend can be built immediately against `http://localhost:8000`.

## Copilot
Project instructions are in `.github/copilot-instructions.md`; skills in `.github/skills/` (`add-api-endpoint`, `frontend-dashboard`, `sponsor-integrations`, `demo-check`).
