# Copilot instructions — Festive Commerce Guardian

Hackathon project (deadline 25 Nov 2026, 5 PM IST). Goal: one working failure → investigation → approval → recovery demo.

- Backend: Python 3.12 + FastAPI in `backend/app` (use `uv`). Integrations live in `backend/app/services/` (flagsmith, sarvam, nudgebee).
- Frontend: React + Vite in `frontend/src`. Talks to the backend only via the `/api/*` contract in README.md.
- Do not change the API contract or incident JSON shape without telling the team.
- Secrets only in `.env` (never commit). Flagsmith admin key and Sarvam key are backend-only.
- Recovery is limited to the predefined action (toggle the two Flagsmith flags). No arbitrary infra changes.
- Keep fallbacks: manual text input if voice fails; in-memory flags if Flagsmith is unreachable.
- Prefer small PRs; no new features beyond scope (no auth, analytics, multi-tenant).
