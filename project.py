from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich import box
from rich.rule import Rule
from rich.markup import escape as rich_escape

# Rich library is used to create visually appealing console outputs and enhance the user experience.

import re

# Re is used to detect expressions in strings/words

from difflib import get_close_matches

# Difflib compares and helps to generate best matches in this program

import sys

# sys is used for direct stdout writes in the breathing animation countdown

import pickle

# pickle serializes and deserializes JournalEntry objects for local binary storage

import calendar

# To display a calendar for the user and to handle date-related operations for journal entries.

import datetime

# datetime captures current date and time when creating new journal entries

import os

# os handles file system operations: creating the data folder, clearing the screen,replacing files

import cowsay

# ASCII art library to add some lighthearted fun to the app and make it more engaging for users.

import random

# random selects cowsay characters and distraction items to keep content varied

import time

# time adds delays in animations to create smooth loading and breathing effects

from Emotional_Data import EMOTIONS

# EMOTIONS dictionary — all keyword lists, support content, and resources per emotion


def clear_screen():
    """Clears the console screen for better readability and cleaner UI"""
    os.system("cls" if os.name == "nt" else "clear")


# console instance used for all Rich-formatted output throughout the app(global)
console = Console()

# Maps internal snake_case emotion keys to clean single words shown to the user
EMOTION_DISPLAY = {
    "stress_overwhelm": "Stressed",
    "loneliness_isolation": "Lonely",
    "sadness_hopelessness": "Sad",
    "anxiety_panic": "Anxious",
    "anger_frustration": "Angry",
    "grief_loss": "Grieving",
    "academic_pressure": "Academic",
    "burnout_exhaustion": "Burnout",
    "self_esteem_body_image": "Self-esteem",
    "family_relationship_issues": "Relationship",
    "abuse_unsafe_environment": "Unsafe",
    "crisis_self_harm": "Crisis",
    "unknown_help": "Unknown",
    "happy_cheerful": "Happy",
}


def display_emotion(key):
    """Returns a user-friendly label for an internal emotion key. Falls back to title-cased key if unmapped."""
    return EMOTION_DISPLAY.get(key, key.replace("_", " ").title())


# Cowsay animals list for random selection
COWS = [
    cowsay.cow,
    cowsay.trex,
    cowsay.dragon,
    cowsay.tux,
    cowsay.kitty,
    cowsay.daemon,
    cowsay.fox,
    cowsay.ghostbusters,
    cowsay.milk,
    cowsay.stegosaurus,
]


def breathing_animation():
    """Displays a breathing animation with a countdown for each step."""
    steps = [("Breathe in...", 4), ("Hold...", 4), ("Breathe out...", 4)]

    for cycles in range(3):

        for text, seconds in steps:

            for i in range(seconds, 0, -1):  # Counts down second by second

                sys.stdout.write(f"\r{text} {i} ")

                sys.stdout.flush()  # Ensures the output is printed immediately

                time.sleep(1)  # To add delay of 1 second between each count

    print()


# Journal Class to represent each journal entry and handle emotion analysis and display of items based on emotion and mode
class JournalEntry:
    def __init__(self, id, title, date, time, mood, emotion, content):
        """Initializes a JournalEntry object with the given parameters."""
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.mood = mood
        self.emotion = emotion
        self.content = content

    @staticmethod  # Static method to analyze the emotion of the journal entry content based on keywords defined in the EMOTIONS dictionary
    def emotion_analysis(text):
        """Using users journal entry/input text to determine the emotion they are feeling and supplying guidance accordingly."""
        text = text.lower()
        scores = {}  # To find the best matching emotion
        for emotion_name, emotion_data in EMOTIONS.items():
            scores[emotion_name] = 0  # Initializing scores for each emotion to 0
            for keyword in emotion_data[
                "keywords"
            ]:  # Iteration through the keywords for each emotion and checking if they are present in the text to calculate the score for each emotion
                pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

                if re.search(pattern, text):
                    if len(keyword.split()) > 1:
                        scores[emotion_name] += 2
                    else:
                        scores[
                            emotion_name
                        ] += 1  # Incrementing the score for the emotion if a keyword is found in the text but prefer phrases so that words like press in depressed are given less improtant than the word depressed
        highest = max(scores.values())

        matches = [emotion for emotion, score in scores.items() if score == highest]

        best_match = matches[0]
        if scores[best_match] == 0:
            return "unknown_help"  # Generic category for when no specific emotion can be determined from the text
        return best_match

    @staticmethod
    def show_items(title, items):
        """Displays items in a formatted panel based on the type of item (string, quote, technique)."""
        if not items:
            console.print("[bold red]No data available.[/bold red]")
            return

        for item in items:

            # SIMPLE STRING
            if isinstance(
                item, str
            ):  # To display a simple string item in a formatted panel with the title as the category of the item

                panel = Panel(
                    Text.from_markup(item),
                    title=f"[bold cyan]{title}[/bold cyan]",
                    style="bold blue",
                    box=box.ROUNDED,
                    width=90,
                )

                console.print(panel)

            # QUOTES/JOKES
            elif (
                isinstance(item, dict) and "text" in item
            ):  # To display the text of the quote or joke in a formatted panel with the title as the quote/joke category

                panel = Panel(
                    item["text"],
                    title=f"[bold cyan]{title}[/bold cyan]",
                    style="bold magenta",
                    box=box.ROUNDED,
                    width=90,
                )

                console.print(panel)

            # TECHNIQUES
            elif (
                isinstance(item, dict) and "name" in item
            ):  # To display the name, process, and explanation of the technique in a formatted panel

                process = ("\n" + " " * 56).join(
                    [f"• {step}" for step in item["process"]]
                )
                if item["name"] == "Box Breathing":

                    breathing_animation()

                body = f"""
                                    [bold yellow]{item['name']}[/bold yellow]

                                                        {process}

                                    [italic cyan]{item['explanation']}[/italic cyan]
    """

                panel = Panel(  # To display a menu of steps for the technique along with its name and explanation.
                    body,
                    title=f"[bold green]{title}[/bold green]",
                    style="bold blue",
                    box=box.ROUNDED,
                    width=90,
                )

                console.print(panel)

    @staticmethod
    def show_emotion_mode(emotion_key, mode):
        """Retrieves and displays items based on the user's emotion and the selected mode"""

        emotion_data = EMOTIONS.get(
            emotion_key
        )  # To retrieve the data for the specified emotion key from the EMOTIONS dictionary

        if not emotion_data:
            console.print("[bold red]Emotion not found.[/bold red]")
            return

        mode_data = emotion_data.get(
            mode
        )  # To retrieve the data for the specified mode from the emotion data
        #
        if not mode_data:
            console.print("[bold red]Mode not found.[/bold red]")
            return

        for section_name, section_items in mode_data.items():

            pretty_name = section_name.replace(
                "_", " "
            ).title()  # To format the section name by replacing underscores with spaces and capitalizing each word for better readability

            JournalEntry.show_items(
                pretty_name, section_items
            )  # To display items in the section using the show_items method


