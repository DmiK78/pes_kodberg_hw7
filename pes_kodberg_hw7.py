# task 1 Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

given_list = [65, 34, 7, 32, 18, 5, 90]

def rev_generator():
    i = 1
    for _ in given_list:
        yield given_list[-i]
        i += 1

rev_gen = [i for i in rev_generator()]
print(rev_gen)

# task 2 Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл

given_list = [4, 23, 57, 6, 8, 325, 100]
gen_list = []

def sqr_generator():
    for x in given_list:
        if x % 2 == 0:
            yield x ** 2

gen_list = [i for i in sqr_generator()]
print(gen_list)

# task 3 Напишіть функцію-генератор для отримання n перших простих чисел.

'''НЕ ДОРОБЛЕНО'''

def simple_num_gen():
    for x in range(1,1000):
        if x % 2 != 0:
            yield x

n_gen = [i for i in simple_num_gen()]
print(n_gen)
