# -*- coding: utf-8 -*-
COMMON_MEMES = [
    "[link=https://www.reddit.com/r/memes/]Reddit Memes[/link]",
    "[link=https://www.reddit.com/r/Catmemes/]Cat Memes[/link]",
    "[link=https://www.reddit.com/r/wholesomememes/]Wholesome Memes[/link]",
    "[link=https://giphy.com]Giphy[/link]",
    "[link=https://www.reddit.com/r/funny/]r/funny[/link]",
]

COMMON_BREATHING = [
    {
        "name": "Box Breathing",
        "process": [
            "Inhale for 4",
            "Hold for 4",
            "Exhale for 4",
            "Hold for 4",
            "Repeat 4-5 times",
        ],
        "explanation": "Steadies your nervous system with a balanced rhythm.",
    },
    {
        "name": "4-7-8 Breathing",
        "process": [
            "Inhale through your nose for 4",
            "Hold for 7",
            "Exhale slowly for 8",
            "Repeat 3-4 times",
        ],
        "explanation": "Useful when your chest feels tight or your thoughts feel too fast.",
    },
    {
        "name": "Five Finger Breathing",
        "process": [
            "Trace your fingers slowly",
            "Breathe in while tracing up",
            "Breathe out while tracing down",
            "Repeat for every finger",
        ],
        "explanation": "Keeps both your hands and your mind busy.",
    },
    {
        "name": "Slow Exhale",
        "process": [
            "Breathe in gently",
            "Exhale longer than you inhaled",
            "Keep it slow for 1 minute",
        ],
        "explanation": "A long exhale signals safety to your nervous system.",
    },
    {
        "name": "Shoulder Reset",
        "process": [
            "Inhale while lifting your shoulders",
            "Exhale while releasing them",
            "Repeat 5 times",
        ],
        "explanation": "Releases the physical tension that builds up with stress.",
    },
    {
        "name": "Counted Breathing",
        "process": [
            "Count each inhale",
            "Count each exhale",
            "Restart if distracted",
        ],
        "explanation": "Improves focus and calm by giving your brain one simple task.",
    },
]

