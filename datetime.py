# Дата и время в python. Сколько мне дней сейчас. Когда мне исполнится 15000 дней

from datetime import datetime  
from datetime import timedelta

birthday = datetime(1992, 11, 7)
td = datetime.now() - birthday
print("Мне " + str(td.days) + " дней")

othertd = timedelta(15000)  # создан интервал 15000 дней
newdate = birthday + othertd
print('Мне исполнится 15000 дней ' + str(newdate))



