# Cross-platform posting bot for creators — post once, publish to 14 platforms via one API

Publish **one piece of content across every creator platform at once** with the [ModelVI](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=creator-multi-platform-poster) partner API. Describe a post once, list the target platforms, and let ModelVI fan it out — instead of logging into and uploading to each platform by hand.

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=creator-multi-platform-poster)** · [API docs](https://modelvi.com/agent-api) · [Pricing](https://modelvi.com/pricing)

![example](https://img.shields.io/badge/example-MIT-blue) ![python](https://img.shields.io/badge/python-3.9+-green)

---

## What this is

A small, MIT-licensed **example integration** (Python) that shows the core pattern of a **cross-platform posting bot**: one caption + one `POST /schedule` call → published across many platforms at once. It talks only to ModelVI's public partner API. Copy it and go.

**Supported platforms (the 14 ModelVI posts to):** OnlyFans · Fansly · Fancentro · F2F (Friends2Follow) · Maloum · LoyalFans · MYM · Fetlife · Fanvue · 4Based · BestFans · Fansyme · Brezzels · Knky. Platforms are passed as **codes**: `ONLYFANS FAN FNC F2F MALOUM LOYALFANS MYMFANS FETLIFE FOURBASED FANVUE BESTFANS FANSYME BREZZELS KNKY`.

## Quickstart (~5 min)

**1. Get your API key** → **[modelvi.com/sign-up](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=creator-multi-platform-poster)**. Partner keys look like `mvk_<keyId>_<secret>`.

**2. Install & run**
```bash
pip install requests
export MODELVI_API_KEY="mvk_<keyId>_<secret>"
python example.py
```

## The pattern

```
one caption + platform list  ──►  POST /schedule  ──►  ONLYFANS
                                                    ├─►  FAN
                                                    ├─►  FNC
                                                    └─►  … (all 14)
```

`example.py` grabs a model id from `GET /model_list`, then sends a single `POST /schedule` describing the caption, the target platform **codes**, the schedule time (`scheduledAt`, ISO-8601 UTC), and the post `type` (`1`=FREE · `2`=FANS · `3`=PAID). Every `200` is wrapped in `{ "success": true, "payload": … }`.

## Use cases / keywords

A **multi-platform posting bot** / **postbot** for agencies automating creator content: *cross-post OnlyFans Fansly Fancentro*, *postbot maloum*, *onlyfans posting bot*, *fansly scheduler*, *schedule posts to F2F*, *content scheduler for creators*, *social media automation for creators*. Point one API call at all 14 platforms instead of one login per platform per creator.

## Honest note

This is a **minimal example**, not a production SDK — it omits retries, pagination, media upload, and rich error handling. The full, authoritative endpoint reference is at **[modelvi.com/agent-api](https://modelvi.com/agent-api)** and **[modelvi.com/partner-api-docs](https://modelvi.com/partner-api-docs)**. It talks only to the public ModelVI partner API; there's no proprietary logic here.

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=creator-multi-platform-poster)** — see [pricing](https://modelvi.com/pricing).

MIT licensed.
