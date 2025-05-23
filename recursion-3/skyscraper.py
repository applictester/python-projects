def min_drops(n):
    """
    Функція для обчислення мінімальної кількості скидань,
    необхідних для визначення критичного поверху за допомогою двох скляних куль.
    """
    if n <= 2:
        return n
    return n // 2


def recursive_try(count, n):
    """
    Рекурсивна функція для імітації скидання куль.
    """
    if count >= n // 2:
        return count
    return recursive_try(count + 1, n)


try:
    n = int(input("Введіть кількість поверхів хмарочоса: "))
    if n <= 0:
        print("Кількість поверхів має бути додатнім числом.")
    else:
        print(f"Мінімальна кількість скидань для {n} поверхів: {recursive_try(1, n)}")
        print(f"Перевірка: Мінімальна кількість скидань для {n} поверхів: {min_drops(n)}")
except ValueError:
    print("Будь ласка, введіть коректне ціле число.")
