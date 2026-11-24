"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = "Out recharging my weights. Your email is #4,097 in my queue. I'll reply when my loss converges — so, probably never."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
