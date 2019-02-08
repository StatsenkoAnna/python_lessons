age = int(input("Введите Ваш возраст:"))
if 0 <= age <= 3:
    print ("дома")
if 4 <= age <= 6:
    print ("садик")
if 7 <= age <= 17:
    print ("школа")
if 18 <= age <= 22:
    print ("ВУЗ")
if 23 <= age <= 25:
    print ("аспирантура")
if 26 <= age <= 60:
    print ("работа")
if age > 60:
    print ("пенсия")

else:
	print("Вы ввели неверное значение")