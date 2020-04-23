#34. Дано два лінійних масиву однакової розмірності. Скласти третій масив з
#добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.array([random.randint(-5,5) for i in range(20)])#Генеруємо масиви
    X=np.array([random.randint(-5,5) for i in range(20)])
    print('Масив Z: ', Z)
    print('Масив X: ', X)
    C=Z*X #перемножаться елементи з однаковими індексами
    print('Результат множення матриць Z та X: ', C)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break
