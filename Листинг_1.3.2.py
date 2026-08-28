import datetime

t = datetime.datetime.now()
print("Текущее время :", t) # Импорт модуля datetime и вывод текущей даты и времени

import datetime

d = datetime.date.today()
print("Текущая дата:", d) # текущая дата

import datetime

d = datetime.date.today()
date = d.strftime("%d-%m-%Y")
print("Сегодня ", date) # отформатированная текущая дата

import datetime

d = datetime.date.today()
date = d.strftime("%d %B %Y")
print("Сегодня ", date) # вывод месяца текстом