def random_cowsay(text):
    """Displays the given text using a randomly selected cowsay character. For added entertainment and to lighten the mood of the user."""
    animal = random.choice(COWS)

    animal(text)


def main():
    """Main function to display the main menu and handle user choices for navigating through the app."""
    choice = 1
    if not os.path.exists(
        "data"
    ):  # checking if the data directory exists to store journal entries, if not it creates one
        os.makedirs("data")
    # Dots animation for loading effect
    dots = ""
    for i in range(3):
    
        dots += "."  # To get the effect of increasing dots
    
        console.clear()
    
        console.print(
            Align.center(f"[bold cyan]{dots}[/bold cyan]")
        )  # To print the dots in the center of the console
    
        time.sleep(
            0.5
        )  # To give the illusion of animation by adding a delay between each print
    while True:
        menu = """
        1. Journal

        2. Calendar

        3. Support

        4. Recommendations

        5. Exit
        """
        #
        panel = Panel(
            Align.center(menu),
            title="[bold cyan]LIGHTHOUSE[/bold cyan]",
            style="bold blue",
            box=box.ASCII,  # To get a dotted border look
            padding=(1, 4),
            subtitle="[bold cyan]DISCLAIMER:[/bold cyan]",
            width=50,
        )
        console.print(Rule("[blue]MAIN MENU[/blue]"))
        console.print("\n")
        console.print(Align.center(panel))
        console.print("\n")
        console.print(
            Align.center(
                " " * 17
                + "[bold blue] This application is NOT a replacement for professional mental health care.\n\n It is a support tool designed to encourage healthy coping mechanisms and connection to trusted resources.[/bold blue]"
            )
        )  #
        print()
        choice = console.input(
            Align.center("[bold green]Enter your choice (1-5): [/bold green]")
        )
        if (
            choice == "1"
        ):  # opening the journal menu to read, add, edit, or delete journal entries and to analyze the emotions in the journal entries to provide insights and recommendations based on the user's emotional state.
            print("Opening Journal...")
            journal()
        elif (
            choice == "2"
        ):  # opening the calendar menu to view journal entries based on specific dates and to provide a visual representation of the user's journaling habits and emotional patterns over time.
            print("Opening Calendar...")
            calendar_recs()
        elif (
            choice == "3"
        ):  # opening the support menu to provide users with various resources and techniques to help them cope with their emotions and improve their mental well-being based on the emotional analysis of their journal entries and their current emotional state.
            print("Opening Support...")
            support()
        elif (
            choice == "4"
        ):  # opening the reccomendations menu to provide users or developers to suggest feature and/or implementation ideas to make the app better and more helpful for the users and to encourage community involvement in the development of the app.
            print("Opening Recommendations...")
            recommendations()
        elif choice == "5":
            print("Exiting...")
            print("Thank you for using the app!Hope it was helpful.\u263a")
            break
        else:
            print("Invalid choice. Please try again.")


SUPPORTED_EMOTIONS = [
    "stress_overwhelm",
    "loneliness_isolation",
    "sadness_hopelessness",
    "anxiety_panic",
    "anger_frustration",
    "grief_loss",
    "academic_pressure",
    "burnout_exhaustion",
    "self_esteem_body_image",
    "family_relationship_issues",
    "abuse_unsafe_environment",
    "crisis_self_harm",
    "unknown_help",
    "happy_cheerful",
]


def closest_emotion(user_emotion):
    """Fuzzy-matches a user-typed emotion string to the nearest valid internal key.
    Returns unknown_help if no close match is found above the 0.4 similarity cutoff.
    [Fuzzy matching is a data technique that finds approximate matches rather than exact ones case they don't exist.]
    """
    match = get_close_matches(user_emotion.lower(), SUPPORTED_EMOTIONS, n=1, cutoff=0.4)
    return match[0] if match else "unknown_help"


def detect_emotion_with_claim(text, claimed_emotion=None):
    """Determines the final emotion from journal content with an optional user-provided claim.
    Crisis and abuse detections always override the claimed emotion — safety takes priority.
    """
    detected = JournalEntry.emotion_analysis(text)

    crisis_keys = {"crisis_self_harm", "abuse_unsafe_environment"}
    if detected in crisis_keys:
        return detected, detected

    if (
        claimed_emotion
    ):  # Honour the user's own label unless a crisis keyword was detected
        chosen = (
            claimed_emotion
            if claimed_emotion in SUPPORTED_EMOTIONS
            else closest_emotion(claimed_emotion)
        )
        return chosen, detected

    return detected, detected


