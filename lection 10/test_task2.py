# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_zero_division():
    assert all_division(1, 0)

@pytest.mark.smoke
def test_int_division():
    assert all_division(10, 5, 2) == 1.0


def test_reminder_divison():
    assert all_division(10, 6, 3) == 0.5555555555555556


def test_not_digit():
    with pytest.raises(TypeError):
        all_division('1', 2, 3)

def test_minus():
    assert all_division(-999, 3, 3) == -111