"""NudgeBee integration.

Investigation is done in the NuBi UI (no public chat API verified). This returns the
RCA copied from the real NuBi session; the approval workflow calls POST /api/recover.
"""


def investigate(incident) -> dict:
    return {
        "root_cause": "product_catalog_failure",
        "recommended_action": "enable_checkout_fallback",
    }
