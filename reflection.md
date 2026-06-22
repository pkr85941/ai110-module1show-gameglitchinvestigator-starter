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
I utilized Claude Code for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
