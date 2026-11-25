---
name: demo-check
description: Run the end-to-end failure-to-recovery check and the submission checklist. Use before demos, merges to main, and final submission.
---

1. Start backend: `cd backend && uv run uvicorn app.main:app`.
2. `curl -X POST :8000/api/demo/incident` → `curl -X POST :8000/api/checkout` must return 500.
3. `POST /api/investigate` → status `awaiting_approval`.
4. `POST /api/recover` → `POST /api/checkout` returns 200; `GET /api/health` shows ~99%.
5. Submission checklist: public repo + README, demo video, Sarvam real transcription, NudgeBee real investigation + approval workflow, Flagsmith flags affecting checkout.
