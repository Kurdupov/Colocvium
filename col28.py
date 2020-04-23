# 28. Знайти кількість парних елементів одновимірного масиву.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.zeros(10,dtype=int)#ініціалізуєм масив
    count=0#щотчик
    for i in range(10):#проходимся по елементам масива
      Z[i] = random.randint(-10,10)
    print(Z)
    for k in range(10):#проходимся по елементам масива
       if Z[k]%2==0: #якщоділяться на 2
           count+=1#+1
    print('Кількість парних елементів',count)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break