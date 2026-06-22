# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked like your average number guessing game
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hints were backwards, so even though the secret number was 16, it kept telling me to go higher after I guessed 90.
  2. The "New Game" button does not work.
  3. On every even-numbered attempt, the hint flips again due to the secret being secretly converted to a string, so string comparisons give wrong results, making hints unreliable even on guesses where the basic hint was correct.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| # | Input | Expected Behavior | Actual Behavior | Console Error / Output |
|:-:|---|---|---|:---:|
| 1 | Guess **95** (secret is 16) | "Go LOWER" hint | "Go HIGHER" hint shown | None |
| 2 | Click **New Game** button | Starts a fresh game | No response | None |
| 3 | Guess **5** on attempt 2 (secret is 50) | "Go HIGHER" hint | "Go LOWER" hint (string comparison flip) | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I utilized Claude Code for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude identified that the hint messages in `check_guess` were swapped — "Too High" was paired with "Go HIGHER!" when it should say "Go LOWER!". It suggested moving the function to `logic_utils.py` and correcting the messages there. I verified this by running the game and guessing a number I knew was above the secret; the hint now correctly told me to go lower.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude initially flagged the attempt counter as a separate bug (starting at 1 instead of 0), suggesting it caused the game to end one guess early. After testing manually, I found this was a display issue rather than a logic-breaking bug and chose not to fix it in this phase, since the grader confirmed it was lower priority. The AI was technically right about the off-by-one but overstated its impact.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I used two checks: first I ran `pytest` to confirm the targeted test cases passed, then I ran the live app with `python3 -m streamlit run app.py` and manually guessed numbers above and below the secret to verify the hints matched what I expected.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - I ran `pytest tests/test_game_logic.py -v` after fixing Bug 1. The test `test_too_high_message_says_go_lower` called `check_guess(90, 16)` and asserted `"LOWER"` was in the returned message. It passed, confirming the swap was corrected. I also ran `test_no_string_comparison_large_vs_small` which called `check_guess(9, 10)`. This would have returned `"Too High"` under the old string-comparison bug, but now correctly returns `"Too Low"`.

- Did AI help you design or understand any tests? How?
  - Yes. Claude pointed out that the existing starter tests would fail after the refactor because they compared the full return value (`result == "Win"`) instead of unpacking the tuple. It updated the tests to use `outcome, message = check_guess(...)` and added two new tests per bug: one for the outcome label and one for the message direction, which gave me clearer signal about exactly what was broken.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time a user clicks a button or types something in a Streamlit app, the entire Python script runs again from top to bottom, that's called a "rerun." This means any regular variable you set gets wiped out on the next rerun. Session state is Streamlit's fix for this: it's a dictionary (`st.session_state`) that persists across reruns, so things like the secret number, attempt count, and score survive each interaction. Think of it like a whiteboard that stays up between rounds, while everything else on the table gets cleared.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Writing a pytest case immediately after fixing a bug — not after the whole project is done. It forced me to think precisely about what "fixed" actually means and gave me a safety net if I accidentally broke something while working on a different part of the code.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I would give the AI a smaller, more focused scope per prompt. When I asked Claude to identify all bugs at once, it surfaced several at the same time and I had to manually decide which were real priorities. A tighter prompt like "find bugs only in the check_guess function" would have kept the conversation more actionable.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - I used to assume AI-generated code was either fully correct or obviously broken. This project showed me it can be subtly wrong in ways that look intentional — like swapping messages instead of logic — which means you have to test it just as carefully as code you wrote yourself.
