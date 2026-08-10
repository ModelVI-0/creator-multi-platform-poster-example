# creator-multi-platform-poster-example

Publish **one piece of content across many platforms at once** using the [ModelVI posting API](https://modelvi.com).

This is a small, open-source **example integration** for developers who want a clean starting point for **social media automation for creators** and the agencies that manage them. It shows the core pattern of a **cross-platform posting bot**: you describe a post once, list the target platforms, and let the ModelVI posting API fan it out — instead of logging into and uploading to each platform by hand.

> **Requires a ModelVI API key.** → **[Get your API key at modelvi.com](https://modelvi.com)**

---

## What it does

- Takes a single piece of content (a caption, plus optional media).
- Sends it to the ModelVI posting API **once**.
- Fans it out to multiple platforms in a single call — the "post once, publish everywhere" pattern.
- Reads all secrets from the environment (`API_KEY`, `BASE_URL`), so nothing is hard-coded.

It is intentionally minimal: one file, one function, well-commented. Use it as a reference for wiring the ModelVI posting API into your own scheduler, dashboard, or internal tool.

## Why (the agency use-case)

Content teams and creator management agencies typically maintain a presence for each creator across many social platforms. Doing that manually — re-uploading the same clip and caption to five or more apps, per creator, per day — does not scale.

This example is aimed at that workflow. For **social media automation creators** and agency developers, a small **cross-platform posting bot** built on the ModelVI posting API lets you:

- Define a post once and distribute it programmatically.
- Keep API keys out of source control and in environment variables.
- Build the plumbing yourself (queues, retries, scheduling) around a single publish call.

## How it works

```
your content  ──►  ModelVI posting API  ──►  Instagram
(caption +                                ├─►  TikTok
 media +                                  ├─►  X
 platform list)                           ├─►  YouTube
                                          └─►  Facebook (etc.)
```

You send **one** request describing the content and the list of target platforms. See [`example.py`](./example.py) for the exact shape.

## Requirements

- Python 3.9+
- `requests` (`pip install requests`)
- A ModelVI API key — **[get one at modelvi.com](https://modelvi.com)**

## Install

```bash
git clone https://github.com/your-org/creator-multi-platform-poster-example.git
cd creator-multi-platform-poster-example
pip install requests
```

## Configure (`.env`)

Copy `.env.example` to `.env` and fill in your values (or export them in your shell). Both values are **placeholders** you supply yourself:

```dotenv
# Your ModelVI API key — get it at https://modelvi.com
API_KEY=your_modelvi_api_key_here

# Base URL for the API. Placeholder — confirm the real host at https://modelvi.com/docs
BASE_URL=https://api.modelvi.com
```

The example reads these from the environment and will exit early with a helpful message if `API_KEY` is missing.

## Usage

The full, commented sample lives in [`example.py`](./example.py). At a high level:

```bash
export API_KEY="your_modelvi_api_key_here"
export BASE_URL="https://api.modelvi.com"   # placeholder — see modelvi.com/docs

python example.py
```

Inside `example.py`, the `publish_everywhere(...)` helper demonstrates the "one piece of content → many platforms at once" pattern: one caption, optional media, and a list of platforms sent in a single POST to the ModelVI posting API.

## Get your API key

This example does nothing without a key.

**→ [Get your API key at modelvi.com](https://modelvi.com)**

- Product & sign-up: <https://modelvi.com>
- API documentation: <https://modelvi.com/docs>

## A note on honesty

**This is an EXAMPLE integration.** The endpoint path (`/v1/publish`), the request body, and the response handling in `example.py` are **placeholders** that illustrate the pattern — they are clearly marked as such in the code. They are **not** guaranteed to match production. For the real, live endpoints, field names, and response formats, always refer to the official docs:

**→ [https://modelvi.com/docs](https://modelvi.com/docs)**

This repo intentionally does **not** publish response schemas as if they were authoritative. When in doubt, trust the docs over this example.

## License

MIT. See [`LICENSE`](./LICENSE).