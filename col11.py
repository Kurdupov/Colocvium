#11. Дані про температуру води на Чорноморському узбережжі за декаду
#вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
#купання.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    #Генеруємо три декади вересня за допомогою random.
    Z=np.array([random.randint(10,25) for i in range(1,11)])
    X=np.array([random.randint(14,24) for i in range(1,11)])
    C=np.array([random.randint(12,22) for i in range(1,11)])
    count=0 #щотчик
    for i in range(len(Z)): #проходимся по елементам першої декади.
        if 20<=Z[i]<=25: #комфортна температура
           count+=1 #+1
    if 1<=count<=10: #Якщо щотчик!=0,купатись можна
        print(f'Купатися  можна було стільки: {count}.')

    counter=0#щотчик
    for i in range(len(X)):
        if 20<=X[i]<=24:
            counter+=1
    if 1<=counter<=10:
        print(f'Купатися я можна було стільки: {counter}.')

    counterr=0#щотчик
    for i in range(len(C)):
        if 20<=C[i]<=22:
            counterr+=1
    if 1<=counterr<=10:
        print(f'Купатися  можна було стільки: {counterr}.')
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break
    break