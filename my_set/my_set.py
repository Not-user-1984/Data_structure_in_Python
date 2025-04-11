# Создаем множество с разными типами данных
my_set = {1, "Python", 3.14, (1, 2)}
print("Исходное множество:", my_set)

# Создаем множество из списка с дубликатами (дубликаты удаляются)
list_with_duplicates = [1, 2, 2, 3, 3, 4]
unique_set = set(list_with_duplicates)
print("Множество из списка (без дубликатов):", unique_set)

# Пустое множество
empty_set = set()
print("Пустое множество:", empty_set)

# Добавление элементов
my_set.add(42)  # Добавляем один элемент
print("После add(42):", my_set)

my_set.update(["new", 100])  # Добавляем несколько элементов
print("После update(['new', 100]):", my_set)

# Удаление элементов
my_set.remove("Python")  # Удаляем элемент
print("После remove('Python'):", my_set)

my_set.discard("nonexistent")  # Удаляем несуществующий элемент (без ошибки)
print("После discard('nonexistent'):", my_set)

popped_element = my_set.pop()  # Удаляем и возвращаем случайный элемент
print("Удаленный элемент (pop):", popped_element)
print("После pop:", my_set)

# Операции над множествами
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Объединение
union_set = set1 | set2
print("Объединение (set1 | set2):", union_set)

# Пересечение
intersection_set = set1 & set2
print("Пересечение (set1 & set2):", intersection_set)

# Разность
difference_set = set1 - set2
print("Разность (set1 - set2):", difference_set)

# Симметричная разность
symmetric_diff = set1 ^ set2
print("Симметричная разность (set1 ^ set2):", symmetric_diff)

# Проверка подмножества и надмножества
print("set1.issubset({1, 2, 3, 4, 5}):", set1.issubset({1, 2, 3, 4, 5}))  # True
print("set1.issuperset({1, 2}):", set1.issuperset({1, 2}))  # True

# Проверка наличия элемента
if 3 in set1:
    print("Элемент 3 есть в set1")

# Цикл по множеству
print("Элементы множества set1:")
for item in set1:
    print(item, end=" ")

# Работа с frozenset (неизменяемое множество)
frozen = frozenset([1, 2, 3])
print("\nFrozenset:", frozen)
# frozen.add(4)  # Ошибка: frozenset неизменяем

# Использование frozenset как ключа в словаре (хэшируемость)
my_dict = {frozen: "value"}
print("Frozenset как ключ словаря:", my_dict)

# Очистка множества
set1.clear()
print("После clear (set1):", set1)


# Пример: удаление дубликатов из списка с сохранением порядка
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


original_list = [1, 2, 2, 3, 1, 4]
unique_list = remove_duplicates_preserve_order(original_list)
print("Удаление дубликатов с сохранением порядка:", unique_list)
