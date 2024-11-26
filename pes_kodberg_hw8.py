# task 1 Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
# Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.

import os
import random

PATH = os.path.abspath(__file__ + '/..')

numbers_list = []

for x in range(1,100000):
    x = str(random.randint(1,10000))
    numbers_list.append(x)
    while len(numbers_list) == 10000:
        break
# print(numbers_list)

with open(os.path.join(PATH,"task1.txt"),'w') as f:
    f.write(','.join(numbers_list))

with open(os.path.join(PATH,"task1.txt"), 'r') as f:
    numbers_from_file = f.read().split(',')
    amount = sum(map(int, numbers_from_file))

print(f'The sum from the file = {amount}')

# task 2 Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так,
# щоб він зберігав базу посилань на диску і не «забув» при перезапуску. За бажанням можете ознайомитися з модулем shelve (https://docs.python.org/3/library/shelve.html),
# який у даному випадку буде дуже зручним та спростить виконання завдання.
# ДЗ 7: Створіть програму, яка емулює роботу сервісу зі скорочення посилань.
# Повинна бути реалізована можливість введення початкового посилання та короткої назви і отримання початкового посилання за її назвою.

import os

PATH = os.path.abspath(__file__ + '/..')

pib = input("Введіть Ваше ПІБ: ")
pib_list = pib.split(' ')
print(pib_list)

data_pib = {
    'surname': pib_list[0],
    'name': pib_list[1],
    'father_name': pib_list[2]
}

name = input("Введіть Ваше ім'я, прізвище або по-батькові: ")
if name == pib_list[0] or name == pib_list[1] or name == pib_list[2]:
    print(data_pib['surname'], data_pib['name'], data_pib['father_name'])

with open(os.path.join(PATH, 'task2.txt'), 'w') as f:
    f.write(','.join(pib_list))

with open(os.path.join(PATH, "task2.txt"), 'r') as f:
    from_file = f.read().split(',')
    print(from_file)

# task 3 Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.

import os
import json

PATH = os.path.abspath(__file__ + '/..')

internet_shop = [
    {
        "mobile phone": "iPhone 16",
        "laptop": "ASUS",
        "tv set": "Samsung",
        "fridge": "Siemens"
    }
]

with open("internet_shop.json", 'w') as f:
    json.dump(internet_shop, f, indent=4, ensure_ascii=False)

with open("internet_shop", 'r') as f:
    data = json.load(f)

print(data)
# # ______________________________________________________________

import os
import pickle

PATH = os.path.abspath(__file__ + '/..')

internet_shop = [
    {
        "mobile phone": "iPhone 16",
        "laptop": "ASUS",
        "tv set": "Samsung",
        "fridge": "Siemens"
    }
]

with open("internet_shop.json", 'wb') as f:
    pickle.dump(internet_shop, f)

with open("internet_shop.pkl", 'rb') as f:
    data = pickle.load(f)

print(data)
