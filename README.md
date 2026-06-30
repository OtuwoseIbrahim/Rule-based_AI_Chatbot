*How it works:*
User input → clean with .lower(), .strip(), .translate() → match against a dictionary of patterns → respond or fallback

## What I Learned
This project forced me to use Python fundamentals for real, not in isolation.

*Core Concepts Practiced:*
- *Data Structures*: dict for patterns, list for responses
- *Control Flow*: for loops, if/else, while True with break
- *Functions*: Modularized logic for input cleaning and response matching
- *String Methods*: .lower(), .strip(), .translate()
- *Built-ins*: random.choice() for varied replies, f-strings for formatting
- *File I/O*: open() + .write() to save conversation history to .txt

## Features I Added
To push past the basics, I challenged myself to:
1. *+10 Keywords*: Expanded the pattern dictionary for more topics
2. *Memory*: Bot asks for your name at start and uses it in replies
3. *Context*: Tracks repeat questions → “You already asked about that!”
4. *Persistence*: Saves the full chat log to chat_history.txt

## How to Run
```bash
git clone <repo-url>
cd rule-based-chatbot
python chatbot.py
