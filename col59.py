#Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
#чисел в ньому.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.zeros(10,dtype=int)#ініціалізуєм масив
    for i in range(10):#проходимся по елементам матриці
      Z[i] = random.randint(5,25)# генеруєм значння
    print(Z)
    print('Різних чисел в масиві',len(set(Z)))#за допомогою set шукаєм повторювальні елементи
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break