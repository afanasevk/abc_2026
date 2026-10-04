# todo: База данных пользователя.
# Задан массив объектов пользователя
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1
#Затем сообщение для ввода
# Ввидите критерии поиска: 16
# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
type_sort = int(input("type_sort(1, 2, 3) = "))
result = []
if type_sort == 1:
    age = int(input("age = "))
    for user in users:
        if user["age"] > age:
            result.append(user)
    result.sort(key=lambda user: user["age"])

elif type_sort == 2:
    result = sorted(users, key=lambda user: user["login"][0])
    
elif type_sort == 3:
    result = sorted(users, key=lambda user: user["group"])

print(result)
