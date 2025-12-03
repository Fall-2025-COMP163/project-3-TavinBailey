[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wnCpjX4n)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21707786&assignment_repo_type=AssignmentRepo)
# COMP 163: Project 3 - Quest Chronicles

**AI Usage: Free Use (with explanation requirement)**

## Overview

Build a complete modular RPG adventure game demonstrating mastery of **exceptions and modules**.

## Getting Started

### Step 1: Accept Assignment
1. Click the assignment link provided in Blackboard
2. Accept the assignment - this creates your personal repository
3. Clone your repository to your local machine:
```bash
git clone [your-personal-repo-url]
cd [repository-name]
```

### Step 2: Understand the Project Structure

Your repository contains:

```
quest_chronicles/
├── main.py                     # Game launcher (COMPLETE THIS)
├── character_manager.py        # Character creation/management (COMPLETE THIS)
├── inventory_system.py         # Item and equipment management (COMPLETE THIS)
├── quest_handler.py            # Quest system (COMPLETE THIS)
├── combat_system.py            # Battle mechanics (COMPLETE THIS)
├── game_data.py                # Data loading and validation (COMPLETE THIS)
├── custom_exceptions.py        # Exception definitions (PROVIDED)
├── data/
│   ├── quests.txt             # Quest definitions (PROVIDED)
│   ├── items.txt              # Item database (PROVIDED)
│   └── save_games/            # Player save files (created automatically)
├── tests/
│   ├── test_module_structure.py       # Module organization tests
│   ├── test_exception_handling.py     # Exception handling tests
│   └── test_game_integration.py       # Integration tests
└── README.md                   # This file
```

### Step 3: Development Workflow

```bash
# Work on one module at a time
# Test your code frequently

# Commit and push to see test results
git add .
git commit -m "Implement character_manager module"
git push origin main

# Check GitHub for test results (green checkmarks = passed!, red xs = at least 1 failed test case. Click the checkmark or x and then "Details" to see what test cases passed/failed)
```

## Core Requirements (60 Points)

### Critical Constraint
You may **only** use concepts covered through the **Exceptions and Modules** chapters. 

### 🎨 Creativity and Customization

This project encourages creativity! Here's what you can customize:

**✅ FULLY CUSTOMIZABLE:**
- **Character stats** - Adjust health, strength, magic for balance
- **Enemy stats** - Make enemies easier or harder
- **Special abilities** - Design unique abilities for each class
- **Additional enemies** - Add your own enemy types beyond the required three
- **Game mechanics** - Add status effects, combos, critical hits, etc.
- **Quest rewards** - Adjust XP and gold amounts
- **Item effects** - Create unique items with creative effects

**⚠️ REQUIRED (for testing):**
- **4 Character classes:** Warrior, Mage, Rogue, Cleric (names must match exactly)
- **3 Enemy types:** "goblin", "orc", "dragon" (must exist, stats flexible)
- **All module functions** - Must have the specified function signatures
- **Exception handling** - Must raise appropriate exceptions

**💡 CREATIVITY TIPS:**
1. Start with required features working
2. Add creative elements incrementally
3. Test after each addition
4. Be ready to explain your design choices in the interview
5. Bonus interview points for thoughtful, balanced customization!

**Example Creative Additions:**
- Vampire enemy that heals when attacking
- Warrior "Last Stand" ability that activates when health is low
- Poison status effect that deals damage over time
- Critical hit system based on character stats
- Rare "legendary" weapons with special effects

### Module 1: custom_exceptions.py (PROVIDED - 0 points to implement)

**This module is provided complete.** It defines all custom exceptions you'll use throughout the project.

### Module 2: game_data.py (10 points)

### Module 3: character_manager.py (15 points)

### Module 4: inventory_system.py (10 points)

### Module 5: quest_handler.py (10 points)

### Module 6: combat_system.py (10 points)

### Module 7: main.py (5 points)

## Automated Testing & Validation (60 Points)

## Interview Component (40 Points)

**Creativity Bonus** (up to 5 extra points on interview):
- Added 2+ custom enemy types beyond required three
- Designed unique and balanced special abilities
- Implemented creative game mechanics (status effects, advanced combat, etc.)
- Thoughtful stat balancing with clear reasoning

