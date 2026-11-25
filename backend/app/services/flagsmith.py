"""Flagsmith wrapper. Falls back to in-memory flags when no keys are configured (demo fallback)."""
import os

import requests

_local = {"product_catalog_fail": True, "checkout_fallback_enabled": False}
API = "https://edge.api.flagsmith.com/api/v1"


def is_enabled(name: str) -> bool:
    key = os.getenv("FLAGSMITH_ENVIRONMENT_KEY")
    if not key:
        return _local[name]
    try:
        r = requests.get(f"{API}/flags/", headers={"X-Environment-Key": key}, timeout=5)
        r.raise_for_status()
        for f in r.json():
            if f["feature"]["name"] == name:
                return f["enabled"]
    except requests.RequestException:
        pass
    return _local[name]


def set_flag(name: str, enabled: bool) -> None:
    """TODO: use Flagsmith Admin API with FLAGSMITH_API_KEY (backend-only) to update the real flag."""
    _local[name] = enabled
