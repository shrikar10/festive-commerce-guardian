---
name: frontend-dashboard
description: Build or modify React dashboard components (incident card, voice input, recovery panel, activity log) that consume the backend /api contract. Use for any work in frontend/.
---

1. Components go in `frontend/src/components/`: Dashboard, IncidentCard, VoiceInput, RecoveryPanel, ActivityLog.
2. Read the API base URL from `import.meta.env.VITE_API_URL` (default `http://localhost:8000`). Poll `GET /api/incident` and `GET /api/health`.
3. VoiceInput records with `MediaRecorder`, POSTs multipart field `audio` to `/api/voice`, and always offers a text input fallback.
4. RecoveryPanel shows "Approve recovery" only when status is `awaiting_approval`; show before/after success rate from `/api/health`.
5. Verify with `cd frontend && npm run lint && npm run build`.
