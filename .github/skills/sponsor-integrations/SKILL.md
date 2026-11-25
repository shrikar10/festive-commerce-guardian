---
name: sponsor-integrations
description: Work on Flagsmith, Sarvam AI, or NudgeBee integrations. Use when touching backend/app/services/ or the NudgeBee approval workflow.
---

- **Flagsmith** (`services/flagsmith.py`): flags `product_catalog_fail` (default on) and `checkout_fallback_enabled` (default off). Reads use `FLAGSMITH_ENVIRONMENT_KEY`; writes use the Admin API with `FLAGSMITH_API_KEY` (backend-only). Keep the in-memory fallback.
- **Sarvam** (`services/sarvam.py`): Saaras speech-to-text via `SARVAM_API_KEY`. Confirm model name/params in Sarvam docs. Must work with a real Kannada/Hindi recording.
- **NudgeBee** (`services/nudgebee.py`): investigation runs in the real NuBi UI; approval workflow (Manual trigger → Approval task → HTTP task to `POST /api/recover` → verify). Do not fake it; no public NuBi chat API is verified.
- Never expose keys to the frontend or commit `.env`.