**Note:** Creativity is encouraged, but functionality comes first! A working game with required features scores higher than a broken game with lots of extras.

### Update README.md

Document your project with:

1. **Module Architecture:** Explain your module organization
2. **Exception Strategy:** Describe when/why you raise specific exceptions
3. **Design Choices:** Justify major decisions
4. **AI Usage:** Detail what AI assistance you used
5. **How to Play:** Instructions for running the game

### What to Submit:

1. **GitHub Repository:** Your completed multi-module project
2. **Interview:** Complete 10-minute explanation session
3. **README:** Updated documentation

## Protected Files Warning

⚠️ **IMPORTANT: Test Integrity**

Test files are provided for your learning but are protected. Modifying test files constitutes academic dishonesty and will result in:

- Automatic zero on the project
- Academic integrity investigation

You can view tests to understand requirements, but any modifications will be automatically detected.

## Module-by-Module Description

| Module | Key Functions | Purpose |
|--------|---------------|---------|
| `main.py` | `start_game()`, `load_character()`, `save_character()` | Game launcher; handles player input, starts gameplay loop |
| `character_manager.py` | `create_character()`, `load_character()`, `save_character()`, `gain_experience()`, `level_up()` | Manages character creation, leveling, and persistence |
| `inventory_system.py` | `add_item()`, `remove_item()`, `use_item()`, `equip_item()` | Manages items, equipment, and inventory effects |
| `quest_handler.py` | `accept_quest()`, `complete_quest()`, `abandon_quest()`, `get_active_quests()`, `get_completed_quests()`, `get_available_quests()` | Handles quest acceptance, completion, prerequisites, and rewards |
| `combat_system.py` | `attack_enemy()`, `use_ability()`, `enemy_turn()`, `calculate_damage()` | Implements battle mechanics, turn-based combat, abilities, and damage calculations |
| `game_data.py` | `load_quests()`, `load_items()`, `validate_data()` | Loads quests and items from external files; validates data integrity |
| `custom_exceptions.py` | `InvalidCharacterClassError`, `QuestNotFoundError`, `InsufficientLevelError`, etc. | Defines all custom exceptions for robust error handling |
| `data/quests.txt` | — | Stores quest definitions, including rewards, prerequisites, and levels |
| `data/items.txt` | — | Stores item information, including effects and stats |
| `data/save_games/` | — | Stores player save files automatically |

## Exception Strategy

Custom exceptions enforce game rules:

| Exception | Purpose |
|-----------|---------|
| `InvalidCharacterClassError` | Raised when the player selects a non-existent character class |
| `CharacterNotFoundError` | Raised when trying to load a non-existent character |
| `SaveFileCorruptedError` | Raised when a save file is invalid or corrupted |
| `QuestNotFoundError` | Raised when a quest ID does not exist in data |
| `QuestRequirementsNotMetError` | Raised when prerequisites or requirements for a quest are unmet |
| `QuestAlreadyCompletedError` | Raised when attempting to accept a completed quest |
| `QuestNotActiveError` | Raised when attempting to complete or abandon a non-active quest |
| `InsufficientLevelError` | Raised when character level is too low for a quest |

## Design Choices

- **Character Classes:** Warrior, Mage, Rogue, Cleric  
- **Enemy Types:** Goblin, Orc, Dragon (custom enemies can be added)  
- **Quest System:** Tracks active, completed, and available quests with rewards and prerequisites  
- **Inventory System:** Supports item acquisition, usage, and stat effects  
- **Combat System:** Turn-based with attack, abilities, and enemy interaction  
- **Data-Driven:** All quests and items loaded from external `.txt` files for flexibility  
- **Exception Handling:** Ensures game rules are enforced and prevents invalid actions

## AI Usage

AI assistance was used for:

- Code review and bug checking across modules
- Adding detailed inline comments and docstrings
- Explaining error handling strategies
- Verifying logic for quest management and tracking

## How to Play

1. Clone the repository:

```bash
git clone https://github.com/Fall-2025-COMP163/project-3-TavinBailey.git
cd quest_chronicles