def journal():
    """Function to handle the journal menu and user interactions for reading, adding, editing, and deleting journal entries."""
    clear_screen()
    while True:
        menu = """
        0. Back to Main Menu

        1. Read/Edit Journal Entry

        2. Add New Journal Entry

        3. Delete Journal Entry

        4. Exit Program

        """
        panel = Panel(
            Align.center(menu),
            title="[bold cyan]JOURNAL[/bold cyan]",
            style="bold blue",
            box=box.ASCII,
            padding=(1, 4),
            width=50,
        )

        console.print(Align.center(panel))
        choice = console.input(
            Align.center("[bold green]Enter your choice (0-4): [/bold green]")
        ).strip()
        if choice == "0":  # To go back to the main menu from the journal menu
            break
        elif choice == "1":
            content = []
            if os.path.exists("data/journal_entries.bin"):
                try:
                    with open(
                        "data/journal_entries.bin", "rb"
                    ) as f:  # opening the binary file containing journal entries and reading the entries to display them to the user and allow them to select an entry to read or edit.
                        while True:
                            #
                            try:
                                entry = pickle.load(
                                    f
                                )  # As it loads 1 entry at a time, the entries are appended to a list to keep track of them and to display them to the user for selection. This also allows for efficient memory usage as it doesn't load all entries at once.
                                content.append(entry)

                            except EOFError:

                                break
                        content.sort(key=lambda x: str(x.date))
                except (pickle.UnpicklingError, Exception):
                    if os.path.exists("data/journal_entries_backup.bin"):
                        os.remove("data/journal_entries_backup.bin")

                    os.rename(
                        "data/journal_entries.bin", "data/journal_entries_backup.bin"
                    )
                    console.print(
                        "[bold red]Journal file was corrupted and has been reset. A backup was saved.[/bold red]"
                    )
                if (
                    not content
                ):  # Binary file exists but is empty — no entries written yet
                    console.print("No journal entries found.")
                    continue
                for entry in content:
                    console.print(
                        f"ID: {entry.id}, Title: {entry.title}, Date: {entry.date},  Mood: {entry.mood}, Emotion: {display_emotion(entry.emotion)}"
                    )
                    if hasattr(
                        entry, "claimed_emotion"
                    ):  # Only present if user provided their own label
                        console.print(f"[dim]Claimed: {entry.claimed_emotion}[/dim]")

                    if (
                        hasattr(entry, "detected_emotion")
                        and hasattr(entry, "claimed_emotion")
                        and entry.claimed_emotion != entry.detected_emotion
                    ):
                        console.print(
                            f"[dim]Detected: {display_emotion(entry.detected_emotion)}[/dim]"
                        )
                entry_id_input = console.input(
                    "Enter the ID of the journal entry you want to read/edit: "
                ).strip()
                if not entry_id_input:
                    console.print("[bold red]No ID entered.[/bold red]")
                    continue
                try:
                    entry_id = int(entry_id_input)
                except ValueError:
                    console.print("[bold red]Please enter a valid number.[/bold red]")
                    continue
                with open("data/journal_entries.bin", "rb") as f, open(
                    "data/journal_entries_temp.bin", "wb"
                ) as temp_f:
                    content = []
                    found = False
                    while True:
                        try:
                            entry = pickle.load(f)
                        except EOFError:
                            break
                        content.append(entry)
                        content.sort(key=lambda x: str(x.date))
                        

                        if entry.id == entry_id:
                            found = True
                            scale = {
                                1: "\U0001f621",
                                2: "\U0001f641",
                                3: "\U0001f610",
                                4: "\U0001f642",
                                5: "\U0001f600",
                            }
                            display_mood = scale.get(
                                int(str(entry.mood).strip()), "Invalid mood"
                            )
                            header_table = Table(
                                box=None, show_header=False, expand=True
                            )
                            header_table.add_column(justify="left")
                            header_table.add_column(justify="right")
                            header_table.add_row(
                                f"[bold yellow]ID: {entry.id} | {entry.date} | {entry.time}[/bold yellow]",
                                f"[bold magenta]{display_mood} | {display_emotion(entry.emotion)}[/bold magenta]",
                            )
                            diary_layout = Table(
                                box=None, expand=True, show_header=False
                            )
                            diary_layout.add_column(justify="center")

                            diary_layout.add_row(header_table)
                            diary_layout.add_row(Rule(style="cyan"))
                            diary_layout.add_row(
                                f"[bold cyan]{entry.title.upper()}[/bold cyan]"
                            )
                            diary_layout.add_row("")
                            diary_layout.add_row(
                                f"[italic white]{entry.content}[/italic white]"
                            )
                            console.print(
                                Align.center(
                                    Panel(
                                        diary_layout,
                                        box=box.ROUNDED,
                                        width=65,
                                        style="bold blue",
                                    )
                                )
                            )
                            edit_choice = console.input(
                                "Do you want to edit this entry? (y/n): "
                            ).strip()
                            if edit_choice.lower() == "y":
                                print("Press Enter to keep the original value.")
                                new_title = console.input(
                                    f"Title [{entry.title}]: "
                                ).strip()
                                new_date = console.input(
                                    f"Date [{entry.date}]: "
                                ).strip()
                                new_time = console.input(
                                    f"Time [{entry.time}]: "
                                ).strip()
                                new_mood = console.input(
                                    f"Mood [{entry.mood}]: "
                                ).strip()

                                if (
                                    hasattr(entry, "detected_emotion")
                                    and entry.detected_emotion != entry.emotion
                                ):
                                    console.print(
                                        f"[dim]Detected: {display_emotion(entry.detected_emotion)}[/dim]"
                                    )

                                new_emotion = console.input(
                                    f"Emotion [{display_emotion(entry.emotion)}]: "
                                ).strip()

                                console.print("[bold cyan]Current Content:[/bold cyan]")
                                console.print(entry.content)

                                console.print("\n[bold green]Options:[/bold green]")
                                console.print("1. Keep existing")
                                console.print("2. Replace completely")
                                console.print("3. Append to existing")

                                content_choice = (
                                    console.input("Choose option (1-3): ").strip()
                                    or "1"
                                )  # Default to keep existing if user presses Enter without a choice

                                if content_choice == "1":
                                    final_content = entry.content
                                elif content_choice == "2":
                                    console.print(
                                        "[dim]Type SAVE on a new line when done.[/dim]"
                                    )

                                    lines = []

                                    while True:
                                        line = input()
                                        if line.strip().upper() == "SAVE":
                                            break
                                        lines.append(line)

                                    final_content = "\n".join(lines)
                                    if not final_content.strip():

                                        console.print(
                                            "[bold red]Journal entry cannot be empty.[/bold red]"
                                        )

                                        continue
                                elif content_choice == "3":
                                    console.print(
                                        "[dim]Type additional text. SAVE to finish.[/dim]"
                                    )

                                    lines = []

                                    while True:

                                        line = input()

                                        if line.strip().upper() == "SAVE":
                                            break

                                        lines.append(line)

                                    final_content = (
                                        entry.content + "\n" + "\n".join(lines)
                                    )
                                else:
                                    final_content = entry.content

                                updated_title = (
                                    new_title if new_title.strip() else entry.title
                                )
                                if new_date.strip():
                                    try:
                                        updated_date = datetime.date.fromisoformat(
                                            new_date.strip()
                                        )
                                    except ValueError:
                                        console.print(
                                            "[bold red]Invalid date format. Keeping original.[/bold red]"
                                        )
                                        updated_date = entry.date
                                else:
                                    updated_date = entry.date
                                updated_time = (
                                    new_time if new_time.strip() else entry.time
                                )
                                if new_mood.strip():

                                    try:

                                        mood_value = int(new_mood.strip())

                                        if 1 <= mood_value <= 5:
                                            updated_mood = mood_value
                                        else:
                                            updated_mood = entry.mood

                                    except ValueError:
                                        updated_mood = entry.mood

                                else:
                                    updated_mood = entry.mood

                                claimed_emotion = (
                                    new_emotion.strip() if new_emotion.strip() else None
                                )
                                updated_emotion, updated_detected = (
                                    detect_emotion_with_claim(
                                        final_content, claimed_emotion
                                    )
                                )
                                # Rebuild entry with updated values while preserving the original ID
                                updated_entry = JournalEntry(
                                    entry.id,
                                    updated_title,
                                    updated_date,
                                    updated_time,
                                    updated_mood,
                                    updated_emotion,
                                    final_content,
                                )

                                if claimed_emotion:
                                    updated_entry.claimed_emotion = claimed_emotion
                                    updated_entry.detected_emotion = updated_detected

                                pickle.dump(updated_entry, temp_f)
                                console.print(
                                    "[bold green]Entry updated successfully.[/bold green]"
                                )
                            else:
                                console.print(
                                    "[dim]Okay! Leaving entry unchanged.[/dim]"
                                )
                                time.sleep(1)
                                pickle.dump(entry, temp_f)
                        else:
                            pickle.dump(entry, temp_f)
                if not found:
                    console.print("[bold red]No entry found with that ID.[/bold red]")
                    try:
                        os.remove("data/journal_entries_temp.bin")
                    except OSError:
                        pass
                else:
                    saved = False
                    for _ in range(5):
                        try:
                            os.replace(
                                "data/journal_entries_temp.bin",
                                "data/journal_entries.bin",
                            )
                            console.print("[dim]Saved to disk.[/dim]")
                            saved = True
                            break
                        except PermissionError:
                            time.sleep(0.5)
                    if not saved:
                        console.print(
                            "[bold red]Could not save. Close any other program using the journal file and try again.[/bold red]"
                        )

            else:
                console.print("No journal entries found.")
        elif choice == "2":

            # Load all existing entries to check for a duplicate today entry and assign the next ID
            entries = []

            if os.path.exists("data/journal_entries.bin"):
                with open("data/journal_entries.bin", "rb") as f:
                    while True:
                        try:
                            entries.append(pickle.load(f))
                        except EOFError:
                            break
                    entries.sort(key=lambda x: str(x.date))
            today = str(datetime.date.today())

            already_exists = any(str(entry.date) == today for entry in entries)

            if already_exists:
                console.print(
                    "[bold yellow]You already wrote today. Edit instead.[/bold yellow]"
                )  # Allowing only 1 journal entry per day to allow for linear tracking
                continue

            if entries:
                id = entries[-1].id + 1
            # Checking thr last entry in the list to assign the next ID for the new journal entry to maintain a unique identifier for each entry and to keep track of the number of entries in the journal.

            else:
                id = 1
            # Collect all fields for the new entry from the user
            title = console.input("Title: ").strip()

            date = datetime.date.today()
            time_now = datetime.datetime.now().strftime(
                "%H:%M:%S"
            )  # Automatically assigning the current date and time to the new journal entry to ensure accurate tracking of when each entry was created and to provide context for the user's journaling habits and emotional patterns over time.

            scale = {
                1: "\U0001f621",  # Very dissatisfied (Red face)
                2: "\U0001f641",  # Dissatisfied (Slightly sad face)
                3: "\U0001f610",  # Neutral (Flat face)
                4: "\U0001f642",  # Satisfied (Slightly smiling face)
                5: "\U0001f600",  # Very satisfied (Grinning face)
            }

            console.print("Mood Scale:")

            for k, v in scale.items():
                console.print(f"{k}: {v}")
            # Loop until a valid integer between 1 and 5 is entered
            while True:
                try:
                    chosen = int(console.input("Choose mood (1-5): ").strip())
                    if 1 <= chosen <= 5:
                        break
                    console.print(
                        "[bold red]Please enter a number between 1 and 5.[/bold red]"
                    )
                except ValueError:
                    console.print("[bold red]Please enter a valid number.[/bold red]")
            mood = chosen

            emotion = console.input("Emotion (optional, leave blank for auto): ")

            console.print(
                "[dim]Type SAVE on new line[/dim]"
            )  # Dim text to indicate the instruction for saving the journal entry after writing the content, making it clear and easy for the user to understand how to save their entry once they are finished writing.

            lines = []
            # Collect journal content line by line until the user types SAVE
            while True:
                line = input()

                if line.strip().upper() == "SAVE":
                    break

                lines.append(line)

            content = "\n".join(lines)

            if not content.strip():

                console.print("[bold red]Journal entry cannot be empty.[/bold red]")

                continue
            # Use the written content and the optionally provided emotion (claimed) for detection

            claimed_emotion = emotion.strip().lower() if emotion.strip() else None

            if claimed_emotion:
                matched = closest_emotion(claimed_emotion)

                if matched == "unknown_help":

                    console.print(
                        "[bold yellow]Emotion not recognized. Using automatic detection instead.[/bold yellow]"
                    )

                    claimed_emotion = None
            final_emotion, detected_emotion = detect_emotion_with_claim(
                content, claimed_emotion
            )

            new_entry = JournalEntry(
                id, title, date, time_now, mood, final_emotion, content
            )

            if claimed_emotion:
                new_entry.claimed_emotion = claimed_emotion
                new_entry.detected_emotion = detected_emotion

            with open("data/journal_entries.bin", "ab") as f:
                pickle.dump(new_entry, f)

            console.print("[bold green]Journal entry created.[/bold green]")
        elif choice == "3":

            if not os.path.exists("data/journal_entries.bin"):
                console.print("[bold red]No journal entries found.[/bold red]")
                return

            entries = []

            with open("data/journal_entries.bin", "rb") as f:
                while True:
                    try:
                        entries.append(pickle.load(f))
                    except EOFError:
                        break
                entries.sort(key=lambda x: str(x.date))
            if not entries:
                console.print("[bold red]No entries available.[/bold red]")
                return

            console.print("[bold yellow]Existing Entries:[/bold yellow]")

            for entry in entries:
                console.print(
                    f"ID: {entry.id} | Title: {entry.title} | Date: {entry.date}"
                )

            delete_id = console.input(
                "\nEnter ID to delete (or press Enter to cancel): "
            ).strip()

            if not delete_id.strip():
                console.print("Delete cancelled.")
                continue

            try:
                delete_id = int(delete_id)
            except ValueError:
                console.print("[bold red]Invalid ID.[/bold red]")
                continue

            confirm = console.input(
                "Are you sure? This cannot be undone. (y/n): "
            ).strip()

            if confirm.lower() != "y":
                console.print("Deletion cancelled.")
                continue

            updated_entries = [entry for entry in entries if entry.id != delete_id]
            if len(updated_entries) == len(entries):
                console.print("[bold red]No entry found with that ID.[/bold red]")
                continue
            with open("data/journal_entries.bin", "wb") as f:
                for entry in updated_entries:
                    pickle.dump(entry, f)

            console.print("[bold green]Entry deleted successfully.[/bold green]")
        elif choice == "4":
            print("Exiting Journal...Hope you could get things off your chest!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")


