# Lighthouse 💡
#### Video Demo: <URL HERE>
#### GitHub Repository: https://github.com/Shimona012/Lighthouse
#### Description:

Lighthouse is a terminal-based,menu-driven mental health journaling application as well as a basic resource to guide teens, who have 'feels'. Its Built for teenagers. It provides a private, low-pressure space to write about how they are feeling, understand their emotions, and access coping resources, all offline, with no account required. The name Lighthouse was chosen intentionally: a lighthouse cannot save ships, but it can guide them. That is what this application tries to be, a guiding beacon.

---

## What the Project Does

The application has four main areas: a Journal, a Calendar, a Support system, and a Recommendations section. Each is accessible from a main menu and loops until the user decides to leave.

When a user writes a journal entry, the application runs keyword scoring across 14 emotional categories — stress, loneliness, sadness, anxiety, anger, academic pressure, abuse, crisis, burnout, grief, self-esteem, family issues, unknown, and happiness, and assigns the entry an emotion automatically. The user can also optionally provide their own emotion label, which the app will fuzzy-match to the closest valid category. If crisis or abuse keywords are detected in the content, those always override any claimed emotion, regardless of what the user said. This was a deliberate design choice: a teenager should never be able to accidentally route themselves away from crisis support just because they labelled their mood as something else.
[Fuzzy matching is a data technique that finds approximate matches rather than exact ones]

---

## Files

**`project.py`** — The main application file. Contains the `main` function, all menu logic, the `JournalEntry` class with `emotion_analysis` as a static method, and the following functions at the top level:

- `detect_emotion_with_claim(text, claimed_emotion)` — Takes journal content and an optional user-provided emotion label. Returns the final emotion key and the detected emotion separately. Crisis and abuse keywords always override the claimed emotion.
- `closest_emotion(user_emotion)` — Uses `difflib.get_close_matches` to fuzzy-match a user's typed emotion label to the nearest valid internal key. Returns `unknown_help` if nothing matches closely enough.
- `display_emotion(key)` — Converts internal emotion keys like `stress_overwhelm` into user-facing single words like `Stressed`. Prevents internal back-end details from leaking into the UI and making it displeasing for the user.
- `show_moreable(items, title, shown_set)` — Displays one item at a time from a list, tracking which items have already been shown so the user always sees something new.
- `choose_emotion()` — Displays the 14-option emotion menu and returns the corresponding internal key.
- `journal()` — Handles all journal operations: adding, reading, editing, and deleting entries stored locally via `pickle`. 
- `support()` — Routes the user to distractions, support techniques, focus tools, or emergency contacts based on their chosen emotion.
- `calendar_view()` — Lets the user browse past entries by month and day. Shows a calendar.

**`Emotional_Data.py`** — A data file containing the `EMOTIONS` dictionary. Each of the 14 emotion keys maps to a nested dictionary with: `keywords` (for detection), `analysis` (a description shown to the user), `distractions` (jokes, quotes, activities, memes), `support` (grounding, breathing, comfort, resources, hotlines, reassurance), `focus` (study methods, task breakdown, motivation, productivity), and `emergency` (crisis lines, chat support, trusted contact guidance). The content is for basic,minimal guidance and the crisis and abuse sections contain no harmful suggestions, 
**`test_project.py`** — Contains pytest tests for the three required top-level functions: `detect_emotion_with_claim`, `closest_emotion`, and `display_emotion`. Also includes additional tests for `JournalEntry.emotion_analysis` and the `JournalEntry` object itself.

**`requirements.txt`** — Lists pip dependencies: `rich` and `cowsay`.

**`README.md`** — Gives an idea about the project.
---

## Design Choices

**Keyword-based detection over machine learning** — A simpler approach was chosen deliberately. ML models require more specialised software at times,or access to the internet or more resources.Especially in cases involving one's mental state its dangerous to give certified help. Hence, this program only appeals as a basic guidance software rather than claiming to help people feel magically better. Keyword scoring is transparent, fast, fully offline, and easy to audit. The tradeoff is that it can be fooled by sarcasm or mixed signals, but for a journaling tool aimed at teenagers writing genuinely about their feelings, it performs well enough.

The usual python terminal interface however was too bland to garner interest from fellow teenagers. It also made it hard to discern various feature from one another. So rich module was used to make it more engaging and user-friendly.

**Pickle for storage** — Journal entries are stored locally in a binary file using Python's `pickle` module. This keeps the app fully self-contained with no external database. For a personal private journal, binary is the best choice as it prevents anyone from reading it.

**Claimed emotion with crisis override** — Letting users label their own emotion respects their self-awareness. The hard override for crisis keywords exists because getting that routing wrong has real consequences. Safety was prioritised over user control in that specific case.

**One entry per day** — Enforced to encourage reflection rather than compulsive logging. A journal should feel meaningful, not like a feed.

**Rich for the terminal interface** — The default Python terminal was too plain to engage teenagers.
Rich was used to add panels, colour, rules, and alignment, making each section visually distinct
and easier to navigate without overwhelming the user.

---

## How to Run

Install dependencies:
```
pip install -r requirements.txt
```

Run the application(only if you are in the same directory where it is stored):
```
python project.py
```

Run tests:
```
pytest test_project.py 
```

A `data/` folder is created automatically on first run to store journal entries locally.

---

> Lighthouse is not a replacement for professional mental health support.
> It is a guiding software to provide a minimal relief or even distraction so that the user calms down and goes seeking actual help.
> The project is also a basic one and is up for additional features in due time as it targets an important and critical issue of society.
> If you or someone you know is in crisis, please contact a local helpline or emergency services.
