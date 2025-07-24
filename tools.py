import random

def roll_dice():
    return random.randint(1, 6)

def generate_event():
    events = [
        "You found a hidden treasure chest!",
        "A wild monster appears!",
        "You met a mysterious traveler.",
        "You discovered a secret cave."
    ]
    return random.choice(events)