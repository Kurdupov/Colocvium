#Змінній t привласнити значення істина, якщо в одновимірному масиві є
#хоча б одне від’ємне і парне число.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.zeros(10,dtype=int)#ініціалізуєм масив
    t=False #присваюєм tзначення False
    for i in range(10):#проходимся по елементам масива
      Z[i] = random.randint(-10,10)
    print(Z)
    for y in range(10):#проходимся по елементам масива
       if Z[y]%2==0 and Z[y]<0: #якщо значення відємне і парне
           t=True
    print(t)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break