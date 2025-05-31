# test_string_utils_pytest.py
import pytest
from string_utils import reverse_string, is_palindrome

# ----------- Valid input tests using simple assert ----------
def test_reverse_string_valid():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("12345") == "54321"

def test_is_palindrome_valid():
    assert is_palindrome("racecar")
    assert is_palindrome("Level")
    assert is_palindrome("A")
    assert is_palindrome("")
    assert not is_palindrome("hello")

# ----------- Parameterized tests for reverse_string ----------
@pytest.mark.parametrize("input_str, expected", [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("", ""),
    ("a", "a"),
    ("12345", "54321"),
])
def test_reverse_string_param(input_str, expected):
    assert reverse_string(input_str) == expected

# ----------- Parameterized tests for is_palindrome ----------
@pytest.mark.parametrize("input_str, expected", [
    ("racecar", True),
    ("Level", True),
    ("A", True),
    ("", True),
    ("hello", False),
])
def test_is_palindrome_param(input_str, expected):
    assert is_palindrome(input_str) == expected

# ----------- Exception tests ----------
def test_reverse_string_invalid():
    with pytest.raises(TypeError):
        reverse_string(None)
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string(["h", "e", "l", "l", "o"])

def test_is_palindrome_invalid():
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(12321)
    with pytest.raises(TypeError):
        is_palindrome(["r", "a", "c", "e"])

# Added and explored a fixture
@pytest.fixture
def sample_data():
    return "racecar"

@pytest.fixture
def sample_data_1():
    return "hello"

@pytest.mark.usefixtures("sample_data")
def test_reverse_string(sample_data):
    assert reverse_string(sample_data) == "racecar"

@pytest.mark.usefixtures("sample_data")
def test_is_a_palindrome(sample_data):
    assert is_palindrome(sample_data) is True

@pytest.mark.usefixtures("sample_data_1")
def test_is_a_palindrome_false(sample_data_1):
    assert is_palindrome(sample_data_1) is False
