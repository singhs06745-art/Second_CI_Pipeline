import importlib

module = importlib.import_module("26_second_largest")


def test_normal_numbers():
    assert module.second_largest([10, 20, 5, 8]) == 10


def test_duplicate_numbers():
    assert module.second_largest([10, 10, 5, 5]) == 5


def test_negative_numbers():
    assert module.second_largest([-5, -2, -10]) == -5


def test_single_number():
    assert module.second_largest([7]) is None


def test_empty_list():
    assert module.second_largest([]) is None