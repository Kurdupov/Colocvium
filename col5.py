# 5. Створіть масив А [1..7] за допомогою генератора випадкових чисел і
#виведіть його на екран. Збільште всі його елементи в 2 рази.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z = np.zeros(7, dtype=int)  # ініціалізуєм матрицю
    a = []  # пустий список для масиву
    for i in range(7):#проходимся по елементам матриці
      Z[i] = random.randint(0,100)
    print(Z)
    for k in range(7):#проходимся по елементам матриці
      b=Z[k]*2#доножаєм елементи на 2
      a.append(b)#добавляем в список
    print(a)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break