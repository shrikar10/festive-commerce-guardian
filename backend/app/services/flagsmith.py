"""Flagsmith wrapper. Falls back to in-memory flags when no keys are configured (demo fallback)."""
import os

import requests

_local = {"product_catalog_fail": True, "checkout_fallback_enabled": False}
API = "https://edge.api.flagsmith.com/api/v1"
ADMIN = "https://api.flagsmith.com/api/v1"


def _live() -> bool:
    """Real Flagsmith is opt-in (USE_FLAGSMITH=true); default is in-memory dummy flags."""
    return os.getenv("USE_FLAGSMITH", "false").lower() == "true"


def is_enabled(name: str) -> bool:
    key = os.getenv("FLAGSMITH_ENVIRONMENT_KEY") if _live() else None
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


def _feature_id(env: str, name: str):
    r = requests.get(f"{API}/flags/", headers={"X-Environment-Key": env}, timeout=5)
    r.raise_for_status()
    return next((f["feature"]["id"] for f in r.json() if f["feature"]["name"] == name), None)


def set_flag(name: str, enabled: bool) -> None:
    """Update the flag via the Flagsmith Admin API (FLAGSMITH_API_KEY, backend-only); mirror locally as fallback."""
    _local[name] = enabled
    env, token = os.getenv("FLAGSMITH_ENVIRONMENT_KEY"), os.getenv("FLAGSMITH_API_KEY")
    if not (_live() and env and token):
        return
    headers = {"Authorization": f"Token {token}"}
    try:
        fid = _feature_id(env, name)
        env_id = requests.get(f"{ADMIN}/environments/{env}/", headers=headers, timeout=5).json()["id"]
        base = f"{ADMIN}/environments/{env_id}/features/{fid}/versions/"
        # Environment uses v2 versioning: create a version, edit its state, publish.
        ver = requests.post(base, headers=headers, json={}, timeout=5)
        ver.raise_for_status()
        vbase = f"{base}{ver.json()['uuid']}/"
        states = requests.get(f"{vbase}featurestates/", headers=headers, timeout=5)
        states.raise_for_status()
        fs = states.json()[0] if isinstance(states.json(), list) else states.json()["results"][0]
        requests.patch(
            f"{vbase}featurestates/{fs['id']}/", headers=headers, json={"enabled": enabled}, timeout=5
        ).raise_for_status()
        requests.post(f"{vbase}publish/", headers=headers, json={}, timeout=5).raise_for_status()
    except requests.RequestException:
        pass
