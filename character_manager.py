"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: Tavin Bailey

AI Usage: AI used to check all errors.

This module handles character creation, loading, and saving.
"""

import os # os: Used for file handling (create directories, check existence, delete files).
from custom_exceptions import (
    InvalidCharacterClassError, # Raised when user tries to create a character with an invalid class.
    CharacterNotFoundError, # Raised when a save file doesn’t exist.
    SaveFileCorruptedError, # Raised when save file cannot be read.
    InvalidSaveDataError, # Raised when save file is incorrectly formatted.
    CharacterDeadError # Raised when operations are attempted on dead characters.
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]

    # Define base stats for each class
    valid_classes = {
        "Warrior": {"health": 120, "strength": 15, "magic": 5},
        "Mage": {"health": 80, "strength": 8, "magic": 20},
        "Rogue": {"health": 90, "strength": 12, "magic": 10},
        "Cleric": {"health": 100, "strength": 10, "magic": 15}
    }

    # Validate input class
    if character_class not in valid_classes:
        # Raise error with the invalid class and list of valid ones
        # ', '.join(...) makes a comma-separated string of class names
        raise InvalidCharacterClassError(
            f"'{character_class}' is not a valid class. "
            f"Valid classes: {', '.join(valid_classes.keys())}"
        )

    # Extract stats from the selected class
    stats = valid_classes[character_class]

    # Return dictionary representing character
    return {
        "name": name,
        "class": character_class,
        "level": 1, # Level starts at 1
        "health": stats["health"], # Current health stat
        "max_health": stats["health"], # Max health stat
        "strength": stats["strength"], # Strength stat
        "magic": stats["magic"], # Magic stat
        "experience": 0, # XP starts at 0
        "gold": 100, # Starting gold = 100
        "inventory": [], # Empty inventory
        "active_quests": [], # No active quests initially
        "completed_quests": [] # No completed quests initially
    }

def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    os.makedirs(save_directory, exist_ok=True) # Ensure save directory exists
    filename = os.path.join(save_directory, f"{character['name']}_save.txt")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            # Save all key-value pairs in uppercase
            for key, value in character.items():
                key_str = key.upper()  # Required by tests
                f.write(f"{key_str}: {value}\n")
        return True
    except Exception as e:
        raise SaveFileCorruptedError(str(e)) # Wrap any I/O error


def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    filename = os.path.join(save_directory, f"{character_name}_save.txt")


    if not os.path.exists(filename): # Check if file exists
        raise CharacterNotFoundError(f"No save found for {character_name}.")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines() # Read file contents
    except Exception as e:
        raise SaveFileCorruptedError(str(e))

    data = {}

    # Parse lines into key-value dictionary
    try:
        for line in lines:
            line = line.strip()
            if not line:
                continue

            if ": " not in line:
                raise InvalidSaveDataError("Invalid line in save file.")

            key, value = line.split(": ", 1)
            key = key.strip().lower()
            data[key] = value.strip()
    except InvalidSaveDataError:
        raise
    except Exception as e:
        raise SaveFileCorruptedError(str(e))

    # Convert CSV strings to lists
    def parse_list(value):
        return [] if value == "" else [x for x in value.split(",")]

    # Convert all fields to correct types
    character = {
        "name": data["name"],
        "class": data["class"],
        "level": int(data["level"]),
        "health": int(data["health"]),
        "max_health": int(data["max_health"]),
        "strength": int(data["strength"]),
        "magic": int(data["magic"]),
        "experience": int(data["experience"]),
        "gold": int(data["gold"]),
        "inventory": parse_list(data.get("inventory", "")),
        "active_quests": parse_list(data.get("active_quests", "")),
        "completed_quests": parse_list(data.get("completed_quests", ""))
    }

    return character

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    if not os.path.exists(save_directory):
        return [] # Directory doesn't exist, return empty list

    entries = []
    try:
        for fn in os.listdir(save_directory):
            if fn.endswith("_save.txt"):
                entries.append(fn[:-9])  # remove "_save.txt"
    except Exception:
        return [] # If directory can't be read, return empty list rather than crashing

    return entries

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    filename = os.path.join(save_directory, f"{character_name}_save.txt")

    if not os.path.exists(filename):
        raise CharacterNotFoundError(f"{character_name} does not exist.")

    os.remove(filename)
    return True

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
    if character["health"] <= 0:
        raise CharacterDeadError("Cannot gain XP while dead.")

    character["experience"] += xp_amount

    leveled_up = False

    # Handle multiple level-ups if enough XP
    while character["experience"] >= character["level"] * 100:
        character["experience"] -= character["level"] * 100
        character["level"] += 1
        character["max_health"] += 10
        character["strength"] += 2
        character["magic"] += 2
        character["health"] = character["max_health"] #Heal on level-up
        leveled_up = True

    return leveled_up

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
    new_total = character["gold"] + amount

    if new_total < 0:
        raise ValueError("Cannot have negative gold.")

    character["gold"] = new_total
    return character["gold"]

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    if character["health"] <= 0:
        raise CharacterDeadError("Cannot heal a dead character.")

    original = character["health"]
    character["health"] = min(character["health"] + amount, character["max_health"])
    return character["health"] - original # Return actual amount healed

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    return character["health"] <= 0

def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    if character["health"] > 0:
        return False # Already alive
    
    character["health"] = character["max_health"] // 2

    return True

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists

    # List of all keys that every character must have
    required = [
        "name", "class", "level", "health", "max_health",
        "strength", "magic", "experience", "gold",
        "inventory", "active_quests", "completed_quests"
    ]
    # Check that all required fields exist in the dictionary
    for key in required:
        if key not in character:
            # Raise an error immediately if any required key is missing
            raise InvalidSaveDataError(f"Missing field: {key}")

    # Check that numeric fields are integers
    for field in ["level", "health", "max_health", "strength", "magic", "experience", "gold"]:
        if not isinstance(character[field], int):
            # Raise an error if a numeric field is not an integer
            raise InvalidSaveDataError(f"Field {field} must be an integer.")

    # Check that list fields are actually lists
    for field in ["inventory", "active_quests", "completed_quests"]:
        if not isinstance(character[field], list):
            # Raise an error if a field that should be a list isn't a list
            raise InvalidSaveDataError(f"Field {field} must be a list.")

    # If all checks pass, return True indicating the character is valid
    return True

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    try:
        char = create_character("Lily", "Healer") # "Healer" is invalid
        print("Created:", char)
    except Exception as e:
        print("Error:", e)
    # try:
    #     char = create_character("TestHero", "Warrior")
    #     print(f"Created: {char['name']} the {char['class']}")
    #     print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    # except InvalidCharacterClassError as e:
    #     print(f"Invalid class: {e}")

    try:
        save_character(char)
        print("Character saved successfully")
    except Exception as e:
        print(f"Save error: {e}")

    # Test saving
    # try:
    #     save_character(char)
    #     print("Character saved successfully")
    # except Exception as e:
    #     print(f"Save error: {e}")

    try:
        loaded = load_character("TestHero")
        print(f"Loaded: {loaded['name']}")
    except CharacterNotFoundError:
        print("Character not found")
    except SaveFileCorruptedError:
        print("Save file corrupted")
    # Test loading
    # try:
    #     loaded = load_character("TestHero")
    #     print(f"Loaded: {loaded['name']}")
    # except CharacterNotFoundError:
    #     print("Character not found")
    # except SaveFileCorruptedError:
    #     print("Save file corrupted")
