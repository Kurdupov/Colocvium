# 24. Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
#одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
#числами від 500 до 1000.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.zeros(30,dtype=int)#ініціалізуєм матрицю
    count=0#щотчик
    for i in range(30):#проходимся по елементам матриці
      Z[i] = random.randint(500,1000)#вводим значения
    print(Z)
    for k in range(30):#проходимся по матриці
      b=Z[k]#елементи в зміну
      if b%5==0 and b%8==0: #якщо значения кратні 5 і 8
         count+=b#+1
    if count==0:
        print('Таких чисел немає')
    else:
       print('Cумма чисел кратних 5 і 8',count)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break