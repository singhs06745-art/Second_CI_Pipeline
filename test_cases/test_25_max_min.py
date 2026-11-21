import importlib

module = importlib.import_module("25_max_min")


def test_positive_numbers():
    assert module.find_max_min([10, 5, 20, 3]) == (20, 3)


def test_negative_numbers():
    assert module.find_max_min([-5, -2, -10]) == (-2, -10)


def test_single_number():
    assert module.find_max_min([7]) == (7, 7)


def test_empty_list():
    assert module.find_max_min([]) == (None, None)


def test_duplicate_numbers():
    assert module.find_max_min([4, 4, 4]) == (4, 4)
    