#3. Створіть масив з 5 прізвищ і виведіть їх на екран стовпчиком,
#починаючи з останнього.

#Курдупов Олексій 122Г
import numpy as np #імпортуємо бібліотеку numpy.
while True:
    Z=np.array(['Гребенюк', 'Дужак', 'Солоненко', 'Заїка', 'Гунько'])#Задаємо прізвища
    X=Z[::-1] #початок прізвищ тепер з кінця
    print('Прізвища: ', Z) #Виведемо прізвища.
    for i in X: #Щоб вивести прізвища стовчиком
        print(i)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break