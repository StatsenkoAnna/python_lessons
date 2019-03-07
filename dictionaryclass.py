import os
	
# программа на классах

class Dictionary:
	en_ru = {}
	def fill_my_dict(self):
		slovo = input("Введите слово на английском языке ")
		if slovo in self.en_ru:
			print("Такое слово уже есть в словаре.") # Оно переводится как ".format(en_ru.get(slovo)))
		else:
			znach = input ("Введите значение на русском ")
			self.en_ru[slovo] = znach
	
	def test_user(self):
		errors = 0
		
		for key, value in self.en_ru.items():
			answer = input("Введите перевод слова {} ".format(key))
			if answer != value:
				errors += 1
			test_en_ru = input("Еще одно? Да/Нет ")
			if test_en_ru != "Да":
				break
		print("Количество ошибок: {}".format(errors))
		return errors

	def test_user_back(self):
		errors = 0
		for key, value in self.en_ru.items():
			answer = input("Введите перевод слова {} ".format(value))
			if answer != key:
				errors += 1
			test_ru_en = input("Еще одно? Да/Нет ")
			if test_en_ru != "Да":
				break
		print("Количество ошибок: {}".format(errors))
		return errors
		
	

# Основная часть программы

# Добавление слов в словарь
d = Dictionary()
while(True):
    slovar = input("Хотите добавить слово в словарь? Да/Нет ")
    if slovar == "Да":
        d.fill_my_dict()
    else:
        break

# Перевод с английского - тест, в результате выдает кол-во ошибок
test_en_ru = input("Хотите перевести слова с английского? Да/Нет")
if test_en_ru == "Да":
    d.test_user()

# Перевод с русского - тест, в результате выдает кол-во ошибок
test_ru_en = input("Хотите перевести слова с русского? Да/Нет")
if test_ru_en == "Да":
    d.test_user_back()
