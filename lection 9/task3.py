# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

def list_sort(sum_list, tmp_sum):
    """
    Функция для сортировки сумм покупок. Принимает на вход новую сумму и список трем самых больших сумм покупок.
    Записывает новую сумму на первую позицию списка, сортирует список.
    """
    sum_list[0] = tmp_sum
    sum_list.sort()


def expensive_purchases(path):
    """
    Функция для определения суммы трех самых дорогих покупок.
    Принимает на вход файл с "покупками", где в каждой строке записана цена товара.
    "Покупки" должны быть разделены пустыми строками.
    Возвращает сумму трех самых дорогих покупок.
    """
    sum_list = [0, 0, 0, 0]
    tmp_sum = 0
    try:
        with open(path, 'r+', encoding='UTF-8') as file:
            for line in file:
                try:
                    tmp_sum += int(line)
                except ValueError:
                    list_sort(sum_list, tmp_sum)
                    tmp_sum = 0
    except FileNotFoundError:
        print('Не получилось прочитать файл')

    # чтобы не потерять последний блок с ценами сортируем еще раз:
    list_sort(sum_list, tmp_sum)

    return sum(sum_list[1:4])


three_most_expensive_purchases = expensive_purchases('test_file/task_3.txt')

assert three_most_expensive_purchases == 202346
