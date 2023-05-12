# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    new_num = 0
    lst = [int(x) for x in str(num)]  # переводим число num в список из его цифр
    # Начинаем перебор цифр числа num:
    for x in range(len(lst)):
        actual_digit = lst[x]
        for d in reversed(range(lst[x] + 1, 10)):
            lst[x] = d
            new_num = int(''.join(str(y) for y in lst))
            if new_num % 3 == 0:
                break
            else:
                new_num = 0
        if new_num != 0:
            break
        else:
            lst[x] = actual_digit

    if new_num == 0:
        for x in reversed(range(len(lst))):
            actual_digit = lst[x]
            for d in reversed(range(1, lst[x])):
                lst[x] = d
                new_num = int(''.join(str(y) for y in lst))
                if new_num % 3 == 0:
                    break
                else:
                    new_num = 0
            if new_num != 0:
                break
            else:
                lst[x] = actual_digit
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
