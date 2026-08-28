from datetime import datetime, date, time, timedelta

d = date(2012, 10, 25)
# print(d) # выводит в международном формате
# print(d, type(d)) # меняется класс и тип - дата для даты, тайм для времени
t = time(12, 15, 17)
# print(t, type(t))
# dt = d + t # неправильно так делать, не работет!
dt = datetime.combine(d, t)
# print(dt, type(dt))
# print(datetime.now().replace(microsecond=0)) # получить текущее время. Или естудей вместо нау
# dtt = datetime.now()
# dtt = dtt.replace(hour=12, minute=12, second=0, microsecond=0, year = 2025, month = 1, day = 1) # устанавливаем часы, минуты, секунды, микросекунды
# print(dtt) #присвоили дату, время год
# dat = input('Введите дату (дд.мм.гггг):')
# date_ = datetime.strptime(dat, '%d.%m.%Y') # переводим введенное значение в дату время
# print(date_)
dt = datetime.now()
d = dt.timetuple()
print(d)

# for i in d:
#     print(i)
# print(dt.weekday()) # номер даты от 1, в календаре чаще викдэй
# print(dt.isoweekday()) # номер даты от 0
# cc = dt.isocalendar()
# print(cc)
# print(dt.strftime("%A %d %Y %B %H:%M:%S")) #а - следующий день за текущим
# # маленький игрек - сокращенно год 2 цифры, большой - весь год
# print(dt.strftime("%A %d %Y %B %X"))# % X выводит текущее время
# days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
# print(days[dt.weekday()]) # вытаскиваем дату на русском по индексу


# dat = input('Введите дату (дд.мм.гггг):')
# date_ = datetime.strptime(dat, '%d.%m.%Y') # переводим введенное значение в дату время
# print(date_)
# td = date_ - dt # считаем прошедшее время
# print(td)
# print(td.days) # тайм дельта используется для расчета разницы во времени

# считаем количество дней до дня рождения. Присвамваем дате рождения текущий год и вычитаем
birthday = input('Дата рождения(дд.мм.гггг): ')
birthday = datetime.strptime(birthday, '%d.%m.%Y').date() #строковую запись переводм в международный формат, а потом в формат даты
date_today = date.today()
print(birthday, date_today)
year_=date_today.year #
birth_day=birthday
birthday = birthday.replace(year=year_)
if birthday < date_today:
    birthday = birthday.replace(year=year_ +1)
    age_days = (date_today + timedelta(days=365) - birth_day).days
elif birthday == date_today:
    print('Поздравляем с днем рождения!')
    exit(0)
days_ = (birthday - date.today()).days
age = round(age_days//365) # контрол + R  заменить значение во всем файле
print(birthday)
print(birthday - date.today())
print(f'Кол-во дней до дня рождения - \'{days_}\'. Вам исполнится \'{age: 0f}\' лет') # выводим ответ в апострофах