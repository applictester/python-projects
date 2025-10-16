import random

def petro_place_in_line(heights, petro_height):
    position = 1
    for h in heights:
        if h >= petro_height:
            position += 1
    return position


n = int(input("Введіть кількість людей у строю: "))
# Генеруємо список зросту учнів 
heights = [random.randint(140, 200) for _ in range(n)]

print("Зріст учнів:", heights)
petro_height = int(input("Введіть зріст Петра: "))
place = petro_place_in_line(heights, petro_height)
print(f"Петро повинен стати під номером: {place}")