def calendar_recs():
    """Showing the various days in calendar adn allowing the suer to check their journal entries based on the date and to provide a visual representation of the user's journaling habits and emotional patterns over time."""
    try:
        yy = int(console.input("Enter year: ").strip())
    except ValueError:
        console.print("[bold red]Invalid year.[/bold red]")
        return
    month_input = console.input("Enter month (1-12 or name): ").strip()

    month_map = {
        "jan": 1,
        "january": 1,
        "feb": 2,
        "february": 2,
        "mar": 3,
        "march": 3,
        "apr": 4,
        "april": 4,
        "may": 5,
        "jun": 6,
        "june": 6,
        "jul": 7,
        "july": 7,
        "aug": 8,
        "august": 8,
        "sep": 9,
        "september": 9,
        "oct": 10,
        "october": 10,
        "nov": 11,
        "november": 11,
        "dec": 12,
        "december": 12,
    }

    if month_input.isdigit():
        mm = int(month_input)
    else:
        mm = month_map.get(month_input.lower().strip())
    #
    if mm is None or mm < 1 or mm > 12:
        console.print("[bold red]Invalid month.[/bold red]")
        return

    calc = calendar.month(
        yy, mm
    )  # Calculating the calendar for the specified month and year to display it to the user and allow them to select a date to view their journal entries.
    while True:
        clear_screen()  # Redraw the calendar cleanly on each loop
        for (
            line
        ) in (
            calc.splitlines()
        ):  # Splitting the calendar output into lines and printing each line centered in the console.
            console.print(Align.center(line))

        date = console.input("Enter the date you want to view (DD): ").strip()
        if not date:
            print("Enter a valid date.")
        else:
            try:
                date = int(date)
                try:
                    datetime.date(yy, mm, date)
                except ValueError:
                    print("That date doesn't exist in this month.")
                    continue
                if date < 1 or date > 31:  # Checking if date is valid
                    print("Enter a valid date.")
                else:
                    if os.path.exists("data/journal_entries.bin"):
                        entries = []
                        with open("data/journal_entries.bin", "rb") as f:
                            while True:
                                try:
                                    content = pickle.load(f)
                                    entries.append(
                                        content
                                    )  # Collect all entries to filter by date
                                except EOFError:
                                    break
                            entries.sort(key=lambda x: str(x.date))
                        if entries:
                            found_on_date = [
                                entry
                                for entry in entries
                                if str(entry.date) == str(datetime.date(yy, mm, date))
                            ]
                            if found_on_date:
                                for entry in found_on_date:
                                    scale = {
                                        1: "😡",
                                        2: "🙁",
                                        3: "😐",
                                        4: "🙂",
                                        5: "😀",
                                    }
                                    display_mood = scale.get(
                                        int(str(entry.mood).strip()), ""
                                    )
                                    header_table = Table(
                                        box=None, show_header=False, expand=True
                                    )
                                    header_table.add_column(justify="left")
                                    header_table.add_column(justify="right")
                                    header_table.add_row(
                                        f"[bold yellow]ID: {entry.id} | {entry.date} | {entry.time}[/bold yellow]",
                                        f"[bold magenta]{display_mood} | {display_emotion(entry.emotion)}[/bold magenta]",
                                    )
                                    diary_layout = Table(
                                        box=None, expand=True, show_header=False
                                    )
                                    diary_layout.add_column(justify="center")
                                    diary_layout.add_row(header_table)
                                    diary_layout.add_row(Rule(style="cyan"))
                                    diary_layout.add_row(
                                        f"[bold cyan]{entry.title.upper()}[/bold cyan]"
                                    )
                                    diary_layout.add_row("")
                                    diary_layout.add_row(
                                        f"[italic white]{entry.content}[/italic white]"
                                    )
                                    console.print(
                                        Align.center(
                                            Panel(
                                                diary_layout,
                                                box=box.ROUNDED,
                                                width=65,
                                                style="bold blue",
                                            )
                                        )
                                    )
                            else:
                                console.print(
                                    "[bold yellow]No entries found for this date.[/bold yellow]"
                                )
                        else:
                            console.print(
                                "[bold yellow]No journal entries found.[/bold yellow]"
                            )
                    else:
                        console.print("No journal entries found.")
            except ValueError:
                print("Enter a valid date.")
        choice = console.input("Do you want to view another date? (y/n): ").strip()
        if choice.lower() != "y":
            break


