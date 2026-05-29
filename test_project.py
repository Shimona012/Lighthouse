import pytest
import calendar
import datetime
from Emotional_Data import EMOTIONS
from project import (
    JournalEntry,
    detect_emotion_with_claim,
    closest_emotion,
    display_emotion,
    SUPPORTED_EMOTIONS,
    support,
)


def test_emotion_analysis():
    """To test if correct emotions are being detected."""
    assert (
        JournalEntry.emotion_analysis(
            "I feel so overwhelmed with everything....I don't know what to do"
        )
        == "stress_overwhelm"
    )
    assert (
        JournalEntry.emotion_analysis(
            "I have no one to talk to and I feel completely alone"
        )
        == "loneliness_isolation"
    )
    assert (
        JournalEntry.emotion_analysis(
            "I feel empty what if nothing will ever get better"
        )
        == "sadness_hopelessness"
    )
    assert (
        JournalEntry.emotion_analysis(
            "I can't help but panic about every single thing.Its like I can't breathe."
        )
        == "anxiety_panic"
    )
    assert (
        JournalEntry.emotion_analysis("I am so frustrated I could scream")
        == "anger_frustration"
    )
    assert (
        JournalEntry.emotion_analysis("I have three exams tomorrow and idk what to do")
        == "academic_pressure"
    )
    assert (
        JournalEntry.emotion_analysis(
            "I feel unsafe at home, I don't think they should be being this mean to me.. "
        )
        == "abuse_unsafe_environment"
    )
    assert (
        JournalEntry.emotion_analysis(" I think,I want to hurt myself")
        == "crisis_self_harm"
    )
    assert (
        JournalEntry.emotion_analysis(
            "I am exhausted and completely burnt out to even do anything "
        )
        == "burnout_exhaustion"
    )
    assert (
        JournalEntry.emotion_analysis(" I miss them so much it hurts..why")
        == "grief_loss"
    )
    assert (
        JournalEntry.emotion_analysis(
            " I hate how I look, I just wish I could look prettier"
        )
        == "self_esteem_body_image"
    )
    assert (
        JournalEntry.emotion_analysis("things at home are really bad right now ")
        == "family_relationship_issues"
    )
    assert (
        JournalEntry.emotion_analysis("xyzqqqblarghhh nothing here matches ughhh ")
        == "unknown_help"
    )
    assert (
        JournalEntry.emotion_analysis(" I am so happy, today was finally a good day")
        == "happy_cheerful"
    )
    assert JournalEntry.emotion_analysis(" ") == "unknown_help"


def test_calendar_generation():
    """To test handling of days aand canlendar generation"""
    _, days = calendar.monthrange(2026, 2)
    assert days == 28

    _, days = calendar.monthrange(2026, 1)
    assert days == 31

    weekday, _ = calendar.monthrange(2026, 5)
    assert isinstance(weekday, int)
    assert 0 <= weekday <= 6


def test_detect_emotion_with_claim():
    """To test if the program handles both user-given and detected emotions separately,unknown emotions and crisis situations"""
    emotion, detected = detect_emotion_with_claim(
        "I feel empty and hopeless", claimed_emotion="anger_frustration"
    )
    assert emotion == "anger_frustration"
    assert detected == "sadness_hopelessness"

    emotion, detected = detect_emotion_with_claim(
        "I want to hurt myself", claimed_emotion="happy_cheerful"
    )
    assert emotion == "crisis_self_harm"
    assert detected == "crisis_self_harm"

    emotion, detected = detect_emotion_with_claim("I am so stressed")
    assert emotion == detected

    emotion, detected = detect_emotion_with_claim(
        "today was okay", claimed_emotion="xyzblarghhh"
    )
    assert emotion == "unknown_help"


#
def test_journal_entry():
    """To test journal creation."""
    entry = JournalEntry(
        id=1,
        title="First Day",
        date=datetime.date.today(),
        time="12:00:00",
        mood=3,
        emotion="stress_overwhelm",
        content="I feel extremely stressed today",
    )
    assert entry.title == "First Day"
    assert entry.mood == 3
    assert entry.emotion == "stress_overwhelm"
    assert entry.content == "I feel extremely stressed today"
    assert not hasattr(entry, "claimed_emotion")  #


#
def test_closest_emotion():
    """To test if user given emotions are matched to their most similar counterparts in the program."""
    assert closest_emotion("stresed") == "stress_overwhelm"
    assert closest_emotion("grief_loss") == "grief_loss"
    assert closest_emotion("GRIEF_LOSS") == "grief_loss"
    assert closest_emotion("banana_xyz_blarg") == "unknown_help"


#
def test_display_emotion():
    """To test if a uder-friendly key is returned."""
    assert display_emotion("stress_overwhelm") == "Stressed"
    assert display_emotion("crisis_self_harm") == "Crisis"
    assert display_emotion("happy_cheerful") == "Happy"
    assert display_emotion("unknown_help") == "Unknown"
    assert display_emotion("some_random_key") == "Some Random Key"


if __name__ == "__main__":
    pytest.main()
