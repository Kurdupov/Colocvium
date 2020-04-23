# 10. Дані про температуру повітря за декаду листопада зберігаються в масиві.
# Визначити, скільки разів температура опускалася нижче -10 градусів.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    # Генеруємо три декади листопада за допомогою random.
    Z = np.array([random.randint(-15, 5) for i in range(1, 11)])
    X = np.array([random.randint(-18, 5) for i in range(1, 11)])
    C = np.array([random.randint(-20, 5) for i in range(1, 11)])
    count = 0  # щотчик
    for i in range(len(Z)):  # проходимся посписку
        if Z[i] < -10:  #якщо температура менше -10.
            count += 1  # +1
    print(f'За 1 декаду лиситопада температура  -10 була {count} разів.')

    count1 = 0  # щотчик для 2 декади
    for i in range(len(X)):  # проходимся посписку
        if X[i] < -10:
            count1 += 1
    print(f'За 2 декаду лиситопада температура  -10 була {count} разів.')

    count2 = 0 # щотчик для 3 декади
    for i in range(len(C)):  # проходимся посписку
        if C[i] < -10:
            count2 += 1
    print(f'За 3 декаду лиситопада температура  -10 була {count} разів.')
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break

