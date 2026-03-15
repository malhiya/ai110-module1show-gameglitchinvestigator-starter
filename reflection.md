# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
(1) One thing I noticed when I played it the first time was that the hints kept telling me to go lower even though the secret number was higher than my guess. I also noticed that the hints seem to be the be more random and incorrect (for example: when the secret number is lower than my guess, it tells me to guess higher and another time it would correctly say to go lower). 
(2) the hints suggesting to go out of range. It hinted to go lower even when I inputted the lowest number allowed (1). It would be better to say go higher since it isn't possible to go lower (unless fractions are allowed). 
(3) The 'New Game' button does not work after you played the first. In order to play the game again, I have to refresh the whole page
The game also accepted negative numbers and numbers above 100. It would be better to have a out of bounds/ invalid input error, with a message saying to guess in the range


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

- I used Claude Code as an AI agent and ChatGPT to ask any logistical questions. 
- One example of a correct suggestion was the high/low bug for the hints. Claude Code helpped find the logic where the bug was. I was able to verify the fix with my own understanding of python. I also played the game and used pytests to verify the work. 
- One example of a misleading AI suggestion was when I asked how it would add the out of range check for numbers outside 1 and 100. The AI suggested going in app.py and changing the UI code. The solution was a bit confusing and I then responded by suggesting to add the check in the parse_guess function which it agreed with for a more simpler solution. I then verified the result by doing a pytest and playing the game again. I also tried to verify by asking if there could be any confilcts with the added code and somewhere else in the program, whihc the AI believed there wasn't (and it was true).

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
- I decided if a bug was really fixed if it passed the  pytest and also if I didn't notice ant errors when playing the game a few times. 

- One test I ran using pytest was for the high/low hint bug. At first the test failed. And I was confused since playing the game didn't show any apparent errors. I then asked Claude Code what the error message meant and it explained how the it was comparing a tuple to a string. I then worked with the AI to fix the comparison and it worked. It showed what the return type of certain functions and actions and helped me parse it for the tests. 
- AI helped me break down tests as they are a new topic for me. It helped me feel more comfortable with the syntax. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit "reruns" happen every time you interact with your app, like clicking a button and the script runs from top to bottom again. I learned that session state is a way to remember values (user inputs) across reruns so you don’t lose them
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I would like to reuse is to always ask AI to explain something it bring up or points to if I don't understand it. This forces me to learn along the way and get a better understanding of the the code. 
One thing I would do differently is do a better job at haing different cchats open for each bug. I did this well, however, I would accidently ask it a random question once I thought I had a bug fixed.
I learned that AI generated code is very prone to make mistakes or change a small thing that can create a big error. It's important to write clear messages, ask questions, use your own understanding of CS, and double check the AI code before implementing it. 