EMOTIONS = {
    "stress_overwhelm": {
        "keywords": [
            "stressed",
            "stress",
            "overwhelmed",
            "pressure",
            "too much",
            "cant handle",
            "drowning",
            "difficult",
            "overloaded",
            "swamped",
            "under pressure",
            "too many things",
            "can't breathe",
            "can't cope",
            "nervous",
            "anxious",
            "pressuring",
            "pressured",
            "cornered",
            "can't keep up",
            "cannot keep up",
        ],
        "analysis": [
            "User may be mentally overloaded",
            "Possible emotional exhaustion",
            "May benefit from grounding and task breakdown",
        ],
        "distractions": {
            "memes": COMMON_MEMES,
            "jokes": [
                {
                    "text": "Why did the spider join the tech company? Because he was great at building web pages. 🕸️"
                },
                {
                    "text": "I'm reading a book on anti-gravity. It's impossible to put down. 📘"
                },
                {"text": "Why did the coffee file a police report? It got mugged. ☕"},
                {
                    "text": "I'm not lazy. I'm just on low power mode with no charger in sight. 🔋"
                },
                {
                    "text": "My brain has too many tabs open and one of them is playing music. 💻"
                },
                {
                    "text": "I would tell you a joke about procrastination, but I'll do it tomorrow. ⏳"
                },
                {"text": "The deadline and I are not on speaking terms. 📝"},
                {
                    "text": "I asked my stress to leave. It said it was living here now. 😭"
                },
                {
                    "text": "I tried to be productive, but my motivation had other plans. 🤦"
                },
                {"text": "I told my calendar a joke. It took it very literally. 📅"},
                {"text": "My concentration left the group chat. 👻"},
                {
                    "text": "I'm not overwhelmed. I'm just experiencing a dramatic amount of life. 💀"
                },
            ],
            "quotes": [
                {"text": "You do not have to solve everything today."},
                {"text": "Rest is productive too."},
                {"text": "A rough day is not a rough life."},
                {"text": "You can take this one step at a time."},
                {"text": "Small progress still counts."},
                {"text": "You are allowed to move slowly and still be moving."},
                {"text": "You do not need to carry the whole week in one afternoon."},
                {"text": "One calm breath is still a win."},
                {"text": "Today only needs your next step, not your entire future."},
            ],
            "activities": [
                "Listen to calming music, I personally love rain sounds :)",
                "Watch comfort videos, or your comfort series or hey, even cat videos.",
                "Draw or doodle randomly, it doesn't need to make sense just needs to be you.",
                "Take a short walk, if its possible and an appropriate time then nature is more than ready to answer your problems.",
                "Drink water and stretch. It seems simple but reminds your body that you are safe.",
                "Open a window and breathe slowly. Just focus on that, the breath going in and out; in and out; innn and out.",
                "Put your phone down for 5 minutes. Sometimes a break from notifications and constant bombardment grounds you.",
                "Hold something cold and name what you can see. Its not ISPY but it works none the less.",
            ],
        },
        "support": {
            "grounding": [
                {
                    "name": "5-4-3-2-1",
                    "process": [
                        "Name 5 things you can see",
                        "Name 4 things you can touch",
                        "Name 3 things you can hear",
                        "Name 2 things you can smell",
                        "Name 1 thing you can taste",
                        "Good job! It seems silly but it really can help you feel more present. :D",
                    ],
                    "explanation": "It Pulls your brain out of spiraling thoughts and back into the present.",
                },
                {
                    "name": "3-3-3",
                    "process": [
                        "Name 3 things you can see",
                        "Name 3 things you can hear",
                        "Move 3 body parts",
                    ],
                    "explanation": "For a quick reset when your mind feels too loud.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cold water",
                        "Hold something cold",
                        "Focus on the temperature",
                    ],
                    "explanation": "It can interrupt a stress spiral fast.",
                },
                {
                    "name": "Sound Anchoring",
                    "process": [
                        "Play calming music",
                        "Focus on one instrument or sound",
                        "Follow its rhythm",
                    ],
                    "explanation": "Gives your brain one safe thing to hold onto.",
                },
            ],
            "breathing": COMMON_BREATHING,
            "comfort": [
                {"text": "It is okay to pause. 🙂"},
                {"text": "You are allowed to rest."},
                {"text": "One step at a time still counts."},
                {"text": "You do not need to fix everything at once."},
                {"text": "Your pace is allowed to be human."},
            ],
            "resources": [
                "[link=https://jedfoundation.org]JED Foundation[/link]",
                "[link=https://childmind.org]Child Mind Institute[/link]",
                "[link=https://samaritanshope.org/our-services/hey-sam/]Hey Sam[/link]",
            ],
            "hotlines": [
                {
                    "name": "988 Suicide & Crisis Lifeline-USA",
                    "process": [
                        "Call 988",
                        "Text 988",
                        "Use 988 chat on the official site",
                    ],
                    "explanation": "24/7 support for mental health and crisis needs.",
                },
                {
                    "name": "Crisis Text Line-India",
                    "process": ["Call 14416"],
                    "explanation": "24/7 support for mental health and crisis needs in India.",
                },
            ],
            "reassurance": [
                {"text": "Feeling overwhelmed does not mean you are failing."},
                {"text": "You do not have to handle everything at once."},
                {"text": "One thing at a time is enough."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Pomodoro",
                    "process": [
                        "Study for 25 minutes",
                        "Take a 5 minute break",
                        "Repeat 4 times",
                        "Take a bigger break after",
                    ],
                    "explanation": "Makes huge workloads feel less terrifying.",
                },
                {
                    "name": "Active Recall",
                    "process": [
                        "Read a topic once",
                        "Close the book",
                        "Write what you remember",
                        "Check mistakes",
                        "Repeat",
                    ],
                    "explanation": "One of the strongest memory techniques.",
                },
                {
                    "name": "Feynman Technique",
                    "process": [
                        "Choose a topic",
                        "Explain it like teaching a child",
                        "Notice where you struggle",
                        "Relearn weak spots",
                    ],
                    "explanation": "If you cannot explain it simply, you may not fully understand it yet.",
                },
                {
                    "name": "Blurting",
                    "process": [
                        "Study normally",
                        "Close notes",
                        "Write everything remembered",
                        "Compare with notes",
                    ],
                    "explanation": "Turns passive studying into active memory testing.",
                },
                {
                    "name": "Mind Mapping",
                    "process": [
                        "Write the main topic in the center",
                        "Create branches for subtopics",
                        "Connect related ideas visually",
                    ],
                    "explanation": "Helpful for big topics and overloaded brains.",
                },
                {
                    "name": "Spaced Repetition",
                    "process": [
                        "Review after 1 day",
                        "Then 3 days later",
                        "Then 1 week later",
                        "Then 1 month later",
                    ],
                    "explanation": "Helps information stay in long-term memory.",
                },
            ],
            "task_breakdown": [
                {
                    "name": "Chapter Breakdown",
                    "process": ["Chapter", "Topic", "Subtopic", "Questions"],
                    "explanation": "Makes big chunks of work feel smaller.",
                },
                {
                    "name": "10-Minute Start",
                    "process": [
                        "Pick the next smallest step",
                        "Set a 10-minute timer",
                        "Start with that only",
                    ],
                    "explanation": "Good when starting feels hard.",
                },
            ],
            "motivation": [
                {"text": "Progress matters more than perfection."},
                {"text": "Everyone struggles sometimes."},
                {"text": "Done is better than perfect."},
                {"text": "Starting badly is still starting."},
            ],
            "productivity": [
                "Keep your phone away for 20 minutes",
                "Start with the easiest task first",
                "Use timers, time will seem to move faster",
                "Write only 3 tasks for today",
                "Close extra tabs before beginning",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Text or call a trusted friend",
                "Talk to a trusted adult, if that seems safe",
                "Reach out to someone safe",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "988 Suicide & Crisis Lifeline-USA",
                    "process": [
                        "Call 988",
                        "Text 988",
                        "Use 988 chat on the official site",
                    ],
                    "explanation": "24/7 support for mental health and crisis needs.",
                },
                {
                    "name": "Crisis Text Line-India",
                    "process": ["Call 14416"],
                    "explanation": "24/7 support for mental health and crisis needs in India.",
                },
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Use the website to search by country",
                        "Pick call, chat, or text if available",
                    ],
                    "explanation": "Helps find local crisis support.",
                },
                {
                    "name": "Local Emergency Services",
                    "process": [
                        "Use local emergency services if there is immediate danger"
                    ],
                    "explanation": "For urgent physical safety concerns.",
                },
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": [
                        "Open the chat support option",
                        "Share only what feels safe",
                        "Follow the counselor's guidance",
                    ],
                    "explanation": "Youth-focused chat support.",
                },
                {
                    "name": "The Live Love Laugh Helplines",
                    "process": [
                        "Visit the helpline page",
                        "Choose an available support option",
                    ],
                    "explanation": "A mental health helpline directory.",
                },
            ],
            "urgent_steps": [
                "Move away from dangerous objects",
                "Do not stay isolated",
                "Go where other people are if possible",
                "Focus on getting through the next 10 minutes",
            ],
            "reassurance": [
                {"text": "You deserve support."},
                {"text": "You do not have to carry this alone."},
                {"text": "Help is available."},
            ],
            "resources": [
                "[link=https://findahelpline.com]Find A Helpline[/link]",
                "[link=https://988lifeline.org]988 Suicide & Crisis Lifeline[/link]",
                "[link=https://icallhelpline.org/about-the-reyou-chat-line/]iCALL ReYou Chat-line[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]The Live Love Laugh Helplines[/link]",
            ],
        },
    },
    "loneliness_isolation": {
        "keywords": [
            "alone",
            "lonely",
            "isolated",
            "ignored",
            "left out",
            "nobody cares",
            "disconnected",
            "forgotten",
            "unseen",
            "unwanted",
            "abandoned",
        ],
        "analysis": ["User may feel disconnected", "May need social reassurance"],
        "distractions": {
            "activities": [
                "Watch comfort shows or try something new you have been curious about",
                "Join online hobby communities, nothing beats the thrill for learning something new.",
                "Read your favorite books",
                "Message one trusted person with a simple emoji or a sticker",
                "Listen to a podcast that feels friendly",
            ],
            "memes": COMMON_MEMES,
            "jokes": [
                {
                    "text": "I'm not alone, I just have a very exclusive audience of one. 😎"
                },
                {"text": "I told my mirror a joke. It cracked up, literally. 🪞"},
                {
                    "text": "My social battery is at 2%. Still enough for a funny meme, though. 🔋"
                },
                {
                    "text": "Why did the selfie go to therapy? It couldn't picture its future. 📸"
                },
                {
                    "text": "I joined a book club so I could have inner peace and outer snacks. 📚"
                },
            ],
            "quotes": [
                {"text": "Connection can begin with one small message."},
                {
                    "text": "Being alone right now does not mean being forgotten forever."
                },
                {"text": "Loneliness lies to people."},
                {"text": "You do not need perfect words to reach out."},
                {"text": "A tiny message can still count as bravery."},
            ],
        },
        "support": {
            "comfort": [
                {"text": "Your feelings are valid."},
                {"text": "People care more than your thoughts convince you."},
                {"text": "You are not difficult to love."},
                {"text": "A small connection still counts."},
            ],
            "resources": [
                "[link=https://www.7cups.com]7 Cups[/link]",
                "[link=https://jedfoundation.org]JED Foundation[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "grounding": [
                {
                    "name": "Notice Five Things",
                    "process": [
                        "5 things you see",
                        "4 you can touch",
                        "3 you hear",
                        "2 you smell",
                        "1 you taste",
                    ],
                    "explanation": "Brings you back to the present when loneliness feels heavy.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cold water",
                        "Hold something cold",
                        "Focus on the temperature",
                    ],
                    "explanation": "It can interrupt a stress spiral fast.",
                },
                {
                    "name": "Sound Anchoring",
                    "process": [
                        "Play calming music",
                        "Focus on one instrument or sound",
                        "Follow its rhythm",
                    ],
                    "explanation": "Gives your brain one safe thing to hold onto.",
                },
            ],
            "breathing": COMMON_BREATHING,
            "reassurance": [
                {"text": "Loneliness is a feeling, not a fact about who you are."},
                {
                    "text": "Not having found your people yet is not the same as never finding them."
                },
                {"text": "You are worth knowing."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Pomodoro",
                    "process": [
                        "Study for 25 minutes",
                        "Take a 5 minute break",
                        "Repeat 4 times",
                        "Take a bigger break after",
                    ],
                    "explanation": "Short sessions make it easier to start.",
                },
                {
                    "name": "Active Recall",
                    "process": [
                        "Read a topic",
                        "Close notes",
                        "Say what you remember",
                        "Check and repeat",
                    ],
                    "explanation": "Helps the brain stay active.",
                },
            ],
            "task_breakdown": [
                {
                    "name": "One Small Step",
                    "process": ["Pick one task", "Make it tiny", "Do only that"],
                    "explanation": "Useful when feeling stuck or isolated.",
                }
            ],
            "motivation": [
                {"text": "A tiny start is still a start."},
                {"text": "You can build momentum slowly."},
            ],
            "productivity": [
                "Use a timer",
                "Study near a window",
                "Keep the task list small",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Text a trusted person",
                "Call a friend",
                "Reach out to a family member or adult you trust",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "988 Suicide & Crisis Lifeline-USA",
                    "process": ["Call 988", "Text 988", "Use 988 chat"],
                    "explanation": "Available 24/7 in the U.S.",
                },
                {
                    "name": "Crisis Text Line-India",
                    "process": ["Call 14416"],
                    "explanation": "24/7 support for mental health and crisis needs in India.",
                },
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search for support by country",
                        "Choose phone or chat if available",
                    ],
                    "explanation": "Lets you find local support quickly.",
                },
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": [
                        "Open the chat support page",
                        "Write what you feel comfortable sharing",
                    ],
                    "explanation": "Helpful when talking feels hard.",
                }
            ],
            "urgent_steps": [
                "Do not stay alone if you feel unsafe",
                "Move closer to people you trust",
                "Put distance between you and anything harmful",
            ],
            "reassurance": [
                {"text": "You are not a burden."},
                {"text": "Support can start with one message."},
            ],
            "resources": [
                "[link=https://www.7cups.com]7 Cups[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
        },
    },
    "sadness_hopelessness": {
        "keywords": [
            "sad",
            "empty",
            "hopeless",
            "crying",
            "worthless",
            "done",
            "blue",
            "heartbroken",
            "tearful",
            "down",
            "heavy",
            "miserable",
        ],
        "analysis": [
            "Possible depressive thoughts",
            "May need reassurance and support",
        ],
        "distractions": {
            "activities": [
                "Comfort movies",
                "Favorite songs",
                "Nature videos",
                "Soft ambient sounds",
                "Wrap yourself in something comfortable and rest without forcing anything",
            ],
            "memes": COMMON_MEMES,
            "jokes": [
                {
                    "text": "Why did the pillow get promoted? It was outstanding under pressure. 🛏️"
                },
                {
                    "text": "My mood said 'let's spiral,' and honestly that was very rude of it. 🌀"
                },
                {"text": "My feelings booked a one-way trip to sad town. 🚆"},
                {
                    "text": "My heart is doing that thing where it becomes a very dramatic movie. 🎬"
                },
                {
                    "text": "I'm not saying I'm emotionally fragile, but a sad song can end me in one chorus. 🎧"
                },
            ],
            "quotes": [
                {"text": "You have survived difficult days before."},
                {"text": "Feelings can change with time and support."},
                {"text": "You do not need to force yourself to be okay right now."},
                {"text": "A heavy day is still only one day."},
                {"text": "Healing does not have to look impressive."},
            ],
        },
        "support": {
            "grounding": [
                {
                    "name": "Sunlight",
                    "process": [
                        "Sit somewhere with sunlight",
                        "Let your body relax for a minute",
                        "Breathe slowly",
                    ],
                    "explanation": "A gentle reset without much effort.",
                },
                {
                    "name": "Slow Breathing",
                    "process": [
                        "Inhale slowly",
                        "Exhale even slower",
                        "Repeat 5 times",
                    ],
                    "explanation": "Simple and low-pressure.",
                },
            ],
            "resources": [
                "[link=https://childmind.org]Child Mind Institute[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
            "comfort": [
                {"text": "It is okay to feel heavy right now."},
                {"text": "Crying does not mean weakness."},
                {"text": "You can rest without fixing everything."},
                {"text": "Sadness is not a character flaw. It is a human experience."},
                {"text": "You are allowed to feel this without having to explain it."},
                {"text": "You have gotten through hard days before."},
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "breathing": COMMON_BREATHING,
            "reassurance": [
                {"text": "This will not feel this heavy forever."},
                {"text": "Hard seasons end."},
                {"text": "Reaching out even a little bit matters."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Pomodoro",
                    "process": [
                        "Study for 25 minutes",
                        "Take a 5 minute break",
                        "Repeat",
                    ],
                    "explanation": "Short study blocks are easier on low-energy days.",
                },
                {
                    "name": "Active Recall",
                    "process": [
                        "Read once",
                        "Close notes",
                        "Say or write what you remember",
                    ],
                    "explanation": "Helps you stay active instead of just rereading.",
                },
            ],
            "task_breakdown": [
                {
                    "name": "Tiny Start",
                    "process": [
                        "Pick one tiny task",
                        "Do that only",
                        "Stop if you need to",
                    ],
                    "explanation": "Makes starting feel safer.",
                }
            ],
            "motivation": [
                {"text": "Small progress still matters."},
                {"text": "You do not need to do everything today."},
            ],
            "productivity": [
                "Keep the task list short",
                "Use one timer",
                "Work in a quiet place if possible",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Reach out to someone you trust",
                "Text a trusted friend",
                "Tell an adult you feel close to",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "988 Suicide & Crisis Lifeline-USA",
                    "process": ["Call 988", "Text 988", "Use 988 chat"],
                    "explanation": "24/7 support for crisis and mental health.",
                },
                {
                    "name": "Crisis Text Line-India",
                    "process": ["Call 14416"],
                    "explanation": "24/7 support for mental health and crisis needs in India.",
                },
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search by country",
                        "Choose the best available support",
                    ],
                    "explanation": "Finds local crisis help fast.",
                },
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": ["Open the chat line", "Share only what you want"],
                    "explanation": "Good if calling feels too hard.",
                }
            ],
            "urgent_steps": [
                "Stay near other people if you can",
                "Move away from anything harmful",
                "Focus only on the next 10 minutes",
                "You are not alone in this, even if it feels that way right now.",
            ],
            "reassurance": [
                {"text": "You deserve support."},
                {"text": "You do not have to hold this alone."},
            ],
            "resources": [
                "[link=https://childmind.org]Child Mind Institute[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
        },
    },
    "anxiety_panic": {
        "keywords": [
            "panic",
            "anxiety",
            "fear",
            "scared",
            "nervous",
            "overthinking",
            "uneasy",
            "tense",
            "restless",
            "shaking",
            "worried",
            "fearful",
            "can't breathe",
            "cant breathe",
            "cannot calm down",
            "can't calm down",
            "cant calm down",
            "hyper",
            "cannot breathe",
        ],
        "analysis": ["Possible panic response", "Grounding may help immediately"],
        "distractions": {
            "activities": [
                "Listen to calming audios, like rain sounds or soft music",
                "Count objects around you",
                "Watch funny videos",
                "Look for 5 blue things in the room",
                "Hold something comforting, like a soft blanket or a stress ball",
                "Take a slow walk if you can, even just around your room",
            ],
            "memes": COMMON_MEMES,
            "jokes": [
                {
                    "text": "My anxiety tried to run the meeting, but it had no agenda. 📋"
                },
                {
                    "text": "I asked my nerves to calm down. They said, 'We'll take that under advisement.' 😭"
                },
                {"text": "My brain heard one minor inconvenience and chose chaos. 🤡"},
                {
                    "text": "I'm not overthinking. I'm just in the deluxe edition of worry. 🧠"
                },
                {
                    "text": "I set an alarm to remind myself to stop overthinking. I then overthought the alarm. 🔔"
                },
            ],
            "quotes": [
                {"text": "Anxiety is loud but it is not in charge."},
                {"text": "You do not have to believe every worried thought."},
                {
                    "text": "This feeling will pass, even if it does not feel like it right now."
                },
                {"text": "You have handled uncertain moments before."},
            ],
        },
        "support": {
            "breathing": COMMON_BREATHING,
            "comfort": [
                {
                    "text": "Anxiety lies about how permanent and catastrophic things are."
                },
                {
                    "text": "You have survived every anxious moment so far. That is 100 percent."
                },
                {
                    "text": "Your body is trying to protect you. It is just being a bit too enthusiastic."
                },
            ],
            "grounding": [
                {
                    "name": "5-4-3-2-1",
                    "process": [
                        "5 things you can see",
                        "4 things you can touch",
                        "3 things you can hear",
                        "2 things you can smell",
                        "1 thing you can taste",
                    ],
                    "explanation": "A classic grounding reset.",
                },
                {
                    "name": "3-3-3",
                    "process": [
                        "Name 3 things you can see",
                        "Name 3 things you can hear",
                        "Move 3 body parts",
                    ],
                    "explanation": "A short panic interruption.",
                },
                {
                    "name": "Object Focus",
                    "process": [
                        "Pick one nearby object",
                        "Describe its color and texture",
                        "Focus only on details",
                    ],
                    "explanation": "Helps interrupt anxious spirals.",
                },
                {
                    "name": "Wall Support",
                    "process": [
                        "Lean gently against a wall",
                        "Notice the support beneath you",
                        "Take slow breaths",
                    ],
                    "explanation": "Creates physical stability during anxiety.",
                },
                {
                    "name": "Finger Counting",
                    "process": [
                        "Touch each fingertip slowly",
                        "Count each touch",
                        "Repeat calmly",
                    ],
                    "explanation": "Redirects focus into simple actions.",
                },
                {
                    "name": "Breath Watching",
                    "process": [
                        "Notice your breathing without changing it",
                        "Count 5 slow breaths",
                    ],
                    "explanation": "Reduces panic intensity.",
                },
                {
                    "name": "Safe Sound",
                    "process": [
                        "Play calming ambient audio",
                        "Focus on one repeating sound",
                    ],
                    "explanation": "Helps stabilize attention.",
                },
            ],
            "resources": [
                "[link=https://jedfoundation.org]JED Foundation[/link]",
                "[link=https://childmind.org]Child Mind Institute[/link]",
            ],
            "reassurance": [
                {"text": "You are safe right now, even if it does not feel that way."},
                {"text": "Anxiety always passes, even when it feels permanent."},
                {"text": "You have gotten through hard moments before."},
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Pomodoro",
                    "process": [
                        "Study for 25 minutes",
                        "Take a 5 minute break",
                        "Repeat",
                    ],
                    "explanation": "Short sessions are easier when anxious.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "One Task",
                    "process": ["Pick one task", "Do only that task", "Take a break"],
                    "explanation": "Stops overwhelm from growing.",
                }
            ],
            "motivation": [{"text": "One step at a time still counts."}],
            "productivity": [
                "Keep your phone away for 20 minutes",
                "Use a timer",
                "Reduce the task size",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Text or call a trusted friend",
                "Talk to a trusted adult",
                "Reach out to someone safe",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "988 Suicide & Crisis Lifeline-USA",
                    "process": ["Call 988", "Text 988", "Use 988 chat"],
                    "explanation": "24/7 support for crisis and mental health.",
                },
                {
                    "name": "Crisis Text Line-India",
                    "process": ["Call 14416"],
                    "explanation": "24/7 support for mental health and crisis needs in India.",
                },
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search by country",
                        "Choose call or chat if available",
                    ],
                    "explanation": "Finds local support quickly.",
                },
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": ["Open chat support", "Share what feels safe"],
                    "explanation": "A good option when talking is hard.",
                }
            ],
            "urgent_steps": [
                "Move away from dangerous objects",
                "Do not stay isolated",
                "Focus on the next 5 minutes",
            ],
            "reassurance": [
                {"text": "You deserve support."},
                {"text": "Help is available."},
            ],
            "resources": [
                "[link=https://jedfoundation.org]JED Foundation[/link]",
                "[link=https://childmind.org]Child Mind Institute[/link]",
            ],
        },
    },
    "anger_frustration": {
        "keywords": [
            "angry",
            "rage",
            "frustrated",
            "furious",
            "annoyed",
            "mad",
            "irritated",
            "fed up",
            "livid",
        ],
        "analysis": ["Possible emotional overload", "May need cooldown techniques"],
        "distractions": {
            "activities": [
                "Fast walk",
                "Exercise",
                "Music",
                "Movement",
                "Doodling or art",
            ],
            "memes": COMMON_MEMES,
            "jokes": [
                {"text": "My patience left like it had a train to catch. 🚆"},
                {"text": "I'm not mad, I'm just emotionally buffering. ⏳"},
                {"text": "My temper and I are having a very temporary separation. 💔"},
                {
                    "text": "I wanted to stay calm, but my feelings said, 'not today bestie.' 🤝"
                },
                {"text": "I practiced being calm. Then someone talked to me. 🙃"},
            ],
            "quotes": [
                {"text": "You are allowed to feel this. You do not have to act on it."},
                {"text": "Taking space is not weakness."},
                {"text": "Anger is a signal, not a sentence."},
                {"text": "You can be frustrated and still be in control."},
            ],
        },
        "support": {
            "breathing": [
                {
                    "name": "Cooling Breath",
                    "process": [
                        "Breathe in through your nose for 4",
                        "Hold for 4",
                        "Breathe out slowly through your mouth for 8",
                    ],
                    "explanation": "The long exhale slows your heart rate and calms the anger response.",
                },
            ]
            + COMMON_BREATHING,
            "grounding": [
                {
                    "name": "Pause Before Reacting",
                    "process": [
                        "Step away physically",
                        "Drink water",
                        "Wait 10 minutes minimum",
                        "Do not send texts while furious",
                    ],
                    "explanation": "Strong emotions make impulsive decisions feel logical even when they are not.",
                },
                {
                    "name": "Physical Release",
                    "process": [
                        "Fast walk",
                        "Exercise",
                        "Stretch aggressively but safely",
                    ],
                    "explanation": "Anger has physical energy too.",
                },
                {
                    "name": "Doodling or Art",
                    "process": [
                        "Draw your emotions out",
                        "Scribble, tear, be messy if you want",
                        "Focus on the process, not the product",
                    ],
                    "explanation": "Can help release tension and reset your mood.",
                },
            ],
            "comfort": [
                {"text": "Feeling angry does not make you a bad person."},
                {"text": "Strong emotions are human."},
                {"text": "You can choose how to respond even when you feel this way."},
            ],
            "resources": [
                "[link=https://findahelpline.com]Find A Helpline[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]The Live Love Laugh Foundation[/link]",
            ],
            "reassurance": [
                {"text": "You can calm down before deciding anything."},
                {"text": "Pausing is not giving up."},
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Pomodoro",
                    "process": ["Study for 25 minutes", "Take a 5 minute break"],
                    "explanation": "Helps you work without getting more irritated.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "Cool-Down First",
                    "process": ["Pause", "Breathe", "Return to one task"],
                    "explanation": "Do not start hard work while angry.",
                }
            ],
            "motivation": [{"text": "Pause first, act second."}],
            "productivity": [
                "Do not text while angry",
                "Leave the room for a bit",
                "Use music or movement to reset",
                "Confide in a trusted friend if you need to vent safely",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Text a trusted person if you might act impulsively",
                "Talk to someone safe",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search for support by country",
                        "Pick a line or chat option",
                    ],
                    "explanation": "Useful when anger feels out of control.",
                }
            ],
            "chat_support": [
                {
                    "name": "The Live Love Laugh Helplines",
                    "process": ["Visit the helpline page", "Choose a support option"],
                    "explanation": "Can help when you need to talk things through.",
                }
            ],
            "urgent_steps": [
                "Step away for 5 to 10 minutes",
                "Do not make decisions while furious",
                "Focus on breathing slowly",
            ],
            "reassurance": [{"text": "You can calm down before deciding anything."}],
            "resources": [
                "[link=https://findahelpline.com]Find A Helpline[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]The Live Love Laugh Foundation[/link]",
            ],
        },
    },
    "academic_pressure": {
        "keywords": [
            "exam",
            "grades",
            "jee",
            "marks",
            "assignment",
            "study",
            "exams",
            "studies",
            "leaerning",
            "material",
            "neet",
            "school work",
            "college load",
            "resources",
        ],
        "analysis": [
            "User may be under academic stress",
            "May need structure and reassurance",
        ],
        "distractions": {
            "quotes": [
                {"text": "One test does not define your worth."},
                {"text": "Learning is not linear."},
                {"text": "Your brain is allowed to need breaks too."},
                {"text": "A bad test is not a bad life."},
                {"text": "Marks are a snapshot, not your identity."},
            ],
            "memes": COMMON_MEMES,
            "jokes": [
                {
                    "text": "My exam prep and I are in a long-distance relationship. We barely meet. 📚"
                },
                {
                    "text": "I studied for 10 minutes, which is 10 minutes more than my stress expected. ✅"
                },
                {"text": "Why was the math teacher suspicious? Too many problems. ➗"},
                {"text": "I opened my textbook and immediately needed a nap. 📖"},
                {
                    "text": "I don't always study, but when I do, it's accidentally at 2 a.m. 🌙"
                },
                {"text": "My brain looked at revision and said, 'nice try.' 😭"},
            ],
            "activities": [
                "Take a 10 minute walk without your phone.",
                "Organize your desk for 5 minutes only.",
                "Drink water and stretch your shoulders.",
                "Write down the next smallest possible task.",
                "Put on a background playlist and just breathe for a moment before starting.",
            ],
        },
        "support": {
            "reassurance": [
                {"text": "Everyone struggles academically sometimes."},
                {"text": "Your value is bigger than your grades."},
            ],
            "comfort": [
                {"text": "One test does not define your worth."},
                {"text": "Your brain is allowed to need rest."},
                {"text": "Struggle is part of learning, not proof of failure."},
            ],
            "resources": [
                "[link=https://jedfoundation.org]JED Foundation[/link]",
                "[link=https://childmind.org]Child Mind Institute[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "grounding": [
                {
                    "name": "Desk Reset",
                    "process": [
                        "Clear one small part of your desk",
                        "Put away unrelated items",
                        "Take one slow breath",
                        "Look only at the next task",
                    ],
                    "explanation": "Helps reduce overwhelm from clutter and pressure.",
                },
                {
                    "name": "5-4-3-2-1 Method",
                    "process": [
                        "Name 5 things you can see",
                        "4 things you can touch",
                        "3 things you hear",
                        "2 things you smell",
                        "1 thing you taste",
                    ],
                    "explanation": "Reconnects attention to the present moment.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cool water",
                        "Focus only on the temperature",
                        "Take 3 slow breaths",
                    ],
                    "explanation": "Interrupts spiraling stress thoughts.",
                },
                {
                    "name": "Chair Grounding",
                    "process": [
                        "Sit back fully in your chair",
                        "Feel your feet touching the floor",
                        "Relax your shoulders slowly",
                    ],
                    "explanation": "Brings awareness back into the body.",
                },
                {
                    "name": "Window Pause",
                    "process": [
                        "Look outside for one minute",
                        "Notice colors and movement",
                        "Take slow breaths while observing",
                    ],
                    "explanation": "Creates mental distance from academic pressure.",
                },
            ],
            "breathing": COMMON_BREATHING,
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Pomodoro",
                    "process": [
                        "Study for 25 minutes",
                        "Take a 5 minute break",
                        "Repeat 4 times",
                        "Take a bigger break after",
                    ],
                    "explanation": "Makes huge workloads feel less terrifying.",
                },
                {
                    "name": "Active Recall",
                    "process": [
                        "Read a topic once",
                        "Close the book",
                        "Write what you remember",
                        "Check mistakes",
                        "Repeat",
                    ],
                    "explanation": "One of the strongest memory techniques.",
                },
                {
                    "name": "Feynman Technique",
                    "process": [
                        "Choose a topic",
                        "Explain it like teaching a child",
                        "Notice where you struggle",
                        "Relearn weak spots",
                    ],
                    "explanation": "If you cannot explain it simply, you may not fully understand it yet.",
                },
                {
                    "name": "Blurting",
                    "process": [
                        "Study normally",
                        "Close notes",
                        "Write everything remembered",
                        "Compare with notes",
                    ],
                    "explanation": "Turns passive studying into active memory testing.",
                },
                {
                    "name": "Mind Mapping",
                    "process": [
                        "Write the main topic in the center",
                        "Create branches for subtopics",
                        "Connect related ideas visually",
                    ],
                    "explanation": "Helpful for big topics and overloaded brains.",
                },
                {
                    "name": "Spaced Repetition",
                    "process": [
                        "Review after 1 day",
                        "Then 3 days later",
                        "Then 1 week later",
                        "Then 1 month later",
                    ],
                    "explanation": "Helps information stay in long-term memory.",
                },
            ],
            "task_breakdown": [
                {
                    "name": "Chapter Breakdown",
                    "process": ["Chapter", "Topic", "Subtopic", "Questions"],
                    "explanation": "Makes big work feel smaller.",
                },
                {
                    "name": "3-Step Plan",
                    "process": [
                        "Pick the topic",
                        "Pick the first question",
                        "Start for 10 minutes",
                    ],
                    "explanation": "Good when starting feels hard.",
                },
            ],
            "motivation": [
                {"text": "Studying when it feels hard still counts as effort."},
                {"text": "Progress matters more than perfection."},
                {"text": "You do not have to understand everything today."},
            ],
            "productivity": [
                "Work in short focused sessions.",
                "Take real breaks between tasks.",
                "Write down one thing you finished today.",
                "Reward yourself for small wins.",
                "Study with friends",
                "Join online communities",
                "Use past papers.",
                "Revise mistakes more than correct answers.",
                "Teach the topic out loud.",
                "Set one timer and stop when it ends.",
                "Study the easiest part first if you are stuck.",
                "Use flashcards for quick recall.",
                "Keep a small error notebook.",
                "Break revision into short sessions instead of one long one.",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Talk to a trusted adult",
                "Reach out to a friend if stress feels too heavy",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
                "Take a step back and remember that your worth is not defined by your academic performance",
            ],
            "crisis_lines": [
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search by country",
                        "Choose a local mental health line",
                    ],
                    "explanation": "Good for finding region-specific help.",
                }
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": [
                        "Open the chat support option",
                        "Tell them you are overwhelmed with studies",
                    ],
                    "explanation": "Useful when you need to talk to someone safe.",
                }
            ],
            "urgent_steps": [
                "Stop studying for a few minutes",
                "Drink water",
                "Pick only one next task",
            ],
            "reassurance": [{"text": "One bad study day does not define you."}],
            "resources": [
                "[link=https://jedfoundation.org]JED Foundation[/link]",
                "[link=https://childmind.org]Child Mind Institute[/link]",
            ],
        },
    },
    "abuse_unsafe_environment": {
        "keywords": ["abuse", "unsafe", "violence", "fear at home", "scared"],
        "analysis": [
            "Potentially unsafe environment",
            "Safety-focused response recommended",
        ],
        "distractions": {
            "activities": [
                "Find a quiet, private space if you can and just breathe for a moment",
                "Write down your feelings privately — you do not have to show anyone",
                "Listen to calming music with headphones if that is available",
                "Focus on one small thing around you that feels okay right now",
                "Hold something familiar and grounding — a book, a blanket, an object",
                "Breathe slowly and count your breaths up to ten",
                "Step outside for a moment if that is safe to do",
                "Draw or write without a goal — just get the feeling out somewhere",
                "Think of one person who makes you feel safe, even if they are not here right now",
                "If it is safe, text someone you trust just to feel connected",
            ],
            "quotes": [
                {"text": "What is happening is not your fault."},
                {"text": "You deserve to feel safe."},
                {"text": "Reaching out is an act of strength, not weakness."},
                {"text": "Your safety matters more than anything else right now."},
                {"text": "You are not alone, even when it feels that way."},
                {"text": "You do not have to fix everything today. Just stay safe."},
                {"text": "People care about what happens to you."},
                {
                    "text": "This situation is not permanent, even when it feels like it is."
                },
                {"text": "You deserve kindness. Full stop."},
                {"text": "Getting help is not dramatic. It is necessary and right."},
                {"text": "You are allowed to put yourself first."},
                {
                    "text": "Surviving this takes real courage, even if it does not feel that way."
                },
                {"text": "Your feelings about what is happening are valid."},
                {"text": "One step toward safety is enough for right now."},
                {"text": "You matter. What happens to you matters."},
            ],
        },
        "support": {
            "reassurance": [
                {"text": "What is happening is not your fault."},
                {"text": "You deserve safety and support."},
            ],
            "resources": [
                "[link=https://childhelphotline.org]Child Helpline[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "grounding": [
                {
                    "name": "Find Safety",
                    "process": [
                        "Locate the nearest exit or safe space",
                        "Focus on one neutral object near you",
                        "Name it and describe it in your head",
                        "Breathe slowly",
                    ],
                    "explanation": "Anchors you to what is physically around you right now.",
                },
                {
                    "name": "5-4-3-2-1 Method",
                    "process": [
                        "Name 5 things you can see",
                        "4 things you can touch",
                        "3 things you hear",
                        "2 things you smell",
                        "1 thing you taste",
                    ],
                    "explanation": "Reconnects attention to the present moment.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cool water",
                        "Focus only on the temperature",
                        "Take 3 slow breaths",
                    ],
                    "explanation": "Interrupts spiraling stress thoughts.",
                },
                {
                    "name": "Chair Grounding",
                    "process": [
                        "Sit back fully in your chair",
                        "Feel your feet touching the floor",
                        "Relax your shoulders slowly",
                    ],
                    "explanation": "Brings awareness back into the body.",
                },
            ],
            "breathing": [
                {
                    "name": "Slow Breath",
                    "process": [
                        "Breathe in gently for 4",
                        "Hold for 2",
                        "Breathe out for 6",
                        "Repeat",
                    ],
                    "explanation": "Regulates your nervous system when you feel unsafe.",
                },
            ]
            + COMMON_BREATHING,
            "comfort": [
                {"text": "What is happening is not your fault."},
                {"text": "You deserve to feel safe."},
                {"text": "Reaching out for help is strength, not weakness."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Micro-Study",
                    "process": [
                        "Study only when safe",
                        "Use very small chunks",
                        "Stop if you feel unsafe",
                    ],
                    "explanation": "Safety comes first.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "Safety First",
                    "process": [
                        "Check if you are safe",
                        "Move to a safer place",
                        "Only then think about tasks",
                    ],
                    "explanation": "Do not force productivity in an unsafe place.",
                }
            ],
            "motivation": [{"text": "Your safety matters most."}],
            "productivity": [
                "Focus on staying safe",
                "Do not isolate if unsafe",
                "Keep your phone charged",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Reach out to a trusted adult",
                "Stay near safe people if possible",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
                "Reach out to other family members if they are safe and you feel comfortable doing so",
                "If you are in immediate danger, try to get to a public place or somewhere with other people around if you can do so safely",
                "Authorities can also be contacted if you are in danger and have no safe adults to reach out to",
            ],
            "crisis_lines": [
                {
                    "name": "Emergency services",
                    "process": [
                        "Use emergency services if you are in immediate danger"
                    ],
                    "explanation": "For urgent physical safety.",
                },
                {
                    "name": "Child Helpline India",
                    "process": ["Call 1098"],
                    "explanation": "24/7 support for children in distress in India.",
                },
                {
                    "name": "Local child protection helplines",
                    "process": ["Contact local child protection support"],
                    "explanation": "Useful when a teen is unsafe at home.",
                },
            ],
            "chat_support": [
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search your country",
                        "Choose chat support if available",
                    ],
                    "explanation": "A quick way to find verified help.",
                }
            ],
            "urgent_steps": [
                "Leave the unsafe space if you can do so safely",
                "Keep your phone charged",
                "Go where other people are",
            ],
            "reassurance": [{"text": "You deserve safety and support."}],
            "resources": [
                "[link=https://childhelphotline.org]Child Helpline[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
        },
    },
    "crisis_self_harm": {
        "keywords": [
            "suicide",
            "kill myself",
            "self harm",
            "hurt myself",
            "dont want to live",
        ],
        "analysis": ["High-risk emotional state", "Immediate support recommended"],
        "distractions": {
            "activities": [
                "Move to a different room — physical distance from the moment helps",
                "Sit near a window and just look outside for a few minutes",
                "Text or call someone you trust right now, even with a short message",
                "Put distance between yourself and anything harmful — that one step matters",
                "Hold something cold or textured and focus entirely on how it feels",
                "Breathe in slowly for four counts, out for six — repeat five times",
                "Write exactly what you are feeling right now, no filter needed",
                "Stay near other people if you can, even without talking",
                "Put on something familiar in the background — a show, a voice, anything",
                "Focus on getting through just the next ten minutes, nothing further than that",
            ],
            "quotes": [
                {"text": "You matter, even when it does not feel that way."},
                {"text": "This moment is not the whole story."},
                {"text": "Help exists and you deserve to receive it."},
                {"text": "You are still here. That counts for everything."},
                {"text": "Pain this heavy deserves support, not silence."},
                {"text": "You do not have to carry this alone."},
                {"text": "Asking for help is the bravest thing you can do right now."},
                {
                    "text": "This feeling will shift. It always does, even when it does not feel possible."
                },
                {"text": "You are worth the effort it takes to reach out."},
                {
                    "text": "Even one person knowing how you feel can change the weight of it."
                },
                {
                    "text": "You surviving today is enough. That is the whole goal right now."
                },
                {
                    "text": "What you are feeling is real. And real things can get support."
                },
                {"text": "There are people trained and ready to help right now."},
                {"text": "You deserve to still be here tomorrow."},
                {
                    "text": "One message, one call, one step — that is all that is needed right now."
                },
            ],
        },
        "support": {
            "reassurance": [
                {"text": "You deserve support right now."},
                {"text": "Please do not stay alone with these thoughts."},
                {"text": "There are people who want to help."},
            ],
            "resources": [
                "[link=https://findahelpline.com]Find A Helpline[/link]",
                "[link=https://988lifeline.org]988 Lifeline[/link]",
            ],
            "grounding": [
                {
                    "name": "Surroundings",
                    "process": [
                        "Look around you",
                        "Name what you can see",
                        "Stay present for the next minute",
                    ],
                    "explanation": "Pulls attention away from the spiral.",
                },
                {
                    "name": "5-4-3-2-1 Method",
                    "process": [
                        "Name 5 things you can see",
                        "4 things you can touch",
                        "3 things you hear",
                        "2 things you smell",
                        "1 thing you taste",
                    ],
                    "explanation": "Reconnects attention to the present moment.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cool water",
                        "Focus only on the temperature",
                        "Take 3 slow breaths",
                    ],
                    "explanation": "Interrupts spiraling stress thoughts.",
                },
                {
                    "name": "Chair Grounding",
                    "process": [
                        "Sit back fully in your chair",
                        "Feel your feet touching the floor",
                        "Relax your shoulders slowly",
                    ],
                    "explanation": "Brings awareness back into the body.",
                },
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "breathing": [
                {
                    "name": "Grounding Breath",
                    "process": [
                        "Breathe in for 4",
                        "Breathe out for 6",
                        "Repeat 10 times",
                        "Focus only on the count",
                    ],
                    "explanation": "Slows the crisis response and buys time between the urge and the action.",
                },
            ]
            + COMMON_BREATHING,
            "comfort": [
                {"text": "You matter, even when it does not feel that way."},
                {"text": "This moment is not the whole story."},
                {"text": "You deserve to still be here tomorrow."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Very Small Steps",
                    "process": [
                        "Pick one tiny task",
                        "Do only that",
                        "Stop and get support if needed",
                    ],
                    "explanation": "Do not push productivity during crisis.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "Next Safe Step",
                    "process": [
                        "Put distance from danger",
                        "Contact support",
                        "Stay with a safe person",
                    ],
                    "explanation": "Safety first, tasks later.",
                }
            ],
            "motivation": [{"text": "Getting through this moment is enough."}],
            "productivity": [
                "Do not focus on schoolwork right now",
                "Focus on staying safe",
                "Let someone know you need help",
                "Its not shameful to ask for help when you are struggling.",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Reach out to a trusted friend or adult immediately",
                "Tell someone how you are feeling, even if it is just through text",
                "If reaching out feels too hard, stay near people even without talking",
                "Journal your feelings if you cannot speak them yet",
                "Write a message to someone you care about, even if you do not send it",
                "If you have a pet, stay close to them — their presence can help",
                "Post in an online support community if that feels safer",
            ],
            "crisis_lines": [
                {
                    "name": "988 Suicide & Crisis Lifeline",
                    "process": [
                        "Call 988",
                        "Text 988",
                        "Use 988 chat on the official site",
                    ],
                    "explanation": "24/7 support for mental health and crisis needs.",
                },
                {
                    "name": "Crisis Text Line-India",
                    "process": ["Call 14416"],
                    "explanation": "24/7 support for mental health and crisis needs in India.",
                },
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Use the website to search by country",
                        "Pick call, chat, or text if available",
                    ],
                    "explanation": "Helps find local crisis support.",
                },
                {
                    "name": "Emergency services",
                    "process": ["Use emergency services if there is immediate danger"],
                    "explanation": "For urgent life-threatening situations.",
                },
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": [
                        "Open the chat support page",
                        "Share only what feels safe",
                        "Follow the counselor's guidance",
                    ],
                    "explanation": "Youth-focused chat support.",
                }
            ],
            "urgent_steps": [
                "Move away from dangerous objects",
                "Stay around other people if possible",
                "Focus only on getting through the next few minutes",
            ],
            "reassurance": [
                {"text": "You are not alone."},
                {"text": "Help is available right now."},
            ],
            "resources": [
                "[link=https://findahelpline.com]Find A Helpline[/link]",
                "[link=https://988lifeline.org]988 Lifeline[/link]",
                "[link=https://icallhelpline.org/about-the-reyou-chat-line/]iCALL ReYou Chat-line[/link]",
            ],
        },
    },
    "burnout_exhaustion": {
        "keywords": [
            "burnt out",
            "burnout",
            "exhausted",
            "tired all the time",
            "cant do this anymore",
            "drained",
            "fatigue",
            "tired",
            "tiring",
            "cant do this",
            "can't do this",
            "exhausting",
            "incredibly exhausting",
        ],
        "analysis": [
            "User may be emotionally and mentally exhausted",
            "Likely needs rest and reduced pressure",
            "May struggle with motivation and concentration",
        ],
        "distractions": {
            "activities": [
                "Listen to rain sounds",
                "Rest without guilt for 20 minutes",
                "Drink something warm slowly",
                "Watch low-energy comfort videos",
                "Sit near plants or sunlight",
            ],
            "memes": COMMON_MEMES,
            "jokes": [
                {
                    "text": "My energy left the building and forgot to sign the exit form. 🏃"
                },
                {"text": "I'm not tired, I'm just emotionally in airplane mode. ✈️"},
                {"text": "My motivation needs a nap, a snack, and a support group. 💤"},
                {
                    "text": "I wanted to do everything, but my battery said absolutely not. 🔋"
                },
                {
                    "text": "I made a to-do list. Then I took a nap to recover from making it. 📋"
                },
            ],
            "quotes": [
                {"text": "Rest is not laziness."},
                {"text": "Burnout is not weakness."},
                {"text": "You are a person, not a machine."},
            ],
        },
        "support": {
            "comfort": [
                {"text": "You are allowed to slow down."},
                {"text": "Constant productivity is not human."},
                {"text": "Even phones need charging."},
            ],
            "resources": [
                "[link=https://jedfoundation.org]JED Foundation[/link]",
                "[link=https://www.nimh.nih.gov]NIMH[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "grounding": [
                {
                    "name": "Body Scan",
                    "process": [
                        "Notice your forehead",
                        "Relax your jaw",
                        "Relax your shoulders",
                        "Relax your hands",
                    ],
                    "explanation": "Releases physical tension from exhaustion.",
                },
                {
                    "name": "Blanket Reset",
                    "process": [
                        "Wrap yourself in a blanket",
                        "Focus on warmth and pressure",
                        "Take slow breaths",
                    ],
                    "explanation": "Provides a sense of safety and calm.",
                },
                {
                    "name": "Feet Grounding",
                    "process": [
                        "Place both feet on the floor",
                        "Press them gently downward",
                        "Notice the support beneath you",
                    ],
                    "explanation": "Helps reconnect with the present.",
                },
                {
                    "name": "Light Observation",
                    "process": [
                        "Look at nearby light sources",
                        "Notice shadows and brightness",
                        "Breathe slowly",
                    ],
                    "explanation": "Redirects attention from exhaustion loops.",
                },
                {
                    "name": "Temperature Focus",
                    "process": [
                        "Hold a cold or warm object",
                        "Focus on the sensation",
                        "Describe it mentally",
                    ],
                    "explanation": "Brings awareness back to the body.",
                },
            ],
            "breathing": [
                {
                    "name": "Slow Breath",
                    "process": [
                        "Breathe in for 4",
                        "Breathe out for 8",
                        "Repeat 6 times",
                    ],
                    "explanation": "The long exhale activates rest mode in your body.",
                },
            ]
            + COMMON_BREATHING,
            "reassurance": [
                {"text": "Rest is not laziness. It is maintenance."},
                {"text": "You are allowed to stop before you collapse."},
                {"text": "Doing less right now is not failure."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Pomodoro",
                    "process": [
                        "Study for 25 minutes",
                        "Take a 5 minute break",
                        "Repeat",
                    ],
                    "explanation": "Short sessions are easier when you are exhausted.",
                },
                {
                    "name": "Low-energy Revision",
                    "process": [
                        "Read lightly",
                        "Review only key points",
                        "Stop before you crash",
                    ],
                    "explanation": "Lets you keep going without draining yourself.",
                },
                {
                    "name": "Flashcards",
                    "process": [
                        "Review quick questions",
                        "Test yourself",
                        "Stop after a short set",
                    ],
                    "explanation": "Good when full chapters feel too heavy.",
                },
            ],
            "task_breakdown": [
                {
                    "name": "Only 3 Tasks",
                    "process": [
                        "Pick only 3 important tasks",
                        "Reduce workload temporarily",
                        "Focus on completion, not perfection",
                    ],
                    "explanation": "Better for low-energy days.",
                }
            ],
            "motivation": [
                {"text": "Small progress still counts."},
                {"text": "You do not need to do everything today."},
            ],
            "productivity": [
                "Keep the task list short",
                "Use one timer",
                "Work in a quiet place if possible",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Text a trusted person",
                "Call a friend",
                "Tell an adult you trust you need help",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "FindAHelpline",
                    "process": ["Search by country", "Choose a local support line"],
                    "explanation": "Useful if exhaustion turns into a crisis.",
                }
            ],
            "chat_support": [
                {
                    "name": "The Live Love Laugh Helplines",
                    "process": ["Visit the helpline page", "Choose a support option"],
                    "explanation": "Can help when you need to talk.",
                }
            ],
            "urgent_steps": [
                "Stop and rest",
                "Drink water",
                "Ask for help with one thing",
            ],
            "reassurance": [{"text": "Rest is allowed."}],
            "resources": [
                "[link=https://jedfoundation.org]JED Foundation[/link]",
                "[link=https://www.nimh.nih.gov]NIMH[/link]",
            ],
        },
    },
    "grief_loss": {
        "keywords": ["grief", "loss", "miss them", "death", "mourning", "gone forever"],
        "analysis": [
            "User may be grieving emotionally",
            "Needs compassion and patience",
        ],
        "distractions": {
            "activities": [
                "Write down a memory of them — something small and specific",
                "Look at old photos only if it feels okay right now, not as a task",
                "Sit somewhere quiet and let yourself just be without fixing anything",
                "Make something warm to drink and hold the mug with both hands",
                "Draw or doodle without any goal, just let your hand move",
                "Put on music that feels gentle, not music that demands anything from you",
                "Write them a letter you do not have to send",
                "Step outside for a few minutes and just breathe",
                "Wrap yourself in something soft and rest without guilt",
                "Look at something in nature — a plant, the sky, anything growing",
            ],
            "quotes": [
                {"text": "Grief is love with nowhere to go. It is still love."},
                {"text": "You do not have to rush through this."},
                {"text": "There is no wrong way to grieve."},
                {"text": "Missing someone deeply means they mattered. They did."},
                {"text": "You are allowed to have good moments even in hard seasons."},
                {
                    "text": "Healing is not forgetting. It is learning to carry it differently."
                },
                {"text": "Rest is not giving up. It is surviving, which is enough."},
                {"text": "You do not need to explain your grief to anyone."},
                {"text": "Some days will be heavier than others. That is normal."},
                {"text": "You are still here. That matters more than you know."},
                {
                    "text": "Crying is not weakness. It is grief doing what it needs to do."
                },
                {"text": "You are allowed to miss them and still move gently forward."},
                {"text": "There is no deadline on feeling this."},
                {"text": "Even on hard days, you are not alone in having them."},
                {"text": "Small steps through grief still count as steps."},
            ],
        },
        "support": {
            "comfort": [
                {"text": "Grief has no proper timeline."},
                {"text": "Missing someone deeply is human."},
                {"text": "You do not need to move on instantly."},
                {"text": "Write memories down"},
                {"text": "Talk about them with someone trusted"},
                {"text": "Cry if needed"},
                {"text": "Rest more than usual"},
                {"text": "Remind yourself that healing is not linear"},
                {"text": "Let yourself live the happy and sad moments without guilt"},
            ],
            "reassurance": [
                {"text": "There is no deadline on feeling this."},
                {"text": "You are allowed to have good moments and still be grieving."},
                {"text": "Missing them does not mean you are not healing."},
            ],
            "grounding": [
                {
                    "name": "Memory Anchor",
                    "process": [
                        "Think of one good memory",
                        "Name one detail from it",
                        "Breathe slowly while holding it",
                    ],
                    "explanation": "Connects you gently to something real and warm.",
                },
                {
                    "name": "Shoulder Reset",
                    "process": [
                        "Inhale while lifting shoulders",
                        "Exhale while relaxing them",
                        "Repeat 5 times",
                    ],
                    "explanation": "Releases tension from stress.",
                },
                {
                    "name": "Slow Exhale",
                    "process": [
                        "Breathe in normally",
                        "Exhale slower than your inhale",
                        "Repeat gently",
                    ],
                    "explanation": "Signals safety to the nervous system.",
                },
                {
                    "name": "Counted Breathing",
                    "process": [
                        "Count each inhale",
                        "Count each exhale",
                        "Restart if distracted",
                    ],
                    "explanation": "Improves focus and calm.",
                },
            ],
            "breathing": COMMON_BREATHING,
            "resources": [
                "[link=https://childmind.org]Child Mind Institute[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Gentle Study",
                    "process": [
                        "Do one light task",
                        "Take breaks often",
                        "Stop if it becomes too much",
                    ],
                    "explanation": "Grief can make concentration harder.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "Minimum Day",
                    "process": ["Pick the smallest task", "Do only that", "Rest after"],
                    "explanation": "Enough for hard days.",
                }
            ],
            "motivation": [{"text": "You are allowed to move gently."}],
            "productivity": [
                "Keep expectations low",
                "Use a timer if helpful",
                "Rest first if needed",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Talk to someone you trust",
                "Do not stay alone with overwhelming grief",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search by country",
                        "Choose the best available support",
                    ],
                    "explanation": "Helps find local help fast.",
                }
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": [
                        "Open chat support",
                        "Share as much or as little as you want",
                    ],
                    "explanation": "Good when talking feels hard.",
                }
            ],
            "urgent_steps": [
                "Sit near someone safe",
                "Drink water",
                "Breathe slowly for a minute",
            ],
            "reassurance": [{"text": "You do not have to handle this alone."}],
            "resources": [
                "[link=https://childmind.org]Child Mind Institute[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
        },
    },
    "self_esteem_body_image": {
        "keywords": [
            "ugly",
            "fat",
            "skinny",
            "insecure",
            "my body",
            "features",
            "confidence",
            "self esteem",
            "self-esteem",
            "body image",
            "body shame",
            "hate my body",
            "hate myself",
            "compare myself",
            "not good enough",
            "embarrassed",
            "looks",
            "look",
            "appearance",
            "acne",
            "my face",
        ],
        "analysis": [
            "User may be struggling with self-worth or body image.",
            "Teen-friendly reassurance and self-kindness may help.",
        ],
        "distractions": {
            "jokes": [
                {
                    "text": "My inner critic writes terrible reviews. One star, would not recommend. 📝"
                },
                {
                    "text": "I told my brain to be nicer. It said it would take it under advisement. 🧠"
                },
                {
                    "text": "The voice in my head has opinions. Most of them are wrong. 🙃"
                },
                {
                    "text": "My reflection and I have very different opinions about today. 🪞"
                },
                {
                    "text": "I tried to hype myself up. My confidence asked for more evidence. 📊"
                },
            ],
            "quotes": [
                {"text": "Your body is not a trend."},
                {"text": "You are more than how you look today."},
                {"text": "Comparison is not a fair judge."},
                {"text": "Confidence can grow slowly."},
            ],
            "activities": [
                "Unfollow accounts that make you feel worse",
                "Write 3 things your body helps you do",
                "Pick one outfit that feels comfortable",
                "Step away from mirrors for a bit",
                "Listen to something grounding",
                "Ask people you trust what they like about you that has nothing to do with looks",
                "Focus on your talents and qualities instead of appearance",
            ],
        },
        "support": {
            "comfort": [
                {"text": "You do not need to look perfect to be worthy."},
                {"text": "Teen bodies change, and that is normal."},
                {"text": "You are allowed to be a work in progress."},
                {"text": "Try kinder self-talk."},
                {"text": "Notice what your body can do, not just how it looks."},
                {"text": "Take breaks from social media when comparison gets loud."},
                {"text": "Talk to someone you trust if this feels heavy."},
            ],
            "resources": [
                "[link=https://kidshealth.org/en/teens/body-image.html]Body Image - KidsHealth[/link]",
                "[link=https://www.mentalhealth.org.uk/]Mental Health Foundation[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "grounding": [
                {
                    "name": "What My Body Can Do",
                    "process": [
                        "Name one thing your body did today",
                        "Write it down or say it out loud",
                        "Thank it — even something as small as breathing",
                    ],
                    "explanation": "Shifts focus from how the body looks to what it actually does for you.",
                },
                {
                    "name": "5-4-3-2-1 Method",
                    "process": [
                        "Name 5 things you can see",
                        "4 things you can touch",
                        "3 things you hear",
                        "2 things you smell",
                        "1 thing you taste",
                    ],
                    "explanation": "Reconnects attention to the present moment.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cool water",
                        "Focus only on the temperature",
                        "Take 3 slow breaths",
                    ],
                    "explanation": "Interrupts spiraling stress thoughts.",
                },
                {
                    "name": "Chair Grounding",
                    "process": [
                        "Sit back fully in your chair",
                        "Feel your feet touching the floor",
                        "Relax your shoulders slowly",
                    ],
                    "explanation": "Brings awareness back into the body.",
                },
            ],
            "breathing": [
                {
                    "name": "Gentle Breath",
                    "process": [
                        "Breathe in softly for 4",
                        "Hold for 2",
                        "Breathe out for 6",
                    ],
                    "explanation": "Simple and calming when critical thoughts feel loud.",
                },
            ]
            + COMMON_BREATHING,
            "reassurance": [
                {"text": "You are not your appearance. You are everything else too."},
                {
                    "text": "The standards you are measuring yourself against were invented to sell things."
                },
                {"text": "Your worth is not a reflection of how you look today."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Gentle Pomodoro",
                    "process": [
                        "Study for 20 to 25 minutes",
                        "Take a break",
                        "Repeat if you still have energy",
                    ],
                    "explanation": "Keeps pressure lower.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "Tiny First Step",
                    "process": [
                        "Choose one easy task",
                        "Start with that",
                        "Stop if your mind feels overloaded",
                    ],
                    "explanation": "Useful when self-esteem is low.",
                }
            ],
            "motivation": [{"text": "Your worth is not measured by appearance."}],
            "productivity": [
                "Focus on one task",
                "Avoid comparison breaks",
                "Take a short reset after studying",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Talk to someone you trust",
                "Reach out if self-image thoughts are getting overwhelming",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "FindAHelpline",
                    "process": ["Search by country", "Pick a support option"],
                    "explanation": "Helps you find support quickly.",
                }
            ],
            "chat_support": [
                {
                    "name": "The Live Love Laugh Helplines",
                    "process": ["Visit the support page", "Choose an available option"],
                    "explanation": "Can help with emotional support.",
                }
            ],
            "urgent_steps": [
                "Step away from comparison triggers",
                "Breathe slowly",
                "Tell someone how you feel",
            ],
            "reassurance": [{"text": "You are enough as you are."}],
            "resources": [
                "[link=https://kidshealth.org/en/teens/body-image.html]Body Image - KidsHealth[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
        },
    },
    "family_relationship_issues": {
        "keywords": [
            "family",
            "parents",
            "mom",
            "dad",
            "sister",
            "brother",
            "fight",
            "fighting",
            "argument",
            "arguments",
            "breakup",
            "home",
            "relationship",
            "relationship issues",
            "friend drama",
            "friends",
            "betrayed",
            "ignored by family",
            "home tension",
        ],
        "analysis": [
            "User may be dealing with conflict at home or in relationships.",
            "They may need validation, calm, and practical communication support.",
        ],
        "distractions": {
            "jokes": [
                {
                    "text": "Family group chats: where every notification is a surprise. 📱"
                },
                {"text": "I have the patience of a saint. A very tired saint. 😮‍💨"},
                {
                    "text": "Home is where the wifi is. And also the complicated feelings. 🏠"
                },
                {
                    "text": "Tried to set a boundary. My family called it a suggestion. 🚧"
                },
                {"text": "I love my people. From a comfortable emotional distance. 💙"},
            ],
            "quotes": [
                {"text": "Tension does not define your whole life."},
                {"text": "You deserve relationships that feel safe."},
                {"text": "Not every fight needs a reply right away."},
            ],
            "activities": [
                "Take a short break before replying",
                "Write what you want to say first",
                "Talk to a trusted person outside the conflict",
                "Listen to music before sending messages",
                "Communication is key, but it is okay to wait until you feel calmer to have important conversations.",
            ],
        },
        "support": {
            "comfort": [
                {"text": "Conflict is hard, especially when it is close to home."},
                {"text": "You are allowed to need space."},
                {"text": "You can care about people and still set boundaries."},
                {"text": "Use calm words when you can."},
                {"text": "Focus on one issue at a time."},
                {"text": "Do not text while extremely upset."},
                {"text": "If it is safe, explain how you feel using 'I' statements."},
            ],
            "resources": [
                "[link=https://www.7cups.com]7 Cups[/link]",
                "[link=https://childmind.org]Child Mind Institute[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "grounding": [
                {
                    "name": "Safe Space Visualisation",
                    "process": [
                        "Close your eyes",
                        "Picture somewhere you feel safe",
                        "Notice the details — sounds, light, feeling",
                        "Stay there for 2 minutes",
                    ],
                    "explanation": "Creates mental distance from a tense environment.",
                },
                {
                    "name": "5-4-3-2-1 Method",
                    "process": [
                        "Name 5 things you can see",
                        "4 things you can touch",
                        "3 things you hear",
                        "2 things you smell",
                        "1 thing you taste",
                    ],
                    "explanation": "Reconnects attention to the present moment.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cool water",
                        "Focus only on the temperature",
                        "Take 3 slow breaths",
                    ],
                    "explanation": "Interrupts spiraling stress thoughts.",
                },
                {
                    "name": "Chair Grounding",
                    "process": [
                        "Sit back fully in your chair",
                        "Feel your feet touching the floor",
                        "Relax your shoulders slowly",
                    ],
                    "explanation": "Brings awareness back into the body.",
                },
            ],
            "breathing": COMMON_BREATHING,
            "reassurance": [
                {
                    "text": "Difficult relationships are not proof that you are unlovable."
                },
                {"text": "You are allowed to have boundaries even with family."},
                {
                    "text": "How people treat you says more about them than about your worth."
                },
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Short Reset Study",
                    "process": [
                        "Calm down first",
                        "Study for a short block",
                        "Take a break",
                    ],
                    "explanation": "Helps when emotional stress is high.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "One Problem at a Time",
                    "process": ["Pick one issue", "Write it down", "Address only that"],
                    "explanation": "Keeps things from becoming a pile-up.",
                }
            ],
            "motivation": [{"text": "You can be kind and still have boundaries."}],
            "productivity": [
                "Do not reply while upset",
                "Take space if needed",
                "Keep your to-do list short",
                "The right person will understand if you need space to process.",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Talk to a trusted adult",
                "Reach out to a friend you trust",
                "Contact someone safe",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search by country",
                        "Choose a family or mental health support line",
                    ],
                    "explanation": "Useful for conflict and stress support.",
                }
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": [
                        "Open chat support",
                        "Explain the conflict if you want to",
                    ],
                    "explanation": "Helpful if talking feels easier in chat.",
                }
            ],
            "urgent_steps": [
                "Leave the conversation if it is getting too heated",
                "Go to a safer room or nearby adult",
                "Put your phone down for a minute",
            ],
            "reassurance": [{"text": "You do not have to solve everything right now."}],
            "resources": [
                "[link=https://www.7cups.com]7 Cups[/link]",
                "[link=https://findahelpline.com]Find A Helpline[/link]",
            ],
        },
    },
    "unknown_help": {
        "score_mode": True,
        "keywords": [],
        "analysis": [
            "User is not clearly labeling the emotion.",
            "Use score-based classification first, then fall back to general support.",
        ],
        "distractions": {
            "quotes": [
                {"text": "You do not need the perfect word to deserve help."},
                {"text": "It is okay to feel mixed up."},
                {"text": "We can start simple."},
            ],
            "activities": [
                "Take one slow breath",
                "Drink some water",
                "Read one calming line",
                "Pick the closest feeling from a list",
            ],
            "jokes": [
                {
                    "text": "My brain has too many tabs open and one of them is playing music I cannot find. 🎵"
                },
                {"text": "Current mood: loading. Please wait. ⏳"},
                {
                    "text": "I have feelings but the signal to process them is very weak right now. 📶"
                },
                {
                    "text": "I could not name this feeling if you gave me a dictionary. 📖"
                },
                {"text": "Somewhere between fine and absolutely not fine. 🌊"},
            ],
        },
        "support": {
            "comfort": [
                {"text": "You do not have to explain everything perfectly."},
                {"text": "It is okay if the feeling is hard to name."},
                {"text": "You can still get help even if you are unsure."},
                {
                    "text": "Tell me if it feels more like stress, sadness, anger, fear, loneliness, or exhaustion."
                },
                {"text": "We can narrow it down together."},
                {"text": "You can also just say what happened."},
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
            "grounding": [
                {
                    "name": "5-4-3-2-1",
                    "process": [
                        "5 things you see",
                        "4 things you can touch",
                        "3 things you hear",
                        "2 things you smell",
                        "1 thing you taste",
                    ],
                    "explanation": "When you do not know what you feel, start with what is around you.",
                },
                {
                    "name": "Cold Water Reset",
                    "process": [
                        "Wash your face with cool water",
                        "Focus only on the temperature",
                        "Take 3 slow breaths",
                    ],
                    "explanation": "Interrupts spiraling stress thoughts.",
                },
                {
                    "name": "Chair Grounding",
                    "process": [
                        "Sit back fully in your chair",
                        "Feel your feet touching the floor",
                        "Relax your shoulders slowly",
                    ],
                    "explanation": "Brings awareness back into the body.",
                },
            ],
            "breathing": [
                {
                    "name": "Just Breathe",
                    "process": [
                        "Breathe in for 4",
                        "Breathe out for 4",
                        "Repeat until something shifts",
                    ],
                    "explanation": "You do not need to know what is wrong to do this.",
                },
            ]
            + COMMON_BREATHING,
            "resources": [
                "[link=https://findahelpline.com]Find A Helpline[/link]",
                "[link=https://childmind.org]Child Mind Institute[/link]",
            ],
            "reassurance": [
                {
                    "text": "Not knowing what you feel is still a valid reason to reach out."
                },
                {"text": "You do not have to name it to deserve support."},
                {"text": "Something brought you here. That something matters."},
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Gentle Start",
                    "process": [
                        "Pick one tiny task",
                        "Start for 5 to 10 minutes",
                        "Stop or continue based on energy",
                    ],
                    "explanation": "Useful when you are unsure what you need.",
                }
            ],
            "task_breakdown": [
                {
                    "name": "Name the Feeling",
                    "process": [
                        "Pause",
                        "Notice what is strongest",
                        "Choose the closest category",
                    ],
                    "explanation": "Helps sort confusion into something manageable.",
                }
            ],
            "motivation": [{"text": "Not knowing is okay."}],
            "productivity": [
                "Start tiny",
                "Do not pressure yourself",
                "Ask for support early",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Text or call a trusted person",
                "Tell an adult if you feel unsafe",
                "Journal your feelings if reaching out feels too hard",
                "Write a message to someone you care about, even if you do not send it",
                "Post in an online support community if that feels safer",
                "Animals can also be a source of comfort if you have a pet or access to one",
            ],
            "crisis_lines": [
                {
                    "name": "FindAHelpline",
                    "process": [
                        "Search by country",
                        "Choose the most relevant support",
                    ],
                    "explanation": "A good first place if you are unsure where to turn.",
                }
            ],
            "chat_support": [
                {
                    "name": "iCALL ReYou Chat-line",
                    "process": ["Open the chat line", "Share what you can"],
                    "explanation": "Good when it is hard to explain feelings.",
                }
            ],
            "urgent_steps": [
                "Take one breath",
                "Move near a safe person",
                "Stay with the next small step",
            ],
            "reassurance": [
                {"text": "You still deserve help even if you are unsure what you feel."}
            ],
            "resources": [
                "[link=https://findahelpline.com]Find A Helpline[/link]",
                "[link=https://icallhelpline.org/about-the-reyou-chat-line/]iCALL ReYou Chat-line[/link]",
            ],
        },
    },
    "happy_cheerful": {
        "keywords": [
            "happy",
            "excited",
            "cheerful",
            "great",
            "awesome",
            "yay",
            "yayayay",
            "fun",
            "smiling",
            "laughing",
            "joy",
            "content",
            "peaceful",
            "proud",
            "motivated",
            "energetic",
            "vibing",
            "glad",
            "fantastic",
            "amazing",
            "so happy",
        ],
        "analysis": [
            "User seems emotionally positive",
            "Possible stable or uplifted mood",
            "Good moment to encourage healthy habits and reflection",
        ],
        "distractions": {
            "activities": [
                "Make a playlist with songs that match your current vibe.",
                "Take pictures of small things that made today feel nice.",
                "Send someone a random wholesome message.",
                "Dance badly in your room for absolutely no reason.",
                "Write down 3 things you liked about today.",
                "Watch funny videos or wholesome animal clips.",
                "Try a new hobby or random creative idea just because you can.",
                "Go outside for a bit and enjoy the atmosphere.",
            ],
            "memes": COMMON_MEMES,
            "jokes": [
                {
                    "text": "Why are frogs always so happy? Because they eat whatever bugs them. 🐸"
                },
                {
                    "text": "I told my happiness to calm down. It threw confetti at me. 🎉"
                },
                {
                    "text": "Why did the music note feel amazing? Because it was in a good key. 🎵"
                },
                {
                    "text": "My motivation actually showed up today. I almost didn't recognize it. 😭"
                },
                {
                    "text": "I tried being serious today but my goofy energy said absolutely not. 🤡"
                },
                {"text": "Today's vibe: accidentally becoming the main character. ✨"},
            ],
            "quotes": [
                {"text": "You are allowed to enjoy good moments without guilt."},
                {"text": "Happiness does not need to be earned every second."},
                {"text": "Small joyful moments still matter."},
                {"text": "A peaceful day is still a meaningful day."},
                {"text": "You deserve moments that feel light and easy."},
                {"text": "Good days are worth remembering too."},
            ],
        },
        "support": {
            "comfort": [
                {"text": "It is nice to see you having a better moment. 🙂"},
                {"text": "You deserve calm and happiness too."},
                {"text": "Enjoying life is not wasting time."},
                {"text": "Hold onto the little good moments when they appear."},
            ],
            "resources": [
                "[link=https://www.actionforhappiness.org]Action For Happiness[/link]",
                "[link=https://greatergood.berkeley.edu]Greater Good Magazine[/link]",
            ],
            "hotlines": [
                "[link=https://findahelpline.com]Find A Helpline (Global)[/link]",
                "[link=https://www.thelivelovelaughfoundation.org/find-help/helplines]iCall India[/link]",
            ],
        },
        "focus": {
            "study_methods": [
                {
                    "name": "Momentum Study",
                    "process": [
                        "Start with the easiest task",
                        "Build confidence slowly",
                        "Use your good mood as energy",
                    ],
                    "explanation": "Positive moods can help productivity when used gently.",
                },
                {
                    "name": "Reward Method",
                    "process": [
                        "Finish one task",
                        "Reward yourself with something small",
                        "Repeat",
                    ],
                    "explanation": "Makes studying feel less draining.",
                },
            ],
            "task_breakdown": [
                {
                    "name": "Energy Mapping",
                    "process": [
                        "List tasks",
                        "Do high-energy tasks first",
                        "Save lighter tasks for later",
                    ],
                    "explanation": "Helps use motivation while it lasts.",
                }
            ],
            "motivation": [
                {"text": "Good moods can still coexist with imperfect days."},
                {"text": "You are doing better than you think."},
                {"text": "Celebrate small wins too."},
                {
                    "text": "You do not need to be productive every second to deserve happiness."
                },
            ],
            "productivity": [
                "Use your current energy to start something small.",
                "Do one task you have been avoiding.",
                "Keep water nearby and take breaks.",
                "Do not overload yourself just because you feel good today.",
            ],
        },
        "emergency": {
            "trusted_contact": [
                "Share your happiness with someone you trust",
                "Send a random wholesome text to a friend",
                "Take screenshots or notes of moments you want to remember",
            ],
            "reassurance": [
                {"text": "You are allowed to enjoy this moment."},
                {"text": "Good days matter too."},
                {"text": "You deserve peace and joy."},
            ],
            "resources": [
                "[link=https://www.actionforhappiness.org]Action For Happiness[/link]",
            ],
        },
    },
}
