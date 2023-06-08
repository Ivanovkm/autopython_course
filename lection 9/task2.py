# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.

import datetime
import os


def func_log(file_log='log.txt'):
    """
    Функция-декоратор для логирования вызовов функций. Может принимать строку-путь
    к файлу, куда нужно писать лог. Создает файл с логами вызовов,
    каждый вызов в формате '<имя функции> вызвана %d.%m %H:%M:%S'
    """

    def log_decorator(func):
        def wrapper(*args, **kwargs):
            # Чтобы help возвращал имя исходной функции и ее документацию:
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
            try:
                norm_path = os.path.normpath(file_log)
                with open(norm_path, 'a', encoding='UTF-8') as file:
                    file.write(
                        func.__name__ + ' вызвана: ' + datetime.datetime.now().strftime('%d.%m %H:%M:%S') + '\n')
            except FileNotFoundError as e:
                print(repr(e), f'Ошибка, не удалось создать файл для логирования {func.__name__}')
            func(*args, **kwargs)

        return wrapper

    return log_decorator

# Не нашел, как поменять аргументы функции с args, kwargs на аргументы исходной функции. (
