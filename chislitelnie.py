year = int(input("Введите Ваш возраст:"))
if year == 111 or year == 112 or year == 113 or year == 114:
    print (f"Тебе {year} лет")
elif year%100 == 11 or year%100 == 12 or year%100 == 13 or year%100 == 14:
    print (f"Тебе {year} лет")
elif year%10 == 2 or year%10 == 3 or year%10 == 4:
    print (f"Тебе {year} года")
elif year == 1 or year > 20 and year%10 == 1:
    print (f"Тебе {year} год")
else:
    print (f"Тебе {year} лет")
