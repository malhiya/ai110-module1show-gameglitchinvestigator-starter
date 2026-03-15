# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
- (1) One thing I noticed when I played it the first time was that the hints kept telling me to go lower even though the secret number was higher than my guess. I also noticed that the hints seem to be the be more random and incorrect (for example: when the secret number is lower than my guess, it tells me to guess higher and another time it would correctly say to go lower). 
- (2) the hints suggesting to go out of range. It hinted to go lower even when I inputted the lowest number allowed (1). It would be better to say go higher since it isn't possible to go lower (unless fractions are allowed). 
- (3) The 'New Game' button does not work after you played the first. In order to play the game again, I have to refresh the whole page
- The game also accepted negative numbers and numbers above 100. It would be better to have a out of bounds/ invalid input error, with a message saying to guess in the range


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
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
