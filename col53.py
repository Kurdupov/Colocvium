#В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
#масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
#п'ятірки. Додаткового масиву не заводити.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
while True:
    Z=np.zeros(10,dtype=int)#ініціалізуєм масив
    for i in range(10):#проходимся по елементам матриці
      Z[i] = int(input('Введіть значення'))#вводим значення
    while Z[i]!=0 and Z[i]!=1 and Z[i]!=5:#якщо елементи не співпадають з0,1і5 водимо заново
      for i in range(10):
          Z[i]=int(input('Введіть значення 0,1 або 5:'))
    print(Z)
    print(sorted(Z))#переставляєм наші елементи
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break