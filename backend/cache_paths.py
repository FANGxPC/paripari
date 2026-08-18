"""Helpers for deterministic backend cache paths."""

import os


def repo_cache_key(owner: str, repo: str) -> str:
    return f"{owner}_{repo}".replace("-", "_")


def index_cache_path(owner: str, repo: str) -> str:
    cache_dir = os.path.join(os.path.dirname(__file__), "cache")
    filename = f"{repo_cache_key(owner, repo)}_index.json"
    return os.path.join(cache_dir, filename)
