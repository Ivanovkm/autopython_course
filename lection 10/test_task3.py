# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("test_input, expected", [((10, 5), 2), pytest.param((1, 0), None, marks=pytest.mark.skip),
                                                  ((10, 6, 3), 0.5555555555555556), ((-999, 3, 3), -111),
                                                  (('1', 2, 3), None)], ids=['int division', 'zero_division',
                                                                             'reminder_devision',
                                                                             'minus division', 'bad_type_div'])
def test_all_division(test_input, expected):
    assert all_division(*test_input) == expected
