# 26. Напишіть програму аналізу значень температури хворого за добу:
#визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
#температури виробляються шість раз на добу і результати вводяться з клавіатури у
#масив
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
while True:
    Z=np.array(range(1,25,4))#ініціалізуєм масив
    count=0
    for i in range(len(Z)):#проходимся по елементам масива
      Z[i] = float(input('Введіть температуру'))#Вводим температуру
      count+=Z[i]/len(Z)#середнє значення
    print(Z)
    print('Средня температура',count)
    min=min(Z)#мінімальне та максемальне значення
    max=max(Z)
    print('Мінімальна',min,'Максимальна',max)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break