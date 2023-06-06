# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

def expensive_purchases(path):
    """
    Функция для определения суммы трех самых дорогих покупок.
    Принимает на вход файл с "покупками", где в каждой строке записана цена товара.
    "Покупки" должны быть разделены пустыми строками.
    Возвращает сумму трех самых дорогих покупок.
    """
    sum_dict = {'first': 0, 'second': 0, 'third': 0}
    tmp_sum = 0

    try:
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                try:
                    tmp_sum += int(line)
                except ValueError:

                    if tmp_sum > sum_dict['first']:
                        sum_dict['third'] = sum_dict['second']
                        sum_dict['second'] = sum_dict['first']
                        sum_dict['first'] = tmp_sum

                    elif sum_dict['second'] < tmp_sum < sum_dict['first']:
                        sum_dict['third'] = sum_dict['second']
                        sum_dict['second'] = tmp_sum

                    elif sum_dict['third'] < tmp_sum < sum_dict['second']:
                        sum_dict['third'] = tmp_sum

                    tmp_sum = 0

    except FileNotFoundError:
        print('Не получилось прочитать файл')

    return sum(sum_dict.values())


three_most_expensive_purchases = expensive_purchases('test_file/task_3.txt')

assert three_most_expensive_purchases == 202346
