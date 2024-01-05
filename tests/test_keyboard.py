from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard():
    return Keyboard("Dark Project KD87A", 9600, 5)


def test_init(keyboard):
    assert keyboard.language == "EN"
    assert str(keyboard) == "Dark Project KD87A"


def test_change_lang(keyboard):
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"


def test_setter(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = "CH"
