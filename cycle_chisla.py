# программа выводит счетчик от 1 до 100%. Просто красиво и залипательно. Запускать из консоли

import time
import sys

for i in range (1, 101):
	a = print ((str(i)) + "%" + "\b\b\b", end="" )
	sys.stdout.flush()
	time.sleep(0.3) 
	i+=1
	