def choose_emotion():
    """Displays a menu of emotions for the user to choose from and returns the corresponding emotion key based on the user's choice."""
    emotional_menu = """
          1. Stressed or Overwhelmed

          2. Lonely or Isolated

          3. Sad or Depressed

          4. Anxious or Panicked

          5. Angry or Frustrated

          6. Grief or Loss
 
          7. Academic Pressure

          8. Burnout or Exhaustion

    9. Self-esteem or Body Image Issues

    10. Family or Relationship Issues

    11. Abuse or unsafe environment

    12. Suicidal Thoughts or Self-harm

    13. I don't know but I need help

          14. Postive emotions\n 
      (Happy, Excited, Grateful, etc.)
    """
    emotion_map = {
        "1": "stress_overwhelm",
        "2": "loneliness_isolation",
        "3": "sadness_hopelessness",
        "4": "anxiety_panic",
        "5": "anger_frustration",
        "6": "grief_loss",
        "7": "academic_pressure",
        "8": "burnout_exhaustion",
        "9": "self_esteem_body_image",
        "10": "family_relationship_issues",
        "11": "abuse_unsafe_environment",
        "12": "crisis_self_harm",
        "13": "unknown_help",
        "14": "happy_cheerful",
    }
    # Having 14 different emotional categories to cover a wide range of emotions that teenagers might be experiencing and to provide more specific and tailored support and resources based on the user's emotional state.

    emotional_panel = Panel(
        # fomatting the emotional menu to make it appeasing and engaging.
        Align.center(emotional_menu),
        title="[bold cyan]EMOTIONAL SUPPORT[/bold cyan]",
        style="bold blue",
        box=box.ASCII,
        padding=(1, 4),
        width=50,
    )

    console.print(Align.center(emotional_panel))
    print()
    emotional_choice = console.input(
        "[bold green]Enter your choice (1-14): [/bold green]"
    ).strip()
    return emotion_map.get(emotional_choice)


