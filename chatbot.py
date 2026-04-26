# =============================================================================
# chatbot.py
# Project  : Optimization Strategies for Natural Language Interface
#            for EdTech Infrastructure
# Roll No  : PRJN26-127
# Purpose  : Main entry point — runs the CLI loop and handles user interaction.
# Usage    : python chatbot.py
# =============================================================================

import sys
import time
from matcher import match_intent, is_farewell

# ── ANSI Color Codes (for colored CLI output) ─────────────────────────────────
class Color:
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"

# ── Helper: print with color ──────────────────────────────────────────────────
def cprint(text, color=Color.RESET):
    print(f"{color}{text}{Color.RESET}")

# ── Banner ────────────────────────────────────────────────────────────────────
BANNER = r"""
  _____    _       ____        _   
 | ____|  | |     |  _ \      | |  
 | |__  __| |_   _| |_) | ___ | |_ 
 |  __|/ _` | | | |  _ < / _ \| __|
 | |__| (_| | |_| | |_) | (_) | |_ 
 |_____\__,_|\__,_|____/ \___/ \__|
                                    
  Optimization Strategies for Natural Language
  Interface for EdTech Infrastructure
  Roll No : PRJN26-127
  Type 'help' to get started | Type 'exit' to quit
"""

DIVIDER = "─" * 55


def print_banner():
    """Print the startup banner."""
    cprint(BANNER, Color.CYAN)
    cprint(DIVIDER, Color.BLUE)


def print_typing_effect(text, delay=0.012):
    """
    Simulate a typing effect for bot responses.
    Prints characters one by one with a small delay.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after message


def get_user_input():
    """
    Prompt the user for input.
    Returns the raw string typed by the user.
    """
    try:
        cprint(f"\n{'─'*55}", Color.BLUE)
        user_input = input(f"{Color.GREEN}  You   ▶  {Color.RESET}")
        return user_input
    except (KeyboardInterrupt, EOFError):
        # Handle Ctrl+C or Ctrl+D gracefully
        return "exit"


def display_response(response: str):
    """
    Display the chatbot's response with formatting.
    """
    cprint(f"\n{'─'*55}", Color.BLUE)
    cprint(f"  EduBot ▶", Color.CYAN)
    print()
    # Add indentation to each line of the response
    for line in response.split("\n"):
        print(f"  {line}")
    print()


def log_interaction(user_input: str, response: str, log_file="chat_history.log"):
    """
    Append each conversation turn to a log file.
    This simulates a basic DevOps logging practice.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] USER: {user_input}\n")
        f.write(f"[{timestamp}] BOT : {response[:80]}...\n")
        f.write("-" * 60 + "\n")


def main():
    """
    Main CLI loop.
    
    Flow:
    ─────────────────────────────────────────────────────────────────
    1. Print banner / welcome message.
    2. Enter infinite loop:
        a. Read user input.
        b. Check for farewell/exit intent → break if True.
        c. Pass input to matcher → get response.
        d. Display response.
        e. Log interaction to file.
    3. Print goodbye message and exit.
    ─────────────────────────────────────────────────────────────────
    """
    print_banner()
    cprint("  Welcome! I'm EduBot, your EdTech assistant.", Color.YELLOW)
    cprint("  I can help with courses, assignments, grades & more.", Color.YELLOW)
    cprint(DIVIDER, Color.BLUE)

    interaction_count = 0

    while True:
        # ── Step 1: Get input ───────────────────────────────────────────────
        user_input = get_user_input()

        # Skip empty inputs
        if not user_input.strip():
            cprint("  [EduBot] Please type something! Try 'help'.", Color.YELLOW)
            continue

        # ── Step 2: Check for exit ──────────────────────────────────────────
        if is_farewell(user_input):
            farewell_msg = (
                "👋 Goodbye! Keep learning and stay curious.\n"
                "   Visit EduBot anytime. Happy learning! 🎓"
            )
            display_response(farewell_msg)
            log_interaction(user_input, farewell_msg)
            cprint(DIVIDER, Color.BLUE)
            cprint(f"  Session ended. Total interactions: {interaction_count + 1}", Color.MAGENTA)
            cprint(DIVIDER, Color.BLUE)
            break

        # ── Step 3: Get response from matcher ───────────────────────────────
        response = match_intent(user_input)
        interaction_count += 1

        # ── Step 4: Display response ─────────────────────────────────────────
        display_response(response)

        # ── Step 5: Log the interaction ──────────────────────────────────────
        log_interaction(user_input, response)


if __name__ == "__main__":
    main()
