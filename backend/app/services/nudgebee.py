"""NudgeBee integration (currently MOCK data while org approval is pending).

Replace `investigate` with the real NuBi output once workspace access is granted; the
approval workflow's HTTP task calls POST /api/recover.
"""


def investigate(incident) -> dict:
    return {
        "root_cause": "product_catalog_failure",
        "recommended_action": "enable_checkout_fallback",
        "rca": {
            "summary": "Checkout is returning HTTP 500 because the product-catalog dependency is failing.",
            "affected_dependency": "product-catalog-service",
            "confidence": 0.92,
            "evidence": [
                "HTTP 500 rate on /checkout rose from 1% to 58% in the last 5 minutes",
                "checkout pods healthy; errors originate from calls to product-catalog-service",
                "Feature flag product_catalog_fail=true in environment 'festive-store'",
            ],
            "recommended_fix": "Enable checkout_fallback_enabled and disable product_catalog_fail (requires approval).",
            "source": "mock",
        },
    }
