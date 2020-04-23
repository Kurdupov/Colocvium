#13. Створіть масив з 15 цілочисельних елементів і визначте серед них
#мінімальне значення.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.array([random.randint(-15,25) for i in range(1,15)])#Генеруємо масив Z.
    print('Масив: ', Z) #Виводим
    print('Мінімальне значення: ', min(Z)) #Мінімальне значення масиву
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break
