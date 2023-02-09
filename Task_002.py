# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
n = int(input('Введите размер списка: ')) # Объявляем переменную - приглашение пользователю ввести размер списка
list_1 =[] # Объявляем список
for i in range(n): # Объявляем цикл заполнения списка
    list_1.append(randint(1, n)) # Заполненяем список числами от 1 до 10
user_list_1 = set(list_1) # Упорядочиваем список, исключаем повторяющиеся элементы
print(*user_list_1) # Выводим заполненный список на консоль
x = int(input('Введите искомое число: ')) # Объявляем переменную - приглашение пользователю ввести искомое число
ans = 0
if x > max(user_list_1):
    print('->', max(user_list_1))
elif x < min(user_list_1):
    print('->', min(user_list_1))
else:
    while True:
        if x - ans in user_list_1 and x + ans in user_list_1 and x - ans != x + ans:
            print('->', x - ans, ';', x + ans)
            break
        elif x - ans in user_list_1:
            print('->', x - ans)
            break
        elif x + ans in user_list_1:
            print('->', x + ans)
            break
        else:
            ans += 1
