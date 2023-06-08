from datetime import datetime

import pytest


@pytest.fixture()
def my_method_fixture():
    tstart = datetime.now()
    print('Начало теста:', tstart.strftime('%H:%M:%S'))
    yield None
    tend = datetime.now()
    print('Окончание теста: ', tend.strftime('%H:%M:%S'))
    print('Тест выполнялся: ' + str((datetime.now() - tstart).total_seconds()) + ' секунд')


@pytest.fixture(scope='class')
def my_class_fixture():
    tstart = datetime.now()
    print('Начало выполнения тестов класса:', tstart.strftime('%H:%M:%S'))
    yield None
    tend = datetime.now()
    print('Окончание выполнения тестов класса:', tend.strftime('%H:%M:%S'))
    print('Все тесты выполнялись: ' + str((datetime.now() - tstart).total_seconds()) + ' секунд')
