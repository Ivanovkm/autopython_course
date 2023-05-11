# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def which_triangle(a, b, c):
    # Здесь нужно написать код
    sides = [a, b, c]
    type_triangle, eq_sides = None, 0

    for x in sides:
        if sides.count(x) > 1:
            eq_sides += 1

    if max(sides) >= sum(sides) - max(sides):
        type_triangle = 'Не треугольник'
    elif eq_sides == 3:
        type_triangle = 'Равносторонний'
    elif eq_sides == 2:
        type_triangle = 'Равнобедренный'
    else:
        type_triangle = 'Обычный'

    return type_triangle

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
