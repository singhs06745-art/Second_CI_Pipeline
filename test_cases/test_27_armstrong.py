import importlib

module = importlib.import_module("27_armstrong")


def test_armstrong_number():
    assert module.is_armstrong(153) is True


def test_another_armstrong():
    assert module.is_armstrong(370) is True


def test_non_armstrong():
    assert module.is_armstrong(123) is False


def test_single_digit():
    assert module.is_armstrong(5) is True


def test_negative_number():
    assert module.is_armstrong(-153) is False