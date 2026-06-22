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

- [✔️] Describe the game's purpose.
   The game's purpose is to guess the game with a limited guesses if the guesses run out, you lose the game. If you guess the correct answer, you win the game and get points.
- [✔️] Detail which bugs you found.
   The bugs I found were logic and interface. One of the logic bug would be higher and lower being incorrect. The other one would be the attempt counter, it is 1 off the counter. The visual bug would be that when we change the difficulty visually. I would change the difficulty from Easy, Normal, and Hard, but the range does not change or the number of attempts. 
- [✔️] Explain what fixes you applied.
   For each fix, I put in the issues and debug and test each of them. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 1
2. Game returns "Go HIGHER!"
3. User enters a guess of 10 → "Go HIGHER!"
4. User enters a guess of 43 → "Go LOWER!"
5. User enters a guess of 43 → "🎉Correct!"
6. "You won! The secret was 42. Final score: 35"
7. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= 5 passed in 0.02s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
