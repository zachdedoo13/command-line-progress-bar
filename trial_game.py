#makeing a game

#player must press enter when the progress bar is at the pointer 

import os
import lib
import keyboard
import time
import random
import termcolor

os.system('cls')
       
while True:   

    time.sleep(0.2)

    progress = 0 
    running = True
    length = random.randint(40, 60)

    print((" " * length) + termcolor.colored("|    |  |▼|  |    |", 'yellow'))

    length += 11

    while running == True:

        lib.progress_bar(100, progress, 100)

        if keyboard.is_pressed(' '):
            running = False 
        
        progress += 1
        time.sleep(0.01)

    score = 1
    top = 4
    mid = 6
    low = 100

    if (progress >= length - score) and (progress <= length + score):    
        print('\n', 'noice')

    elif (progress >= length - top) and (progress <= length + top) :
        print('\n', 'ok')

    elif (progress >= length - mid) and (progress <= length + mid) :
        print('\n', 'fine')

    else:
        print('\n', 'shit')


    print(str(length))

    time.sleep(0.1)
    
    lib.wait_for_input('space')

    os.system('cls')           