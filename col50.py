#50. У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
#виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
    #Ініціалізуємо 10 виграшних квитків та 10 квитків, що купив користувач.
    Z=np.array([random.randint(1,100) for i in range(10)])
    X=np.array([random.randint(1,100) for i in range(10)])
    flag=False
    for i in range(len(X)): #проходимся по  елементах масиву
        if X[i] in Z: #Перевіряємо на входження
            flag=True
        else:
            flag=False
    if flag==True: #Якщо істина - то виграв
        print(f'білет {X[i]} - виграшний!')
    else:
        print(' У вас немає виграшного квитка(')
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break