#Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
#за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
while True:
   z = int(input("Введіть кількість послуг: "))
   a = np.zeros(z,dtype=object)#ніціалізуєм масив
   b = np.zeros(z,dtype=int)
   for i in range(z):#проходимся по списку
    a[i] = input("Введіть послугу: ")
    b[i] = int(input("Введіть ціну: "))
   print(a)
   print(b)
   usluga=0#щотчик
   count=0
   X= int(input("Введіть ціну X: "))
   for i in range(z):
     if X == b[i]:#якщо елемент дорівнює цініто всі інші удаляєм з 2 таблиці
        poslug = a[i:]
        count = b[i:]
   print(usluga)
   print(count)
   result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
   if result == '1':
       continue
   else:
       break