#Змінній t привласнити значення істина, якщо максимальний елемент
#одновимірного масиву єдиний і не перевищує наперед заданого числа а.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
while True:
    Z=int(input('Введите ваше число:'))
    X=np.zeros(5,dtype=int)#ініціалізуєм масив
    count=0
    for i in range(5):#проходимся по елементам масиву
      X[i] = int(input('Введите значение'))#вводим значення
    print(X)
    maxim=max(X) #шукаєм максимальне значення
    t=False
    for y in range(5):#проходимся по елементам масиву
      if X[y]==maxim: #провіряєм кожен елемент чивін дорівнює максимальному
          count+=1#+1
          if count>1 or maxim>Z:#якшозначення щотчика більше 1
              t=False
          else:
              t=True
    print(t)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break