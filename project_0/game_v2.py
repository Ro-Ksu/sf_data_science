"""Guess the number vol. 2
Computer setting and guessing the number by itself
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): Set number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # set number
        if number == predict_number:
            break # exit loop if guess is correct
    return(count)

print(f"Number of tries: {random_predict()}")

def score_game(random_predict) -> int:
    """Mean number of tries in 1000 guesses

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: mean number of tries
    """
    count_ls = [] # list for keeping number of guesses
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # set number list
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # calculating mean number of tries
    
    print(f"Your algorithm's mean number of guesses: {score}")
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)