# Создаем словарь с информацией о пользователе
user = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "hiking"]
}

# Выводим весь словарь и его длину
print("Исходный словарь:", user)
print("Длина словаря (количество пар):", len(user))

# Доступ к значениям по ключу
print("Имя:", user["name"])  # Прямой доступ
print("Возраст:", user.get("age"))  # Безопасный доступ через get
print("Зарплата (по умолчанию 0):", user.get("salary", 0))  # Ключа нет, возвращается 0

# Добавление новой пары
user["salary"] = 50000
print("После добавления salary:", user)

# Изменение существующего значения
user["age"] = 26
print("После изменения возраста:", user)

# Изменение вложенного списка (значения изменяемы!)
user["hobbies"].append("swimming")
print("После добавления хобби:", user)

# Удаление пары
removed_value = user.pop("city")  # Удаляем и сохраняем значение
print("Удаленное значение:", removed_value)
print("После pop:", user)

# Удаление с помощью del
del user["salary"]
print("После del salary:", user)

# Обход словаря: по ключам
print("Ключи словаря:")
for key in user:
    print(key, "->", user[key])

# Обход словаря: по парам ключ-значение
print("Пары ключ-значение:")
for key, value in user.items():
    print(f"{key}: {value}")

# Обход только значений
print("Только значения:")
for value in user.values():
    print(value)

# Проверка наличия ключа
if "name" in user:
    print("Ключ 'name' найден!")

# Создание словаря с помощью dict comprehension
squares = {x: x**2 for x in range(1, 5)}
print("Словарь квадратов:", squares)

# Слияние словарей (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = dict1 | dict2
print("Слитый словарь:", merged_dict)

# Подсчет элементов с помощью словаря
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print("Подсчет символов:", char_count)

# Очистка словаря
user.clear()
print("После clear:", user)