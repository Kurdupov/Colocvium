#Задано два натуральних числа a і b. Змінній w привласнити значення
#істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
#і не кратний b.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=int(input('Введіть a: '))
    X=int(input('Введіть b: '))
    C=np.zeros(10,dtype=int)#ініціалізуєм масив
    V=False
    for i in range(10):#проходимся по елементам матриці
      C[i] = random.randint(5,25)#вводим значения
    print(C)
    for k in range(10): #проходимся по елементам матриці
        if C[k]%Z==0 and C[k]%X!=0:
            w=True
    print(V)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break