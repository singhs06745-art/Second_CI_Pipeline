import importlib

module = importlib.import_module("22_anagram")
are_anagrams = module.are_anagrams


def test_anagram_strings():
    assert are_anagrams("listen", "silent") == True


def test_non_anagram_strings():
    assert are_anagrams("hello", "world") == False


def test_uppercase_strings():
    assert are_anagrams("Listen", "Silent") == True


def test_strings_with_spaces():
    assert are_anagrams("rail safety", "fairy tales") == True


def test_empty_strings():
    assert are_anagrams("", "") == True