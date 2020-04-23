#20. Знайти суму всіх елементів масиву дійсних чисел, більших за задане
#число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
#від 50 до 100.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    while True:
        Z=np.array([random.uniform(50,100) for i in range(20)])#Генеруємо масив
        print('Масив: ', Z) #Виведемо
        try:
            a=int(input('Задайте число до 100: '))
        except ValueError:
            print('Ведіть число  ')
            break
        count=0#щотчик
        for i in range(len(Z)):
            if Z[i]>a: #Якщо елемент,більший
                count+=Z[i] # додаємо у щотчик.
        print(f' сума чисел, більших від {a}.')
        if count==0:
            print(f'Немає чисел у масиві більших ніж {a}.')
        else:
            print(f'Сума чисел які більші ніж {a} буде {count}.')
        result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
        if result == '1':
            continue
        else:
            break