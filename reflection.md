# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|      Input      |                  Expected Behavior                  |                   Actual Behavior                    |            Console Output / Error            |
|-----------------|-----------------------------------------------------|------------------------------------------------------|----------------------------------------------|
| 1               | Go Higher!                                          | Go Lower!                                            |I should not say lower at 1                   |
| Difficult: Easy | "Guess a number between 1 and 20. Attempts left: 6" | "Guess a number between 1 and 100. Attempts left: 5" |Incorrect Display for Difficulty and Attempts |
| Difficult: Hard | Range: 1 to 100                                     |Range: 1 to 50                                        |Incorrect Display of Range per Difficulty     |

- starting a new game does not work after losing
- the square box under "Make a guess", it does not update the difficulty and the guesses.
- After losing one game, I am unable to start a new game
- Attempts allowed is 1 less than what it says on the left side bar
- 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  The AI tools I used for this project is Coilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  AI suggestion that was correct would be updating the score based on outcome and checking the guess against secret.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  AI suggestion that was incorrect was keeping the ranges for each difficulty. The higher the difficulty means the lower chance of getting the correct guess. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  The way I determine if the bug was fixed by using pytest to make sure it passes.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  The manual test I ran would be starting a new game. It shows that the code works as expected since it resets the guesses and have a new number.
- Did AI help you design or understand any tests? How?
  The AI help me with design interms of figuring out what is going on the frontend. The tests that it created made me realized that there are edge cases that I am forgetting about. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit "reruns" runs continuously without closing the app and reruning it. The session state keeps on refreshing after we save our code with new changes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  One habit from this project that I want to reuse in future labs or projects is breaking the project into smaller parts and understand the testings.
- What is one thing you would do differently next time you work with AI on a coding task?
  The one thing I would do differently next time when I work with AI on a coding task is to think about the design more often.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project changed my view on AI generated code by helping resolve small issues and improve my speed on debuging. 
