import os

en_ru = {}

def fill_my_dict(en_ru):
    try:
        slovo = input("Введите слово на английском языке ")
    except TypeError:
        slovo = input("Это не слово. Введите слово на английском языке ")
    if slovo in en_ru:
        print("Такое слово уже есть в словаре.") # Оно переводится как ".format(en_ru.get(slovo)))
    else:
        znach = input ("Введите значение на русском ")
        en_ru[slovo] = znach
    return en_ru

                    # for k, v in d.items():
                        # print(k, v)

def test_user(en_ru):
    errors = 0
    for key, value in en_ru.items():
        try:
            answer = input("Введите перевод слова {} ".format(key))
        except TypeError:
            answer = input("Это не слово. Введите слово ")
        if answer != value:
            errors += 1
        test_en_ru = input("Еще одно? Да/Нет ")
        if test_en_ru != "Да":
            break
    print("Количество ошибок: {}".format(errors))
    return errors
    
def test_user_back(en_ru):
    errors = 0
    for key, value in en_ru.items():
        try:
            answer = input("Введите перевод слова {} ".format(value))
        except TypeError:
            answer = input("Это не слово. Введите слово ")
        if answer != key:
            errors += 1
        test_ru_en = input("Еще одно? Да/Нет ")
        if test_en_ru != "Да":
            break
    print("Количество ошибок: {}".format(errors))
    return errors

def save_dict(en_ru):
    result = open("mydict.txt", "w")
    result.write("en_ru = %s" % en_ru)
    result.close()


# Основная часть программы

# Добавление слов в словарь
while(True):
    slovar = input("Хотите добавить слово в словарь? Да/Нет ")
    if slovar == "Да":
        fill_my_dict(en_ru)
    else:
        break

# Перевод с английского - тест, в результате выдает кол-во ошибок
test_en_ru = input("Хотите перевести слова с английского? Да/Нет")
if test_en_ru == "Да":
    test_user(en_ru)

# Перевод с русского - тест, в результате выдает кол-во ошибок
test_ru_en = input("Хотите перевести слова с русского? Да/Нет")
if test_ru_en == "Да":
    test_user_back(en_ru)

