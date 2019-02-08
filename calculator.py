summa = int(input())
if summa <= 3000:
    print (round(summa - 300)/95*100)
else:
    print (round(summa/95*100))
	
while (True):
	proverka = input('Хотите сделать еще одну ссылку? Да/Нет')
	if proverka == 'Да':
		summa = int(input())
		if summa <= 3000:
			print (round(summa - 300)/95*100)
		else:
			print (round(summa/95*100))
		
	else:
		break