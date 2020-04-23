#12. Дані про температуру повітря за декаду грудня зберігаються в масиві.
#Визначити, скільки раз температура була вище середньої за цю декаду.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    #Генеруємо наші три декади грудня.
    Z=np.array([random.randint(-5,8) for i in range(1,11)])
    X=np.array([random.randint(-10,5) for i in range(1,11)])
    C=np.array([random.randint(-20,-3) for i in range(1,12)])
    print(f'Середнє значення 1 декади: {np.mean(Z)}')
    print(f'Середнє значення 2 декади: {np.mean(X)}')
    print(f'Середнє значення 3 декади: {np.mean(C)}')
    count=0#щотчик
    for i in range(len(Z)): #проходимся по елементам.
        if np.mean(Z)<Z[i]: #Перевірка чи темп.вища за середню
            count+=1 #Якщо умова True, то лічильник +1.
    print(f'Температура за 1 декаду була вищою за середню стількираз : {count}.')
    count1=0
    for i in range(len(X)):
        if np.mean(X)<X[i]:
            count1+=1
    print(f'Температура за 2 декаду була вищою за середню стількираз: {count1}.')
    count2=0
    for i in range(len(C)):
        if np.mean(C)<C[i]:
            count2+=1
    print(f'Температура за 3 декаду була вищою за середню стількираз: {count2}.')
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break
