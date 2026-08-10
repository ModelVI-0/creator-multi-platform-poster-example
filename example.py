#!/usr/bin/env python3
"""
creator-multi-platform-poster-example

Publish ONE piece of content across MANY creator platforms at once using the
public ModelVI partner API — a minimal "cross-platform posting bot" example.

  Get your API key:  https://modelvi.com/sign-up
  API reference:     https://modelvi.com/agent-api  ·  https://modelvi.com/partner-api-docs

This is a minimal EXAMPLE (no retries/pagination/media upload). It talks only to
the public ModelVI partner API: key -> endpoint -> result.
"""

import os
import sys
from datetime import datetime, timezone, timedelta

import requests  # pip install requests

# Base URL of the public ModelVI partner API (override via env if needed).
BASE_URL = os.environ.get("MODELVI_API_BASE", "https://modelvi.com/api/partner/v1")
API_KEY = os.environ.get("MODELVI_API_KEY")
SIGNUP_URL = "https://modelvi.com/sign-up"

# The 14 platform CODES ModelVI posts to (pass these, not brand names):
PLATFORMS = [
    "ONLYFANS", "FAN", "FNC", "F2F", "MALOUM", "LOYALFANS", "MYMFANS",
    "FETLIFE", "FOURBASED", "FANVUE", "BESTFANS", "FANSYME", "BREZZELS", "KNKY",
]

# Post type: 1 = FREE, 2 = FANS, 3 = PAID.
TYPE_FREE = 1


def _headers():
    if not API_KEY:
        sys.exit(
            f"Missing MODELVI_API_KEY. Get a key at {SIGNUP_URL} and export it:\n"
            f'  export MODELVI_API_KEY="mvk_<keyId>_<secret>"'
        )
    return {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def _payload(resp):
    """Every authed 200 is an envelope: {success, payload}. Return the payload."""
    if resp.status_code == 401:
        sys.exit(f"Unauthorized (401). Get a valid key at {SIGNUP_URL}")
    resp.raise_for_status()
    body = resp.json()
    return body.get("payload", body)


def first_model_id():
    """Grab a model id to schedule posts for (GET /model_list)."""
    resp = requests.get(f"{BASE_URL}/model_list", headers=_headers(), timeout=30)
    models = _payload(resp)
    if not models:
        sys.exit("No models on this account yet — add one in your ModelVI dashboard.")
    # payload shape may be a list or {items:[...]}; handle both defensively.
    model = (models[0] if isinstance(models, list) else models.get("items", [{}])[0])
    return model.get("id") or model.get("model")


def post_everywhere(caption, platforms, when=None, post_type=TYPE_FREE):
    """Publish one caption to many platforms in a single POST /schedule call."""
    model = first_model_id()
    scheduled_at = (when or datetime.now(timezone.utc) + timedelta(minutes=5))
    body = {
        "model": model,
        "platforms": platforms,                       # list of CODES
        "title": caption,                             # the caption field is `title`
        "scheduledAt": scheduled_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": post_type,
    }
    print(f"POST {BASE_URL}/schedule  → {', '.join(platforms)}")
    resp = requests.post(f"{BASE_URL}/schedule", json=body, headers=_headers(), timeout=30)
    result = _payload(resp)
    print("Scheduled:", result)
    return result


if __name__ == "__main__":
    # One caption, fanned out to all 14 platforms at once.
    post_everywhere("New drop is live ✨", PLATFORMS)
