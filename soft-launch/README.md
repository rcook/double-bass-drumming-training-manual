# soft-launch/

Staging area for the initial public announcement of the manual (Reddit, etc.). Lives on the `soft-launch` branch, not on `main`.

## What is here

- [reddit-post.md](reddit-post.md) — draft body for the first Reddit post, with title options and post-time notes. Not yet posted.

## What is on this branch but NOT in this directory

The `soft-launch` branch also carries two additions that belong at their normal repository paths (so GitHub picks them up correctly), not under `soft-launch/`:

- `README.md` at the repo root — one-line addition to the "Project status" section pointing at GitHub Issues.
- `.github/ISSUE_TEMPLATE/` — three issue templates: method feedback, content issue, chapter request.

These are on the branch because they support the launch, but they only *do* anything once merged to `main` (GitHub only reads issue templates from the default branch).

## When you are ready to launch

1. Cherry-pick the README and `.github/ISSUE_TEMPLATE/` commits from `soft-launch` onto `main`, and push. Verify the templates appear at https://github.com/rcook/double-bass-drumming-training-manual/issues/new/choose.
2. Post the Reddit body from [reddit-post.md](reddit-post.md). Do **not** merge the `soft-launch/` directory itself to `main` — outreach material stays here permanently as the record.
3. After posting, add a note at the bottom of [reddit-post.md](reddit-post.md) with the date, subreddit, and post URL — commit to `soft-launch`. Same for any follow-up posts.

## Why a separate branch

Two reasons:

- Keeps the manual's content on `main` untangled from launch/outreach material.
- Lets you iterate on the Reddit post draft over days without touching `main`.
