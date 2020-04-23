#Розсортуйте заданий лінійний масив по зростанню.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
import random #імпортуємо random
while True:
  Z=int(input('Введіть кількість цифр '))
  X=np.zeros(Z,dtype=int) #робим масив
  for i in range(Z):#проходим по списку
   X[i]=random.randint(0,10000)
  print(X)
  n=len(X)
  for i in range(1,n): #сортування бульбашковим методом
      for y in range(n-1,i-1,-1):
            if (X[y-1]>X[y]):
                X[y],X[y-1]=X[y-1],X[y]
  print(Z)
  result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
  if result == '1':
      continue
  else:
      break