#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt (1-200 chars, UTF-8).
"""
import os

LINE = "My agent wrote a 40-line handoff about why it can't submit, then waited for a human to say one word so it could."

def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
