import time
import sys

for i in range (1, 101):
	a = print ((str(i)) + "%" + "\b\b\b", end="" )
	sys.stdout.flush()
	time.sleep(0.3) 
	i+=1
	