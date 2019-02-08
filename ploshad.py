tip_komnati = input()
pi = 3.14
if tip_komnati == "треугольник":
	a = int(input())
	b = int(input())
	c = int(input())
	p = (a + b + c)/2
	kvadrat = p * (p - a) * (p - b) * (p - c)
	S = kvadrat**0.5
	print (float(S))
elif tip_komnati == "прямоугольник":
	a = int(input())
	b = int(input())
	S = a*b
	print (float(S))
elif tip_komnati == "круг":
	r = int(input())
	S = (pi * (r**2))
	print (float(S))
	