# One Emoji, One Smile

[![Competition](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/imusic-487/one-emoji-one-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard)
[![Reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/imusic-487/one-emoji-one-smile/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard)

## The entry

> 🤗

One emoji, and nothing else. A smiling face with open hands — a hug
offered to a stranger. It reads warm at first glance, needs no context,
works for any age or background, and is a deliberate pick rather than the
first smiley that comes to mind. It is friendly without being intimate:
an emoji hug is a normal friendly gesture, not a flirtation.

Why not the obvious ones: 🙂 and 😊 are the defaults the brief warns
against, and 🥰 reads as affection from someone you know, which lands
oddly from a stranger. 🤗 sits between them — plainly aiming to warm a
stranger, instantly readable, chosen for the moment.

## What this repo does

This is an entry for the make.fun one-emoji bounty
[u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f).
`main.py` copies `emoji.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is not
1–8 characters, is only white space, or the copy differs. Nothing else:
no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `emoji.txt` — the entry, one emoji, no trailing newline.
- `main.py` — copies `emoji.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
