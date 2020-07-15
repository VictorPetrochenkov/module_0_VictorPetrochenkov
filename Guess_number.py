import numpy as np  # Загружаем библиотеку numpe. Присваиваем ей значение np

rezult = 0 # Вводим переменную в которой будет формироваться результат согласно  задания
# вместо 0 будут вноситься значения счётчика полученные в результате
# отгадывания задуманного числа
for i in range(0,1000): # Задаём цикл для получения значений счётчика. Результат каждой
    # итерации i от 0 до 1000 будут заноситься в список result
    min_num = 1 # Задаём минимальное значение диапазона в котором загадывается число
    max_num = 100 # Задаём максиальное значение диапазона в котором загадывается число
    number = np.random.randint(min_num, max_num + 1) # загадываем число
    count = 1 # Задаём начальное значение счётчика
    numer_guess = np.random.randint(min_num, max_num + 1) # Угадываем число первый раз
    while numer_guess != number: # Организуем цикл угадывания числа в изменяемом диапазоне,
        # диапазон изменяется на осоновании сообщения больше или меньше
        # угадываемое число относительно загаданного.
        count+=1 # Увеличиваем значение счётчика в процессе неудачного угадывания числа
        if numer_guess < number: # Проверяем угадываемое число на условие больше\меньше относительно загаданного,
            # в зависимости от условия, перераспределяем границы, новую нижнюю и верхнюю границу генерации угадываемого числа
            min_num = numer_guess + 1
        else:
            max_num = numer_guess - 1
        numer_guess = np.random.randint(min_num, max_num + 1)
    rezult+= count # Вносим значение счётчика в список
rezult = rezult/1000 # Определяем среднее значение количества этапов необходимых
# для угадывания заданного числа согласно этого алгоритма
print(rezult) # Выводим на экран результат
