# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('my_class_fixture')
class TestClass:

    def test_zero_division(self, my_method_fixture):
        print('Выполнение теста')
        time.sleep(1)
        assert all_division(1, 0)

    def test_int_division(self):
        assert all_division(10, 5, 2) == 1.0

    def test_reminder_divison(self):
        assert all_division(10, 6, 3) == 0.5555555555555556

    def test_not_digit(self):
        with pytest.raises(TypeError):
            all_division('1', 2, 3)

    def test_minus(self):
        assert all_division(-999, 3, 3) == -111
