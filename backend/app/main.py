from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
load_dotenv()

from .models import Incident
from .services import flagsmith, sarvam, nudgebee

app = FastAPI(title="Festive Commerce Guardian")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

incident: Incident | None = None
activity: list[str] = []


def log(msg: str) -> None:
    activity.append(msg)


def checkout_failing() -> bool:
    return flagsmith.is_enabled("product_catalog_fail") and not flagsmith.is_enabled("checkout_fallback_enabled")


@app.get("/api/health")
def health():
    ok = not checkout_failing()
    return {"checkout_ok": ok, "success_rate": 99 if ok else 42, "error_rate": 1 if ok else 58}


@app.post("/api/checkout")
def checkout():
    if checkout_failing():
        raise HTTPException(500, "product catalog unavailable")
    return {"status": "order_placed"}


@app.post("/api/demo/incident")
def trigger_incident():
    global incident
    flagsmith.set_flag("product_catalog_fail", True)
    flagsmith.set_flag("checkout_fallback_enabled", False)
    incident = Incident()
    log("Incident INC-001 triggered: checkout returning HTTP 500")
    return incident


@app.get("/api/incident")
def get_incident():
    return {"incident": incident, "activity": activity}


@app.post("/api/voice")
async def voice(audio: UploadFile):
    text = await sarvam.transcribe(
        await audio.read(), audio.filename or "audio.wav", audio.content_type or "audio/wav"
    )
    log(f"Voice transcribed: {text}")
    return {"text": text}


@app.post("/api/investigate")
def investigate():
    if incident is None:
        raise HTTPException(404, "no incident")
    result = nudgebee.investigate(incident)
    incident.status = "awaiting_approval"
    incident.root_cause = result["root_cause"]
    incident.recommended_action = result["recommended_action"]
    incident.rca = result["rca"]
    log("NudgeBee investigation complete; awaiting approval")
    return incident


@app.post("/api/recover")
def recover():
    """Called by the NudgeBee workflow HTTP task after human approval."""
    if incident is None:
        raise HTTPException(404, "no incident")
    flagsmith.set_flag("product_catalog_fail", False)
    flagsmith.set_flag("checkout_fallback_enabled", True)
    incident.status = "resolved"
    log("Recovery applied via Flagsmith; incident resolved")
    return incident
