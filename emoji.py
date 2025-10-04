#!/usr/bin/env python3
import random

# Minimal emoji dataset
EMOJIS = {
    "faces": ["😀", "😂", "😍"],
    "animals": ["🐶", "🐱", "🐵"],
    "food": ["🍎", "🍕", "🍔"],
    "symbols": ["❤️", "⭐", "🔥"],
}

def list_categories():
    return list(EMOJIS.keys())

def show_category(cat):
    return EMOJIS.get(cat, [])

def search(term):
    results = []
    for category, emojis in EMOJIS.items():
        if term in category:  # match by category name
            results.extend(emojis)
    return results

def random_emoji():
    all_emojis = sum(EMOJIS.values(), [])
    return random.choice(all_emojis)

# Demo usage
if __name__ == "__main__":
    print("Categories:", list_categories())
    print("Faces:", show_category("faces"))
    print("Search 'food':", search("food"))
    print("Random emoji:", random_emoji())