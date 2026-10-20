from text_cleaner import clean_text
import pytest

def test_removes_leading_and_trailing_whitespace():
    result = clean_text("   Hello, World!   ")

    assert result == "Hello, World!"

def test_handles_empty_string():
    result = clean_text("")

    assert result == ""

def test_replaces_repeated_spaces_with_one():
    result = clean_text("Hello     AI")

    assert result == "Hello AI"

def test_normalizes_tabs_and_newlines():
    result = clean_text("Hello\t\tAI\nEngineering")

    assert result == "Hello AI Engineering"

@pytest.mark.parametrize("value",[123,None,True])
def test_invalid_input(value):
    with pytest.raises(TypeError,match = "text must be a string"):
        clean_text(value)