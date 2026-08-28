##n=int(input('>'))
##print(n+n%10)
##print((n :=int(input('>')))+ n % 100)
##x=10
##y=10
##if x<y:
##    print('x < y')
##else:
##    if x > y:
##        print('x > y')
##    else:
##        print ('x = y')
##x=10
##y=10
##if x<y:
##    print('x < y')
##elif x > y:
##    print('x > y')
##else:
##    print ('x = y')

##h = input('Введите время суток: ')
##if not h.isdigit():
##    exit(0)
##h = int(h)
##if h >= 4 and h < 12:
##    print ('Morning')
##elif 12 <= h < 17:
##    print('Day')
##elif h >= 17 and h < 24:
##    print ('Evening')
##elif h >=0 and h < 4:
##    print ('Night')
##elif h == 24:
##    print ('Night')
##else:
##    print ('Время суток не соответствует.')

##color = input('Введите цвет светофора: ')
##
##match color:
##    case 'red' | 'no':print('STOP')
##    case 'green': print('GO')
##    case 'yellow': print('READY')
##    case _:print('цвет - ', color)

##n = input('What are you going to do: ')
##
##if n == 'GO':
##    print ('Что непонятного, на зеленый идти надо, а не стоять!')
##if n == 'STOP':
##    print ('stoyat dubina, eto krasnushiiiiiiiiiiiiiy!')
##if n == 'WAIT':
##    print ('Стой в АФК, из-за тебя мы проиграли в ксссссс!!!!!!')

##h = input('Я угадаю, чем тебе сейчас надо заниматься. Введи цифрой время суток: ')
##if not h.isdigit():
##    exit(0)
##h = int(h)
##if h >= 4 and h < 12:
##    print ('Просыпайся! Пора идти учится в школу. Без пятерок не возвращайся!!!')
##elif 12 <= h < 17:
##    print('Жми пакет масла и пора хавать хрючево!')
##elif h >= 17 and h < 24:
##    print ('Хватит отдыхать, посуда немыта! И вообще, уроки кто будет делать?')
##elif h >=0 and h < 4:
##    print ('Ты спать собираешься или нет? Знания усваиваются только во сне!')
##elif h == 24:
##    print ('Ты спать собираешься или нет? Знания усваиваются только во сне!')

"""
   00 0
   01 1
   10 2
   11 3
  100 4
  101 5
  110 6
  111 7
 1000 8
 1001 9
 1010 10
 """

num = input('Число в двоичной системе исчисления >')
print(('Число в десятичной системе исчисления > '), end=' ')
match num:
    case '0':
        print(0)
    case '1':
        print(1)
    case '10':
        print(2)
    case '11':
        print(3)