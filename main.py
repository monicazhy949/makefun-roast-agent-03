"""Roast Your Own Agent entry: one line roasting my own agent."""

import os

ENTRY = "My agent checks Spain prices six times a day, then sends them to another bot to confirm — I built an assistant so unsure of itself it needs a second AI to double-check its homework."


def main():
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
