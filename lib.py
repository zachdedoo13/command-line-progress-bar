#fuction libary 

import keyboard
import time


def progress_bar(end_val, current_val, length):
    #calc percent and amout of bars
    percent = (current_val / end_val) * 100 
    bars = percent * (length * 0.01)
    #round veriables
    bars = round(bars, 0) 
    percent = round(percent, 1)
    #bar calc
    bar_till_end = length - bars
    #printing
    if current_val >= end_val + 1:
        pass
    else:
        print(
            (("\u2588" * (int(bars) - 1)) + '|') +
            ("_" * int(bar_till_end)) + 
            ("  |" + str(percent)+'%|') +
            ("   " + str(current_val))
            , end='\r'
            )
    #give %
    return percent

def wait_for_input(key_in_quotation):
    i = True
    while i == True:
        if keyboard.is_pressed(key_in_quotation):
              i = False
    time.sleep(0.1)