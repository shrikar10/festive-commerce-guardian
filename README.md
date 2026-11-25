# Festive Commerce Guardian

Keep your festive sales running. Let AI handle the incidents.

An AI-powered ops assistant that detects checkout failures, investigates the cause (NudgeBee), takes voice input (Sarvam AI), and — after human approval — activates a fallback via feature flags (Flagsmith) without redeploying.

## Structure
- `backend/` – FastAPI (checkout simulator, incident/recovery API, integrations)
- `frontend/` – React + Vite dashboard (voice input, incident, approval, activity log)
- `demo/` – demo script

## API contract
| Endpoint | Purpose |
|---|---|
| `POST /api/demo/incident` | Trigger simulated failure |
| `GET /api/incident` | Current incident + activity log |
| `POST /api/voice` | Transcribe voice (multipart `audio`) |
| `POST /api/investigate` | Start investigation |
| `POST /api/recover` | Apply approved recovery (called by NudgeBee workflow) |
| `GET /api/health` | Checkout health |
| `POST /api/checkout` | Simulated checkout |

## Run
```
cp .env.example .env
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload
cd frontend && npm install && npm run dev
```
Without API keys (or with `USE_FLAGSMITH=false`, the default) the backend uses in-memory flags, a canned transcript, and a **mock NudgeBee investigation** (`rca` field on the incident: summary, affected_dependency, confidence, evidence, recommended_fix). Set `USE_FLAGSMITH=true` plus keys to use real Flagsmith.

## Flagsmith flags
`product_catalog_fail` (default on), `checkout_fallback_enabled` (default off).
