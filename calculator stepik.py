def sum (a, b):
	return (a + b)

def raznost (a, b):
	return (a - b)

def multiply (a, b):
	return (a*b)

def delenie (a, b):
	return (a/b)

def mod (a, b):
	return (a%b)
	
def pow (a, b):
	return (a**b)

def div (a, b):
	return (a//b)
	
A = float(input()) #ввести первое число
B = float(input()) #ввести второе число
operation = (input())

if operation == "+":
	print (sum(A, B))
elif operation == "-":
	print (raznost(A, B))
elif operation == "*":
	print (multiply(A, B))
elif operation == "/":
	if B != 0:
		print (delenie(A, B))
	else:
		print ("Деление на 0!")
elif operation == "mod":
	if B != 0:
		print (mod(A, B))
	else:
		print ("Деление на 0!")
elif operation == "pow":
	print (pow(A, B))
elif operation == "div":
	if B != 0:
		print (div(A, B))
	else:
		print ("Деление на 0!")
else:
	print ("Вы ввели неверную операцию. Попробуйте еще раз")
	
c = input ("press enter to exit")