import time
import lib

val = 0

for i in range(101):

	lib.progress_bar(100, val, 100)
	val += 1
	time.sleep(0.02)

print('\n' + 'press space to exit')
lib.wait_for_input(' ')