# coding: utf-8
import io
import datetime
import sys

file_search = open(sys.argv[1], 'r', encoding="utf-8") # Открываем файл для чтения
file_out = open ('regenbogen-zakazi.csv', 'a') # Определяем файл, куда писать будем. Чтобы ничего не уработать раньше времени.
dtfrom = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d_%H:%M")  # datetime.datetime(2018, 12, 29)
dttill = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d_%H:%M")  # datetime.datetime(2019, 1, 1)
separator = sys.argv[4]
dt_position = int(sys.argv[5])
file_out.write(file_search.readline())
for line in file_search: # Для всего массива, что мы считали в file_search пробегаемся построчно:
    values = line.split(separator)
    if len(values) < dt_position + 1:
        continue
    dt = values[dt_position]
    try:
        dt = datetime.datetime.strptime(dt, "%d.%m.%Y %H:%M")
    except Exception as e:
        print("%s couldn't be converted to a date (%s)" % (
            dt, e
        ))
    else:
        if dtfrom <= dt <= dttill:
            print(line)
            file_out.write(line)
	# if '29.12.2018' in line or '30.12.2018' in line or '31.12.2018' in line or '01.01.2019' in line:
	#	file_out.write(line)

file_out.close()  # close - это функция! Нужны круглые скобки!

# Номер;Дата поступления;Скидка по заказу;Цена доставки;Сумма;Клиент;E-mail клиента;Телефон клиента;Город
# 0;11.09.2018 09:56;;0;31130;Заказ с витрины;Yarkina1966@mail.ru;7-903-283-57-88;
# 0;11.09.2018 09:58;;0;18490;Заказ с витрины;Yarkina1966@mail.ru;7-903-283-57-88;
# 0;11.09.2018 11:59;;0;7350;Заказ с витрины;zateeva_anna@mail.ru;8-921-746-66-19;
# 0;11.09.2018 13:28;;0;2200;Заказ с витрины;julianka_13@mail.ru;8-916-026-10-27;
# 0;11.09.2018 17:30;;0;2570;Заказ с витрины;miles69@mail.ru;7-965-115-81-16;
# 0;11.09.2018 21:49;;0;14800;Заказ с витрины;bmkur@mail.ru;7-926-661-41-66;
# 0;11.09.2018 23:44;;0;26830;Заказ с витрины;Evblinova@yahoo.com;8-985-905-22-22;
# 0;12.09.2018 06:25;;0;14790;Заказ с витрины;978899@mail.ru;8-922-068-00-21;
# 0;12.09.2018 08:36;;0;8750;Заказ с витрины;alievalara@mail.ru;8-999-211-50-26;
