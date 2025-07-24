import random
from tools import roll_dice, generate_event

def narrator_agent(player_choice):
    if "explore" in player_choice.lower():
        return generate_event()
    elif "fight" in player_choice.lower():
        return "A monster blocks your path!"
    else:
        return "You decide to rest at the campfire."

def monster_agent():
    dice = roll_dice()
    if dice >= 4:
        return f"You rolled a {dice}. You defeated the monster!"
    else:
        return f"You rolled a {dice}. The monster wounded you. Try again!"

def item_agent():
    items = ["Sword of Light", "Magic Potion", "Golden Shield", "Mystery Scroll"]
    return f"You received: {random.choice(items)}"