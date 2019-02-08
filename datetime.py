# Дата и время в python

from datetime import datetime  # сократит путь к классу
from datetime import timedelta

# РАЗНИЦА в датах измеряется в ДНЯХ и СЕКУНДАХ.
# нет понятия "МЕСЯЦ" или "ГОД", потому что их длина варьируется

# 1970-01-01 - начало UNIX-эпохи
                    #  Y  M  D  [h [m [s]]]
birthday = datetime(1992, 11, 7)
td = datetime.now() - birthday
print("Мне " + str(td.days) + " дней")

othertd = timedelta(15000)  # создан интервал 15000 дней
newdate = birthday + othertd
print('Мне исполнится 15000 дней ' + str(newdate))

# Посчитать, когда вам исполнится 15000 дней
# узнать, сколько это будет полных лет


