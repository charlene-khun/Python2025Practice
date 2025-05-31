def reverse_string(s):
    """
    Reverses the input string.

    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("Python")
    'nohtyP'
    >>> reverse_string("")
    ''
    >>> reverse_string("12345")
    '54321'
    >>> reverse_string("abc") == "abc"  # False case
    False
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

def is_palindrome(s):
    """
    Checks if the input string is a palindrome (case-insensitive).

    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("Level")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("Noon")
    True
    >>> is_palindrome("Python")
    False
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    s = s.lower()
    return s == reverse_string(s)