def show_moreable(items, title, shown):
    """Shows one unseen item from a list, tracking shown items in a set to avoid repeats.
    Returns False when all items have been shown."""
    remaining = []

    for item in items:
        if isinstance(item, dict):
            key = item.get("text") or item.get("name") or str(item)
        else:
            key = str(item)

        if key not in shown:  # Only include items the user hasn't seen yet this session
            remaining.append(item)

    if not remaining:
        console.print(
            f"[bold yellow]No more {title} available right now. \n That's all for this category for now.[/bold yellow]"
        )
        return False

    item = random.choice(remaining)
    # Extract a hashable string key to track this item in the shown set
    if isinstance(item, dict):
        key = item.get("text") or item.get("name") or str(item)
    else:
        key = str(item)

    shown.add(key)
    JournalEntry.show_items(title, [item])
    return True


def support():
    """Support menu to provide users with various resources and techniques to help them cope with their emotions and improve their mental well-being based on the emotional analysis of their journal entries and their current emotional state."""
    menu = """
            0. Back to Main Menu

            1. Distractions

            2. Support

            3. Focus

            4. Emergency


    """

    while True:
        panel = Panel(
            Align.center(menu),
            title="[bold cyan]SUPPORT[/bold cyan]",
            style="bold blue",
            box=box.ASCII,
            padding=(1, 4),
            width=50,
        )
        clear_screen()
        console.print(Align.center(panel))
        print()
        choice = console.input(
            "[bold green]Enter your choice (0-4): [/bold green]"
        ).strip()

        if choice == "0":
            break

        elif choice == "1":
            emotion_key = choose_emotion()
            if not emotion_key:
                console.print("[bold red]Invalid choice. Please try again.[/bold red]")
                continue

            distractions = EMOTIONS[emotion_key].get("distractions", {})
            if not distractions:
                console.print(
                    "[bold yellow]Distractions are not the best fit here. Try the Support menu instead.[/bold yellow]"
                )
                continue

            shown_jokes = set()
            shown_quotes = set()
            shown_activities = set()
            shown_memes = set()
            #To avoid duplication
            show_moreable(distractions.get("jokes", []), "Joke", shown_jokes)
            show_moreable(distractions.get("quotes", []), "Quote", shown_quotes)
            show_moreable(
                distractions.get("activities", []), "Activity", shown_activities
            )
            show_moreable(distractions.get("memes", []), "Memes", shown_memes)

            while True:
                console.print(
                    Align.center(
                        "[dim white][J] Joke   [Q] Quote   [A] Activity   [M] Memes   [B] Back[/dim white]"
                    )
                )
                cmd = (
                    console.input("[bold green]Choose an option: [/bold green]")
                    .lower()
                    .strip()
                )
                
                if cmd == "j":
                    show_moreable(distractions.get("jokes", []), "Joke", shown_jokes)
                elif cmd == "q":
                    show_moreable(distractions.get("quotes", []), "Quote", shown_quotes)
                elif cmd == "a":
                    show_moreable(
                        distractions.get("activities", []), "Activity", shown_activities
                    )
                elif cmd == "m":
                    show_moreable(distractions.get("memes", []), "Memes", shown_memes)
                elif cmd == "b":
                    break
                else:
                    console.print("[bold red]Invalid option.[/bold red]")

        elif choice == "2":
            print()
            emotion_key = choose_emotion()

            if not emotion_key:
                console.print("[bold red]Invalid choice. Please try again.[/bold red]")
                continue

            support_data = EMOTIONS[emotion_key].get("support", {})

            shown_grounding = set()
            shown_breathing = set()
            shown_comfort = set()
            shown_resources = set()
            shown_hotlines = set()
            shown_reassurance = set()

            show_moreable(
                support_data.get("grounding", []), "Grounding", shown_grounding
            )
            show_moreable(
                support_data.get("breathing", []), "Breathing", shown_breathing
            )
            show_moreable(support_data.get("comfort", []), "Comfort", shown_comfort)
            show_moreable(
                support_data.get("resources", []), "Resources", shown_resources
            )
            show_moreable(support_data.get("hotlines", []), "Hotline", shown_hotlines)

            while True:
                console.print(
                    Align.center(
                        "[dim white][G] Grounding   [V] Breathing   [C] Comfort   [R] Resources   [H] Hotline   [N] Next/Reassurance   [B] Back[/dim white]"
                    )
                )
                cmd = (
                    console.input("[bold green]Choose an option: [/bold green]")
                    .lower()
                    .strip()
                )
                # Show one item from each category on entry so the screen isn't blank
                if cmd == "g":
                    show_moreable(
                        support_data.get("grounding", []), "Grounding", shown_grounding
                    )
                elif cmd == "v":
                    show_moreable(
                        support_data.get("breathing", []), "Breathing", shown_breathing
                    )
                elif cmd == "c":
                    show_moreable(
                        support_data.get("comfort", []), "Comfort", shown_comfort
                    )
                elif cmd == "r":
                    show_moreable(
                        support_data.get("resources", []), "Resources", shown_resources
                    )
                elif cmd == "h":
                    show_moreable(
                        support_data.get("hotlines", []), "Hotline", shown_hotlines
                    )
                elif cmd == "n":
                    show_moreable(
                        support_data.get("reassurance", []),
                        "Reassurance",
                        shown_reassurance,
                    )
                elif cmd == "b":
                    break
                else:
                    console.print("[bold red]Invalid option.[/bold red]")

        elif choice == "3":
            print()
            emotion_key = choose_emotion()

            if not emotion_key:
                console.print("[bold red]Invalid choice. Please try again.[/bold red]")
                continue
                #
            focus_data = EMOTIONS[emotion_key].get("focus", {})
            if not focus_data:
                console.print(
                    "[bold yellow]Focus tips are not the main priority here. Try Support instead.[/bold yellow]"
                )
                continue

            shown_study = set()
            shown_breakdown = set()
            shown_motivation = set()
            shown_productivity = set()

            show_moreable(
                focus_data.get("study_methods", []), "Study Method", shown_study
            )
            show_moreable(
                focus_data.get("task_breakdown", []), "Task Breakdown", shown_breakdown
            )
            show_moreable(
                focus_data.get("motivation", []), "Motivation", shown_motivation
            )
            show_moreable(
                focus_data.get("productivity", []), "Productivity", shown_productivity
            )

            while True:
                console.print(
                    Align.center(
                        "[dim white][S] Study Methods   [T] Task Breakdown   [O] Motivation   [P] Productivity   [B] Back[/dim white]"
                    )
                )
                cmd = console.input("[bold green]Choose: [/bold green]").lower().strip()

                if cmd == "s":
                    show_moreable(
                        focus_data.get("study_methods", []), "Study Method", shown_study
                    )
                elif cmd == "t":
                    show_moreable(
                        focus_data.get("task_breakdown", []),
                        "Task Breakdown",
                        shown_breakdown,
                    )
                elif cmd == "o":
                    show_moreable(
                        focus_data.get("motivation", []), "Motivation", shown_motivation
                    )
                elif cmd == "p":
                    show_moreable(
                        focus_data.get("productivity", []),
                        "Productivity",
                        shown_productivity,
                    )
                elif cmd == "b":
                    break
                else:
                    console.print("[bold red]Invalid option.[/bold red]")

        elif choice == "4":
            console.print(
                Align.center(
                    "[bold red]If you are in an emergency situation, please call your local emergency number or go to the nearest emergency room immediately.[/bold red]"
                )
            )
            console.print(
                Align.center(
                    "[bold green]But if speaking feels hard, here are some options below.[/bold green]"
                )
            )
            print()
            emotion_key = choose_emotion()

            if not emotion_key:
                console.print("[bold red]Invalid choice. Please try again.[/bold red]")
                continue
            if emotion_key == "happy_cheerful":
                console.print(
                    "[bold yellow]It sounds like you are doing okay right now. If something changes, we are here.[/bold yellow]"
                )
                continue

            emergency_data = EMOTIONS[emotion_key]["emergency"]

            shown_trusted = set()
            shown_crisis = set()
            shown_chat = set()
            shown_steps = set()
            shown_reassurance = set()
            shown_resources = set()

            show_moreable(
                emergency_data.get("trusted_contact", []),
                "Trusted Contact",
                shown_trusted,
            )
            show_moreable(
                emergency_data.get("crisis_lines", []), "Crisis Line", shown_crisis
            )
            show_moreable(
                emergency_data.get("chat_support", []), "Chat Support", shown_chat
            )
            show_moreable(
                emergency_data.get("urgent_steps", []), "Urgent Step", shown_steps
            )
            show_moreable(
                emergency_data.get("reassurance", []), "Reassurance", shown_reassurance
            )
            show_moreable(
                emergency_data.get("resources", []), "Resources", shown_resources
            )

            while True:
                console.print(
                    Align.center(
                        "[dim white][U] Trusted Contact   [L] Crisis Lines   [X] Chat Support   [E] Urgent Steps   [N] Reassurance   [R] Resources   [B] Back[/dim white]"
                    )
                )
                cmd = console.input("[bold green]Choose: [/bold green]").lower().strip()

                if cmd == "u":
                    show_moreable(
                        emergency_data.get("trusted_contact", []),
                        "Trusted Contact",
                        shown_trusted,
                    )
                elif cmd == "l":
                    show_moreable(
                        emergency_data.get("crisis_lines", []),
                        "Crisis Line",
                        shown_crisis,
                    )
                elif cmd == "x":
                    show_moreable(
                        emergency_data.get("chat_support", []),
                        "Chat Support",
                        shown_chat,
                    )
                elif cmd == "e":
                    show_moreable(
                        emergency_data.get("urgent_steps", []),
                        "Urgent Step",
                        shown_steps,
                    )
                elif cmd == "n":
                    show_moreable(
                        emergency_data.get("reassurance", []),
                        "Reassurance",
                        shown_reassurance,
                    )
                elif cmd == "r":
                    show_moreable(
                        emergency_data.get("resources", []),
                        "Resources",
                        shown_resources,
                    )
                elif cmd == "b":
                    break
                else:
                    console.print("[bold red]Invalid option.[/bold red]")

        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")


