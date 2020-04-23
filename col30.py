#Обчислити середнє арифметичне значення тих елементів одновимірного
#масиву, які розташовані за першим по порядку мінімальним елементом.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    Z=np.zeros(5,dtype=int)#ніціалізуєм масив
    for i in range(5):#проходимся по елементам масива
      Z[i] = random.randint(1,100)
    print(Z)
    count=0#щотчик
    a=[]#пустий список
    count1=0
    mini=min(Z)
    for k in range(5):
        if Z[k]==min(Z):
            count=k #шукаємо індекс мінімального числа
    for l in range(5):
        if l>count:#ищем индексы чисел после минимального и добавим их в список
            a.append(Z[l])
    print(a)
    if len(a)==0: #якщо довжина списка 0, тоді це мінісальний елемент
        print('Сума 0')
    else:
        print('Среднє значеня після мінісального',sum(a)/len(a))
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break