#44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
#своїм номером і при цьому кратні 3.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.array([random.randint(1,25) for i in range(25)])#Генеруємо масив
    print('Масив: ', Z)
    count=0#щотчик
    for i in range(len(Z)): #прохдимся по елементам масиву.
        if Z[i]==i+1 and Z[i]%3==0: #Берем порядковий номер
            count+=1
    print('Кількість елементів що збігаються з порядковим номером і кратні 3 -', count)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break