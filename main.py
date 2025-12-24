import os
from utils.support_agent import TechnicalSupportAgent

# Robust prompt loading
PROMPT_PATHS = ["prompt.txt", "../prompt.txt"]
SYSTEM_PROMPT = None

for path in PROMPT_PATHS:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            SYSTEM_PROMPT = f.read()
        break

if SYSTEM_PROMPT is None:
    raise FileNotFoundError("prompt.txt not found")


def main():
    print("Technical Support Assistant")
    print("=" * 40)

    agent = TechnicalSupportAgent(SYSTEM_PROMPT)

    sample_conversation = [
        "My browser keeps crashing.",
        "I'm using Chrome on Windows 11.",
        "I already restarted.",
        "Nothing works."
    ]

    for msg in sample_conversation:
        print(f"\nUser: {msg}")
        reply = agent.chat(msg)
        print(f"Support: {reply}")


if __name__ == "__main__":
    main()
