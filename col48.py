# 48. Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
# місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
# з початку і третього від кінця і т.д.
#Курдупов Олексій 122Г
import numpy as np #імпортуємо Бібліотеку numpy .
while True:
    Z = np.array([input('Введіть прізвище брокера: ') for i in range(6)])# введеня даних
    print('Прізвища брокерів: ', Z)
    X = Z[::-1] #використовуємо зріз
    print('Новий список: ', X)
    result = input('Хочите продовжити ? Якщо да - 1, Якщо нет - інше: ')
    if result == '1':
        continue
    else:
        break
