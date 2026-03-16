# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The enter button does not submit the guess, When I click submit guess. It also does not automatically update the array, I have to submit a new guess before it updates
The hints were completely backwards — no matter what number I typed, it kept telling me to go higher even when my guess was way above the secret number.
The range display in the info bar was always "1 and 100" so switching to Easy or Hard didn't change what it showed.
On top of that, the Hard difficulty range was 1–50, which is actually easier than Normal's 1–100, so the difficulty labels were another glitch.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Amazon Q to help investigate and fix the bugs.
One suggestion that was correct was when I asked it to identify why the hints were wrong — it pointed directly to the swapped return messages in check_guess, where "Go HIGHER!" was being returned when the guess was too high instead of "Go LOWER!". I verified this by running the test test_too_high_message_says_go_lower and test_too_low_message_says_go_higher, which passed after the fix.
One suggestion that was misleading was when I asked Amazon Q how to keep the secret number from resetting, and it suggested wrapping the entire game logic in a function and calling st.cache_data on it to cache the secret between reruns. I tried it and the number still reset because st.cache_data is meant for caching data loading functions, not for preserving per-user game state. I verified it was wrong by opening the Developer Debug Info tab and watching the secret change on every button click even with the cache decorator in place. The real fix turned out to be the much simpler if "secret" not in st.session_state check.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when both the automated test passed and I could reproduce the correct behavior manually in the running app.
For the hint direction bug, I ran test_too_high_message_says_go_lower and test_too_low_message_says_go_higher — before the fix both would have failed because the messages were swapped. After moving the corrected logic into logic_utils.py and running pytest, all 10 tests passed.
Amazon Q helped me realize the existing starter tests were also broken because they were comparing check_guess's return value directly to a string like "Win", but the function actually returns a tuple — so the tests would have failed even with correct logic until I unpacked the result.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because Streamlit reruns the entire script from top to bottom every single time you interact with anything on the page including clicking a button. In the original code, random.randint() was called every rerun without checking if a secret already existed, so a new number got picked on every click. The fix was wrapping the secret generation in if "secret" not in st.session_state, which tells Streamlit to only generate a new number the very first time. If I were explaining this to a friend, I'd say: imagine every button click refreshes the whole page like a browser reload — session_state is a small notebook that survives those reloads so your data doesn't disappear.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is writing tests that check the actual message content, not just the outcome label — the test test_too_high_message_says_go_lower caught a real user-facing bug that a simple "Too High" assertion would have missed. Next time I work with AI on a coding task I would read the generated code more carefully before running it, especially any logic that looks or overly clever, because this project showed me that confusing code can hide intentional bugs in plain sight. AI-generated code taught me it can look completely reasonable and still be wrong in ways that only show up when you actually run the code.
