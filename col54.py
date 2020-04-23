#Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
#однаковими значеннями.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.zeros(20,dtype=int)#ініціалізуєм масив
    for i in range(20):#проходимся по елементам масива
      Z[i] = random.randint(1,100)#генерируєм значення
    print(sorted(Z))#Виводим і сортіруєм
    v=0
    v=set(Z)#В set.елементине повторюються
    print(v)
    if len(v)<len(Z):
        print('Однакові елементи є')
    else:
        print('Одинакових елементів немає')
        result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
        if result == '1':
            continue
        else:
            break