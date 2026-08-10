#!/usr/bin/env python3
"""
creator-multi-platform-poster-example

Minimal example: publish ONE piece of content across MANY platforms at once
using the ModelVI posting API.

This is an EXAMPLE integration. The endpoint path and the request/response
shapes below are PLACEHOLDERS to illustrate the pattern only. The real,
authoritative endpoints, field names, and responses live at:

    https://modelvi.com/docs

Get an API key: https://modelvi.com
"""

import os
import sys

import requests  # pip install requests


# ---------------------------------------------------------------------------
# 1. Configuration — read secrets from the environment, never hard-code them.
#    Copy .env.example to .env and fill in your values, or export them:
#        export API_KEY="your_modelvi_api_key_here"
#        export BASE_URL="https://api.modelvi.com"   # placeholder host
# ---------------------------------------------------------------------------
API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL", "https://api.modelvi.com")  # PLACEHOLDER host

if not API_KEY:
    sys.exit(
        "Missing API_KEY. Get one at https://modelvi.com and set it in your "
        "environment (see .env.example)."
    )

# PLACEHOLDER endpoint path — replace with the real endpoint from modelvi.com/docs.
PUBLISH_PATH = "/v1/publish"  # <-- replace with the real path from https://modelvi.com/docs


def publish_everywhere(caption, media_urls, platforms):
    """
    Publish a single piece of content to several platforms in one API call.

    This is the "one piece of content -> many platforms at once" pattern:
    you describe the post once, list the target platforms, and let the
    ModelVI posting API fan it out for you.

    Args:
        caption:    The text/caption for the post.
        media_urls: List of image/video URLs to attach (may be empty).
        platforms:  List of target platforms to publish to at once.
    """

    # PLACEHOLDER request body. The real field names and structure are
    # documented at https://modelvi.com/docs — this only shows the *idea*.
    payload = {
        "caption": caption,      # the text/caption for the post
        "media": media_urls,     # media URLs to attach (optional)
        "platforms": platforms,  # fan-out targets, e.g. ["instagram", "tiktok", "x"]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",  # your ModelVI API key
        "Content-Type": "application/json",
    }

    url = f"{BASE_URL.rstrip('/')}{PUBLISH_PATH}"

    print(f"POST {url}")
    print(f"Publishing one post to: {', '.join(platforms)}")

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
    except requests.RequestException as err:
        # Network / DNS / timeout errors. Because BASE_URL and PUBLISH_PATH
        # above are placeholders, this example will not reach a live server
        # until you point it at the real endpoint from https://modelvi.com/docs.
        sys.exit(f"Request failed: {err}")

    # NOTE: the response schema is intentionally NOT assumed here. Do not rely
    # on any particular field names — check the real response format at
    # https://modelvi.com/docs. We simply surface the status code and raw body.
    print(f"HTTP {response.status_code}")
    print(response.text)

    response.raise_for_status()


if __name__ == "__main__":
    # Example: one caption + one image, fanned out to several platforms at once.
    # Replace the media URL with your own, and trim the platform list as needed.
    publish_everywhere(
        caption="New post from my content workflow.",
        media_urls=["https://example.com/your-image.jpg"],
        platforms=["instagram", "tiktok", "x", "youtube", "facebook"],
    )