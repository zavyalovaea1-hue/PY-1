# import random
# winners = {'ножницы':'бумага',
#            'бумага':'камень',
#            'камень':'ножницы'}
#
# while True:
#     options = ['камень', 'ножницы', 'бумага']
#
#     your_choice = input('Введите камень, ножницы, бумага или выход: ')
#     if your_choice == 'выход':
#         print('Игра заверешена.')
#         break
#
#     if your_choice not in options:
#         print('Некорректный ввод!')
#         continue
#
#     computer_choice = random.choice(options)
#     print(computer_choice)
#
#     if your_choice == computer_choice:
#         print('Ничья!')
#     elif winners[your_choice] == computer_choice:
#     # elif ((your_choice == 'ножницы' and computer_choice == 'ножницы') or
#     #     (your_choice == 'камень' and computer_choice == 'камень') or
#     #     (your_choice == 'бумага' and computer_choice == 'бумага')):
#         print('Вы победили!')
#     else:
#         print('Победил компьютер!')
# from datetime import datetime
# try:
#
#     birth_date = input('Введите вашу дату рождения в формате (DD.MM.YYYY.):')
#     birth_date = datetime.strptime(birth_date, '%d.%m.%Y') # переводим введенную строку в форматы даты-времени
#     current_date = datetime.today() # вывести сегодняшнюю дату или datetime.data.today()
#     age = current_date.year - birth_date.year
#     if current_date.month < birth_date.month:
#         age -= 1
#     print(current_date)
#     if age % 10 ==1:
#         word = 'год'
#     elif age in [2, 3, 4]:
#         word = 'года'
#     else:
#         word = 'лет'
#
#     print(f'Вам {age} {word}')
# except ValueError:
#     print("Ошибка даты.")
# user = {'name': 'Anna', 'age': 20, 'city': 'Moscow'}
# print(f'Имя: {user['name']} Возраст: {user['age']}')
# # user = user.update({'city': 'Riga'}) неверная запись
# user ['city'] = 'London' # замена значения ключа в словаре (города)
# user['proffession'] = 'programmer' # добавляем к словарб профессию, добавляется в самый конец словаря
# # del user['age'] # удаляет возраст. или:
# user.pop('age')
# user['email'] = 'anna777@yandex.ru'
# if 'email' in user:
#     print('Есть ключ.')
# else:
#     print("Ключа нет.")
# for key, value in user.items():
#     print(f'{key}: {value}') # выводим все ключи и значения.
# print(user)
# text = "Осень в Москве, Зима в Москве, Весна в Москве, Лето в Москве!"
# #создать слвоарь полсчета слов
# words = text.replace(',', '').replace('.', '').lower().split() # раздвелить и убрать знаки препинания
# counts = {}
# print(words)
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
# print(counts)
# for word in text:
#     print(word)

# students = [('Анна', 'A'), ('Ivan', 'B'), ('Maria', 'A'), ('Petr', 'B'), ('Olga', 'C')]
#
# groups = {}
# for name, group in students:
#     if group not in groups:
#         print(name, group)
#         groups[group] = []
#
#     groups[group].append(name)
#
# print(groups)

# warehouse = {'laptop': {'price': 80000, 'quantity': 5}, 'mouse': {'price': 1500, 'quantity': 20}, 'keyboard': {'price': 4000, 'quantity': 10}}
#
# print(warehouse)
#
# while True:
#     print(f'\n')
#     print(f'1 - Показать товары.')
#     print(f'2 - Добавить товар.')
#     print(f'3 - Отпустить товар.')
#     print(f'4 - Пополнить остаток.')
#     print(f'5 - Изменить цену.')
#     print(f'6 - Посчитать стоимость склада.')
#     print(f'7 - Самый дорогой товар.')
#     print(f'8 - Товары с остатком меньше 3.')
#     print(f'0 - Выход')
#
#
#     choice = input('Выберите действие: ')
#     if choice == '1': # показать товары
#         for name, product in warehouse.items():
#             print(f'Товар: {name}, Цена: {product['price']} руб Остаток: {product["quantity"]}')
#     elif choice == '2': # Добавить товар
#         name = input('Введите товар: ')
#         if name in warehouse:
#             print('Товар есть в списке')
#         else:
#             price = input('Введите цену: ')
#             quantity = input('Введите количество: ')
#             warehouse[name] = {'price': price, 'quantity': quantity}
#             print(warehouse)
#             print('Товар добавлен.')
#
#     elif choice == '0':
#         print('Выход.')
#         break
#
#     elif choice == '3':  # Пополнить остаток
#         name = input('Введите товар: ')
#         if name not in warehouse:
#             print('Товара нет в списке')
#         else:
#             quantity = int(input('Введите количество: '))
#             if warehouse[name]['quantity'] > quantity:
#                 warehouse[name]['quantity'] -= quantity
#                 print('Товар продан')
#             else:
#                 print('Недостаточное количество товара')
#
#     elif choice == '4':  # Пополнить остаток
#         name = input('Введите товар: ')
#         if name not in warehouse:
#             print('Товара нет в списке')
#         else:
#             quantity = int(input('Введите количество: '))
#             warehouse[name]['quantity'] += quantity
#             print('Остаток пополнен.')
#             print()
#
#     elif choice == '5': # Изменить цену
#         name = input('Введите товар: ')
#         if name not in warehouse:
#             print('Товара нет в списке')
#         else:
#             new_price = int(input("Введдите новую цену: "))
#             warehouse[name]['price'] = new_price
#             print('Цена изменена.')
#     elif choice == '6': # Посчитать общую стоимость склада, перемножение словарей
#         # pass # временная заглушка недописанного кода
#         total = 0
#         for product in warehouse.values():
#             total += product['price'] * product['quantity']
#         print(f'Общая стоимость склада: {total} рублей')
#
#     elif choice == '7': # самый дорогой товар
#         max_price = 0
#         max_product = ''
#         for name, product in warehouse.items():
#             if product['price'] > max_price:
#                 max_price = product['price']
#                 max_product = name
#             print(f'Самый дорогой товар: {max_product} цена: {max_price}')
#
#     elif choice == '8': # товар с остатком меньше 3
#         flag = False
#         for name, product in warehouse.items():
#             if product['quantity']< 3:
#                 print (f'Количество товара {name} меньше 3')
#                 flag = True
#         if flag == False:
#                 print ('На складе достаточное количество товаров')

# Кинотеатр 10*15
kinoteatr = {}













