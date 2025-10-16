import random

def is_in_list_check(lst, num):
    return num in lst

def first_index_check(lst, num):
    try:
        return lst.index(num)
    except ValueError:
        return -1

def is_in_list(lst, num):
    for item in lst:
        if item == num:
            return True
    return False

def first_index(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i
    return -1

n = int(input("Введіть кількість елементів списку: "))
lst = [random.randint(0, 100) for _ in range(n)]
print("Згенерований список:", lst)

num = int(input("Введіть ціле число від 0 до 100: "))

print("Число є у списку?" , is_in_list(lst, num))
print("Переврка: Число є у списку?", is_in_list_check(lst, num))

print("Індекс першого входження:", first_index(lst, num))
print("Переврка: Індекс першого входження:", first_index_check(lst, num))
