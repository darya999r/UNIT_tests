"""Модуль для тестирования кода"""
import pytest

from hw_6 import Lists


@pytest.fixture
def list1():
    """Инициализация первого списка"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    """Инициализация второго"""
    return [6, 7, 8, 9, 10]


def test_init(list1, list2):
    """Проверка инициализации класса"""
    lists = Lists(list1, list2)
    assert lists.list1 == list1
    assert lists.list2 == list2


def test_get_lists_averages(list1, list2):
    """Проверка положительных средних значений списков"""
    lists = Lists(list1, list2)
    assert lists.get_lists_averages() == (3, 8)


@pytest.mark.parametrize("list1, list2, result",
                         [([1, 2, 3], [], (2, 0)), ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
def test_get_empty_lists_averages(list1, list2, result):
    """Проверка пустых средних значений"""
    lists = Lists(list1, list2)
    assert lists.get_lists_averages() == result


@pytest.mark.parametrize("list1, list2, result",
                         [([1, 2, 3], [5], (2, 5)), ([5], [1, 2, 3], (5, 2)), ([5], [5], (5, 5))])
def test_get_one_elemented_lists_averages(list1, list2, result):
    """Проверка средних значений при одном элементе"""
    lists = Lists(list1, list2)
    assert lists.get_lists_averages() == result


def test_first_average_more(list1, list2, capfd):
    """Проверка сообщения 'Первый список имеет большее среднее значение'"""
    lists = Lists(list2, list1)
    lists.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Первый список имеет большее среднее значение"


def test_second_average_more(list1, list2, capfd):
    """Проверка сообщения 'Второй список имеет большее среднее значение'"""
    lists = Lists(list1, list2)
    lists.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Второй список имеет большее среднее значение"


def test_equal_averages(list1, capfd):
    """Проверка сообщения 'Средние значения равны'"""
    lists = Lists(list1, list1)
    lists.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Средние значения равны"
