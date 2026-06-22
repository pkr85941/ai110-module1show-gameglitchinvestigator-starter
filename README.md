# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose:**
A number guessing game built with Streamlit where the player tries to guess a secret number within a limited number of attempts. After each guess, the game provides a "Too High" or "Too Low" hint to guide the next guess. The intentional bugs in the starter code made the game unplayable — this project was about finding and fixing those bugs using AI-assisted debugging.

**Bugs Found:**
1. **Swapped hint messages** — `check_guess` returned "Go HIGHER!" when the guess was too high and "Go LOWER!" when it was too low. The outcome labels were correct but the display messages were backwards.
2. **Even-attempt string comparison** — On every even-numbered attempt, the secret number was secretly cast to a string. This caused lexicographic comparisons (e.g. `"9" > "10"` is `True`) to produce wrong hints on alternating guesses.

**Fixes Applied:**
- Moved `check_guess` into `logic_utils.py` and corrected the hint messages so "Too High" maps to "Go LOWER!" and "Too Low" maps to "Go HIGHER!".
- Removed the even-attempt `str()` conversion in `app.py` so the secret is always compared as an integer.

## 📸 Demo Walkthrough

1. Player selects **Normal** difficulty (range 1–100, 8 attempts).
2. Player guesses **40** — secret is 73 — game returns **"Go HIGHER!"** and decrements attempts.
3. Player guesses **80** — game returns **"Go LOWER!"** and decrements attempts.
4. Player guesses **73** — game returns **"🎉 Correct!"**, score is calculated, and balloons appear.
5. Player clicks **New Game** to reset and start a fresh round.

## 🧪 Test Results

```
$ python3 -m pytest tests/ -v
============================= test session starts ==============================
platform darwin -- Python 3.12.6, pytest-9.0.3, pluggy-1.6.0
collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED     [ 57%]
tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED     [ 71%]
tests/test_game_logic.py::test_no_string_comparison_large_vs_small PASSED [ 85%]
tests/test_game_logic.py::test_no_string_comparison_two_digit PASSED     [100%]

============================== 7 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
