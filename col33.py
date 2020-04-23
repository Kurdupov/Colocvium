#33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.array([random.randint(-3,3) for i in range(1,20)])#Генеруємо масив
    print('Масив: ', Z)
    count=1
    for i in range(len(Z)): #проходимся по елементів масиву.
        if Z[i]!=0: #Якщо елемент ненулевий
            count*=Z[i]
    print('Добуток усіх ненульових елементів: ', count)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break