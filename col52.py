#Знайти найбільший елемент з елементів одновимірного масиву, що мають
#парний номер. Визначити, чи є він єдиним.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
while True:
    Z=np.zeros(10,dtype=int)#ініціалізуєм масив
    for i in range(10):#проходимся по елементам матриці
      Z[i] = int(input('ведіть значення'))#вводим значення
    print(Z)
    a=[]
    c=0
    for y in range(10):#Проходимся по значениям матриці
        if Z[y]%2==0:#якщо елемент парний +1
         a.append(Z[y])
    c=sorted(a)#сортіруєм список
    print(c)
    if c[-1]==c[-2]:#якщо останій елемент відсортованого списка дорівнює передостаньому то цей елемень не один
         print('Максимальний елемент: ',c[-1],'Не єдиний')
    else:
        print('Максимальний елемент: ',c[-1],'Єдиний')
        result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
        if result == '1':
            continue
        else:
            break