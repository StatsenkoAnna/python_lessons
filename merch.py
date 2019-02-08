# из двух файлов программа создает третий файл, куда записывает 8 значений из первого и одно значение из второго. Делалось для расположения
# товаров на сайте интернет-магазина

import io


file_vitrinniy = open ('vitrinnie.csv', 'r') # Открываем файл для чтения
file_obichniy = open ('obichniy.csv', 'r')
vitrina = file_vitrinniy.readlines() # Читаем
obichniy = file_obichniy.readlines() # Читаем
file_vitrinniy.close() # Закрываем файл для чтения
file_obichniy.close() # Закрываем файл для чтения
file_out = open ('merch-potolok.csv', 'a') # Определяем файл, куда писать будем. Чтобы ничего не уработать раньше времени.

a = len(vitrina) + len(obichniy)

j = 1
ob = 0
vi = 0
i = 0
while i <= a:
    if j != 8:
        file_out.write(obichniy[ob])
        ob = ob + 1
        j = j + 1
    else:
        file_out.write(vitrina[vi])
        vi = vi + 1
        j = 1
    i = i + 1
file_out.close

