# 25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
#Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
#100.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.zeros(10,dtype=int)#ініціалізуєм матрицю
    count=1#щотчик
    for i in range(10):#проходимся по елементам масиву
      Z[i] = random.randint(10,100)#вводим значення
    print(Z)
    for k in range(10):#проходимся по елементам масиву
      b=Z[k]#елементи в зміну
      if b%5==0:#якщо значения кратні 5
         count*=b#+1
    if count==1:
        print('Таких чисел немає')
    else:
       print('Добуток чисел кратних 5',count)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break