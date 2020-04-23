#22. Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
#Заповнення масиву здійснити випадковими числами від 5 до 500.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.array([random.randint(5,500) for i in range(10)])#Генеруємо масив
    print('Масив: ', Z)

    count=1 #щотчик = 1, щоб при множенні отримувати добуток чисел.
    for i in range(len(Z)): #проходим по елементам масиву.
        if Z[i]%3==0 and Z[i]%9==0: #Якщо число кратне 3 і 9, то :
            count*=Z[i] #Множимо його у щотчик
            print(f'Числа, кратні 3 та 9 - {Z[i]}.')
    if count==1: #Якщо щотчикдорівнює 1, кратних чисел немає
        print('У масиві немає чисел, кратних 3 і 9.')
    else:
        print('Добуток елементів масиву, які кратні 3 та 9: ',count)
        result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
        if result == '1':
            continue
        else:
            break