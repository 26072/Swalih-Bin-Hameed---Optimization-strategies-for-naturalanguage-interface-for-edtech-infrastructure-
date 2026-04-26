# =============================================================================
# matcher.py
# Project  : Optimization Strategies for Natural Language Interface
#            for EdTech Infrastructure
# Roll No  : PRJN26-127
# Purpose  : Implements the core NLP matching logic using basic string
#            matching techniques: exact match, keyword scan, and partial
#            (substring) matching.
# =============================================================================

from knowledge_base import KEYWORD_MAP, RESPONSES


def normalize(text: str) -> str:
    """
    Normalize user input:
      - Convert to lowercase
      - Strip leading/trailing whitespace
    This ensures matching is case-insensitive and whitespace-tolerant.
    """
    return text.strip().lower()


def match_intent(user_input: str) -> str:
    """
    Core matching function.
    
    Strategy (in order of priority):
    ─────────────────────────────────────────────────────────────────────
    1. EXACT MATCH     → Check if normalized input exactly matches a keyword.
    2. PHRASE MATCH    → Check if a keyword phrase is fully contained in input.
    3. KEYWORD SCAN    → Check if any individual keyword word appears in input.
    4. FALLBACK        → Return 'unknown' intent if no match found.
    ─────────────────────────────────────────────────────────────────────

    Parameters
    ----------
    user_input : str
        Raw text typed by the user.

    Returns
    -------
    str
        The response string mapped to the matched intent.
    """
    normalized_input = normalize(user_input)

    # ── STRATEGY 1: EXACT MATCH ──────────────────────────────────────────────
    # Check if the full input exactly equals any keyword.
    for intent, keywords in KEYWORD_MAP.items():
        for keyword in keywords:
            if normalized_input == keyword:
                return RESPONSES[intent]

    # ── STRATEGY 2: MULTI-WORD PHRASE MATCH ─────────────────────────────────
    # Check if any MULTI-word keyword phrase is found in the input.
    # Only run for multi-word keywords to avoid substring false positives
    # (e.g., 'hi' matching inside 'this').
    # We pad both sides with a space to enforce word boundaries.
    padded_input = f" {normalized_input} "
    for intent, keywords in KEYWORD_MAP.items():
        for keyword in keywords:
            if len(keyword.split()) > 1:          # multi-word phrases only
                if f" {keyword} " in padded_input or keyword in normalized_input:
                    return RESPONSES[intent]

    # ── STRATEGY 3: INDIVIDUAL WORD SCAN ────────────────────────────────────
    # Tokenize user input into a set of words, then check membership.
    # This is safe from substring issues because we compare whole tokens.
    input_words = set(normalized_input.split())
    for intent, keywords in KEYWORD_MAP.items():
        for keyword in keywords:
            keyword_words = keyword.split()
            # Single-word keyword → check set membership (exact token match)
            if len(keyword_words) == 1:
                if keyword in input_words:
                    return RESPONSES[intent]

    # ── FALLBACK ─────────────────────────────────────────────────────────────
    return RESPONSES["unknown"]


def is_farewell(user_input: str) -> bool:
    """
    Check if the user wants to exit/quit the chatbot.
    Used by the main loop to terminate gracefully.
    
    Parameters
    ----------
    user_input : str
        Raw text typed by the user.

    Returns
    -------
    bool
        True if the user's input indicates a farewell/exit intent.
    """
    normalized_input = normalize(user_input)
    farewell_keywords = KEYWORD_MAP.get("farewell", [])
    
    # Check exact match or keyword contained in input
    for keyword in farewell_keywords:
        if keyword == normalized_input or keyword in normalized_input:
            return True
    return False
