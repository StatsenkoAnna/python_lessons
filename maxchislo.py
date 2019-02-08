a = int(input())
b = int(input())
c = int(input())



m = a
if b > m:
	m = b
if c > m:
	m = c
print (m) #нашли самое большое число и вывели его на экран
	
k = a

if b < k:
	k = b
if c < k:
	k = c
print (k) #нашли самое маленькое число и вывели его на экран
	
l = (a+b+c) - (m+k)
print (l)
