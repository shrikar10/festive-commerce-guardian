from pydantic import BaseModel


class Incident(BaseModel):
    incident_id: str = "INC-001"
    service: str = "checkout"
    status: str = "open"
    severity: str = "critical"
    root_cause: str | None = None
    recommended_action: str | None = None
    rca: dict | None = None
