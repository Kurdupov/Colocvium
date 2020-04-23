#Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
#спаданню.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
while True:
    Z=np.zeros(5,dtype=int)#ініціалізуєм матрицю
    a=[]
    for i in range(5):#проходимся по елементам матриці
      Z[i] = int(input(''))
      a.append(Z[i])  #Добавляем наш масив в список
      a.sort(reverse=True)#cортіруєм по убиванію
    print(Z)
    print('Відсортований масив',u)
    t=False
    for y in range(5):
        if a[y]!=Z[y]:# якшо елементи масива не рівні впорядковуєм задопомогою списка
          t=False
          break
        else:
          t=True
    print(t)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break