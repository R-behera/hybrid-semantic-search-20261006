"""Public-data connectors for the portfolio expansion phase.

The generated test suite never calls the network. Run this module manually to
download a small raw snapshot, then review licensing and terms before use.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.request
from pathlib import Path


SOURCES = [
    {
        "name": "arXiv API",
        "url": "https://export.arxiv.org/api/query?search_query=cat:cs.AI&start=0&max_results=5",
        "purpose": "Real technical papers for hybrid indexing"
    },
    {
        "name": "Stack Exchange API",
        "url": "https://api.stackexchange.com/2.3/questions?pagesize=5&order=desc&sort=activity&tagged=machine-learning&site=stackoverflow",
        "purpose": "Real technical questions and metadata filters"
    }
]


def fetch(source: dict) -> bytes:
    request = urllib.request.Request(
        source["url"],
        headers={
            "Accept": "application/json, application/xml, text/plain",
            "User-Agent": os.environ.get(
                "DATA_SOURCE_USER_AGENT",
                "industry-ai-portfolio/0.1 contact@example.com",
            ),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=int, default=0)
    parser.add_argument("--output", default="data/raw/source-snapshot.txt")
    args = parser.parse_args()

    source = SOURCES[args.source]
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(fetch(source))
    print(
        json.dumps(
            {
                "source": source["name"],
                "purpose": source["purpose"],
                "output": str(destination),
                "bytes": destination.stat().st_size,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
