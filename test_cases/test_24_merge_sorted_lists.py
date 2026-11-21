import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_merge_two_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_first_list_empty():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]


def test_second_list_empty():
    assert merge_sorted_lists([1, 2], []) == [1, 2]


def test_both_lists_empty():
    assert merge_sorted_lists([], []) == []


def test_lists_with_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_one_list_has_one_element():
    assert merge_sorted_lists([3], [1, 2]) == [1, 2, 3]