from functools import reduce

l = [22, 33, 44] # функции высшего порядка
l1 = [2, 3, 4]
# n = (map(str, l)) # str(map...)переводим в строковое значение функции мэп, в функции мэп применяются только функции
# print(next(n))
# print(next(n))
# print(next(n))
# n1 = [str(i) for i in l] # переводим в строковое значение функции мэп
# print(n, n1)

# def power(n):
#     return n * 2
# n = list(map(power, l)) # list превращает в списки. Функцию пауэр нельзя заменить ничем, кроме лямба функции
# map вычла по одноиндексным элементам
n = list(map(lambda n, m: n - m, l, l1))# Если заменяем лямбда, то деф и ретерн уже не нужны
n = list(map(lambda n, m: n > m, l, l1))
print(n) # лямбда выполянется столько раз, сколько объектов
# print(next(n))
# print(next(n))
# print(next(n))

n = list(filter(lambda x: x % 2 == 0, l))
nn = [i for i in l if i % 2 == 0] # лист комперехеншн
print(n)
print(nn)
nn = []
for i in l: # эта запись лучше подходит для большого массива данных, чтобы быстрее, когда дальше перебират нет смысла. Здесь есть брейк
    if i == 10:
        nn.append(i)
        break

# агрегирующая функция для списка
city = ['У', 'ф', 'а', '-', 4, 5]
# city = map(str, city)
# res = ''.join(city)
l = [1, 2, 3, 4, 5]
# res = reduce(lambda n, m: str(n)+str(m), city)
# res = reduce(lambda n, m: str(m)+str(n), city) # переворачиваем выражение, в редус могут быть строки, числа
res = reduce(lambda n, m: n * m, l)
print(res)

# декоратор - фвп позволяющая вносить изменения в другие фуункции
# работает как прибавление по символу ниже показывает ккак работает
def concat(n, m):
    print('N = ', n)
    print('M = ', m)
    print(str(n)+str(m))
    return str(n)+str(m)

res = reduce(concat, city)





