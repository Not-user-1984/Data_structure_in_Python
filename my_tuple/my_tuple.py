# Создаем кортеж с разными типами данных
my_tuple = (10, "Python", 3.14, (1, 2, 3))

# Выводим весь кортеж и его длину
print("Исходный кортеж:", my_tuple)
print("Длина кортежа:", len(my_tuple))

# Доступ к элементам по индексу
print("Первый элемент:", my_tuple[0])  # 10
print("Вложенный кортеж:", my_tuple[3])  # (1, 2, 3)
print("Элемент вложенного кортежа:", my_tuple[3][1])  # 2

# Работа со срезами
print("Срез [1:3]:", my_tuple[1:3])  # ("Python", 3.14)
print("Срез с шагом [::2]:", my_tuple[::2])  # (10, 3.14)
print("Обратный кортеж:", my_tuple[::-1])  # ((1, 2, 3), 3.14, "Python", 10)

# Распаковка кортежа
num, text, pi, nested = my_tuple
print("Распакованные значения:", num, text, pi, nested)

# Проверка наличия элемента
if "Python" in my_tuple:
    print("'Python' есть в кортеже!")

# Конкатенация кортежей
new_tuple = my_tuple + (42, "end")
print("После конкатенации:", new_tuple)

# Повторение кортежа
repeated_tuple = my_tuple * 2
print("Повторенный кортеж:", repeated_tuple)

# Подсчет количества вхождений элемента
tuple_with_repeats = (1, 2, 2, 3, 2)
print("Количество двоек:", tuple_with_repeats.count(2))  # 3
print("Индекс первого вхождения 2:", tuple_with_repeats.index(2))  # 1

# Цикл по кортежу
print("Элементы кортежа через цикл:")
for item in my_tuple:
    print(item, end=" ")  # Выводим элементы в строку

# Кортеж как ключ в словаре (хэшируемость)
my_dict = {my_tuple: "value"}
print("\nКортеж как ключ словаря:", my_dict)

# Показываем неизменяемость (раскомментируйте для ошибки)
my_tuple[0] = 100  # TypeError: 'tuple' object does not support item assignment