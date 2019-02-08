# программа берет список артикулов из файла csv и сравнивает артикулы с изображениями в той же папке (изображения названы по артикулам)
# удаляет изображения, которых нет в файле csv, создает таблицу со списком удаленных артикулов


import glob
import os

images=glob.glob("*.jpg")+glob.glob("*.png")
len_images_n = len(images)


i = 0
im = 0

while im < (len_images_n):
    filename = images[i]
    article = filename [0: -4]
    line_drop = 1
    no_file = 1
    f = open('article.csv', 'r')
    for line in f:
        line_art = line
        if article in line:
           line_drop = 0
           no_file = 0
    f.close()
    if line_drop == 1:
       os.remove (filename)
       print (filename, ' removed')
    if no_file == 1:
       print ("работает")
       f2 = open('article1.csv', 'a')
       f2.write (line_art)
       f2.close
    i = i + 1
    im = im + 1
art_number = 0
print ("searching")
f = open('article.csv', 'r')
for line in f:
    art_none = 1
    art_number = 0
    while art_number < len_images_n:
        article = images[art_number]
        if article[0: -4] in line:
            art_none = 0
        art_number = art_number + 1
    if art_none == 1:
        f2 = open('article1.csv', 'a')
        f2.write (line)
        f2.close
f.close()

