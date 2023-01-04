"""Guess the number"""

import numpy as np

number = np.random.randint(1, 101) # setting the number

count = 0

while True:
    count+=1
    predict_number = int(input("Guess the number from 1 to 100"))
    
    if predict_number > number:
        print("Number should be smaller")
    
    elif predict_number < number:
        print("Number should be bigger")
    
    else:
        print(f"Your guess is correct! It's number {number} in {count} times")
        break # end of game, exit loop
