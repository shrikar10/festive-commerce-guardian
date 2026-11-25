---
name: add-api-endpoint
description: Add or change a FastAPI endpoint in the Festive Commerce Guardian backend while keeping the shared API contract and incident JSON shape intact. Use when adding routes, service integrations, or models.
---

1. Check the contract table in `README.md`; if the endpoint is new or changed, update the README table in the same PR.
2. Add the route in `backend/app/main.py` (or a router under `backend/app/routes/`). Put external calls in `backend/app/services/`.
3. Incident responses must keep: `incident_id, service, status, severity, root_cause, recommended_action` (see `backend/app/models.py`).
4. Log user-visible steps with `log(...)` so they show in the activity log.
5. Verify: `cd backend && uv run python -c "from app.main import app"` and curl the endpoint on `uvicorn app.main:app`.