def recommendations():
    """To give users and developers a platform to reach out for suggestions, feedback,contribution and to understand the purpose and vision of the program to foster a sense of community and collaboration among users and developers, and to encourage continuous improvement and growth of the program based on user needs and feedback."""

    console.print(
        Align.center(
            "This is a program made to help the community of teenagers with the help of journaling and seeking support by various means."
        ),
        style="cyan",
    )

    console.print(
        Align.center(
            "This is just the base version and anyone is free to add more features to it and make it better. We are open to suggestions and feedbacks."
        )
    )
    rep_link="[link=https://github.com/Shimona012/Lighthouse] GitHub Repository [/link]"
    console.print(Align.center(f"Github Repository: {rep_link}"), style="bold green")
    console.print(Align.center("Made for teens by teens <3"), style="bold magenta")
    rainbow_name = (
        "[red]-S[/red]"
        "[orange1]h[/orange1]"
        "[yellow]i[/yellow]"
        "[green]m[/green]"
        "[cyan]o[/cyan]"
        "[blue]n[/blue]"
        "[purple]a[/purple] "
        "[pink1]B[/pink1]"
        "[red]a[/red]"
        "[orange1]k[/orange1]"
        "[yellow]s[/yellow]"
        "[green]h[/green]"
        "[cyan]i[/cyan]"
    )

    console.print(Align.center(rainbow_name, style="italic"))

    choice = console.input("Do you wish to go back to the main menu? (y/n): ")
    if choice.lower() == "y":
        return
    else:
        console.print(
            Align.center(
                "Thank you for using the program! Hope it was helpful. \u263a"
            ),
            style="bold yellow",
        )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print(
            "\n[bold yellow]Exiting the program...Thank you!Byee :D[/bold yellow]"
        )
