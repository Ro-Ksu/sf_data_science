"""Игра "Угадай число"
Компьютер сам устанавливает и угадывает случайное число
"""

import numpy as np

"""Подход 1: Случайное угадывание"""

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    
    return count


"""Подход 2: Угадывание с коррекцией"""

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


"""Подход 3. Бинарный поиск числа"""

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число и задаем min и max даипазона поиска.
    Если загаданное число равняется одной из границ диапазона, прерываем цикл подбора.
    Подбираем число в цикле, каждый раз скоращая диапазон для поиска напополам.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    predict = np.random.randint(1, 101)
    min_predict = 1 # вводим min и max границы диапазона поиска 
    max_predict = 100
    
    while number != predict:
        count += 1
        if number == min_predict:
            count +=1 
            break   # прерываем цикл, если загаданное число равно одной из границ
        elif number == max_predict:
            count += 1
            break 
        elif number > predict:
            min_predict = predict
            predict = (max_predict + predict)//2
        elif number < predict:
            max_predict = predict
            predict = (predict + min_predict)//2
            
    return count


"""Функции для оценки алгоритмов"""

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


# RUN
if __name__ == '__main__':
    score_game()