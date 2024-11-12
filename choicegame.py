"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    # используем для решания задачи алгоритм бинарного поиска
    down = 1   # нижняя граница
    up = 100   # верхняя граница
    while True:
        count += 1   #
        middle = (down + up) // 2   # пытаемся угадать число - среднее значение между верхней и нижней границами
        if number > middle:   # если наше загаданное число больше середины
            down = middle + 1   # то середина становится нижней границей и чтобы сократить число попыток угадывания мы добавляем к числу 1
        elif number < middle:   # если наше загаданное число меньше середины
            up = middle - 1   # то середина становится верхней границей и чтобы сократить число попыток угадывания мы отнимаем от числа 1
        else:
            break   # если число угадали то выходим из цикла
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
