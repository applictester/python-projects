"""
В математиці комбінація або сполука це спосіб вибору декількох речей з більшої групи, 
де (на відміну від розміщення) порядок не має значення. 
Наприклад, дано три фрукти, яблуко, помаранч і груша, 
існують три сполуки по два фрукти, що можуть бути отримані з цього набору: 
яблуко і груша, яблуко і помаранч, або груша і помаранч.
"""

# This program calculates the number of combinations of n items taken k at a time using recursion.
def C(n, k):
    if k == 0 or k == n:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)


n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))
print(C(n, k))
