# Сортировка массива 10 случайных цифр подсчетом 


# создание случайного массиива из 10 случайных цифр 
from random import randint
mass_A = []
for i in range(10) :
    mass_A.append(randint(0, 9))
print('Исходный массив: ', mass_A)

# частотный анализ массива
F = [0]*10
for i in range(10) : 
    F[mass_A[i]] += 1

# вывод результата
mass_B = [] 
for i in range(10) :
    for j in range(F[i]) :
        mass_B.append(i)
print("Упорядоченный массив: ", mass_B) 
