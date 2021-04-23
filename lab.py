print("Hello world")
print("some string")
print(5)
print(10)
print(15)
print('asdf')
a = 5
print(a)
print("a")
print(a)
b = 6
print(b)
a = 10
print(a)
print(a)
print(b)
c = "Hello world"
print(c)
print(a)
print(b)
b = 10
print(a)
print(b)
b = "Hello"
print(b)
a = b
print(a)
print(b)
a = 1
b = 2
temp = a
print(temp)
a = b
print(a)
b = temp
print(b)
print(a)
print(b)

#Переменные
name = "Kolia"
name
name = "Sania"
name

#Функция принт
"Vova" * 3
"Runnin' down the hill"
'Runnin\' down the hill'
"Vova" .upper()
len("Vova")
len(str(304023))
name = "Vova"
name
print(name)

#Списки
lottery = [3, 42, 12, 19, 30, 59]
len(lottery)
lottery.sort()
print(lottery)
lottery.reverse()
print(lottery)
lottery.append(199)
print(lottery)
print(lottery[0])
print(lottery[1])
print(lottery)
print(lottery[0])
lottery.pop(0)
print(lottery)



#A Byte of Python
#Основы
#Коментарии
print('Привет, Мир!') #print -- это функция

#print -- это функция
print('Привет, Мир!')
#Текст програми говорит о том, Как, а комментарии должны обьяснять, Почему.
#/
#Метод Формат (format)
#Создает строку на основе каких-либо данных.
age = 26
name = 'Swaroop'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляеться с этим Python'.format(name))

#десятичное число (.) с точностью в 3 знака для плавающих:
'{0:.3}'. format(1/3)

# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
'{0:_^11}'.format('hello')

# по ключевым словам:
'{name} написал {book}'.format(name='Swaroop', book='A byte of Python')


#Переменные
#Пример:Использование переменных и констант
# Имя файла : var.py

i = 5
print(i)
i = i + 1
print(i)

s = '''Это много строчная строка.
Это вторая её строчка.'''
print(s)

# Логические и физические строки
i = 5
print(i)
#тоже самое
i = 5;
print(i);
#и тоже самое можеть быть записано в виде
i = 5; print(i);
#или даже
i = 5; print(i)

#Явное обьединение строк
s = 'Это строка. \
    Это строка продолжаеться.'
print(s)
#Аналолгично
print\
(i)
#То же самое, что и
print(i)

#Операторы и выражения
#Операторы
2 + 3
3 * 5

#Краткая запись мат. операций и присваиванияa 
a = 2; a = a * 3
#в виде:
a = 2; a *= 3

#Выражения
length = 5
breadth = 2

area = length * breadth
print('Площадь равна', area)
print('Периметр равен', 2 * (length + breadth))


#Поток команд
#Оператор if
number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Hi Romina') # Начало нового блока
    print('(хотя и не выиграли никакого приза!)') # Конец нового блока
elif guess < number:
    print('Нет, загаданое число немного болше этого.') # Ещё один блок
    # Внутри блока вы можете выполнить всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
    # что-бы попасть сюда, guess должно быть больше, чем number
    print('Завершено')
    # Это последнее выражение выполняется всегда после выполнения оператора if

# Оператор while

number = 23
running = True

while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Поздравляем, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < number:
        print('нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
    # Здесь можете выполнить всё что вам ещё нужно

print('Завершение.')

# Цикл for

for i in range(1, 5):
    print(i)
else:
    print('Цикл for закончен')

# Оператор break

while True:
    s = input('Введите что-нибуть : ')
    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Завершение')

# Оператор continue

while True:
    s = input('Введите что-нибуть : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue 
    print('Введённая строка достаточной длины')
    # Разные другие действия здесь...

# Функции

def sayHello():
    print('Привет, Мир!') # блок, принадлежащий функции
# Конец функции

sayHello() # вызов функции
sayHello() # ещё один вызов функции

# Параметры функций

def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

printMax(3, 4) # прямая передача значений

x = 5
y = 7

printMax(x, y) # передача переменных в качестве аргументов


# Локальные переменные
x = 50

def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

func(x)
print('x по-прежнему', x)

# Зарезервированное слово "global"

x = 50

def func():
    global x

    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

func()
print('Значение x составляет', x)

# Зарезервированное слово "nonlocal"

def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        global x
        x = 5

    func_inner()
    print('Локальное x сменилось на', x)

func_outer()

# Значения аргументов по умолчанию

def say(message, times = 1):
    print(message * times)

say('Привет') 
say('Мир', 5)

# Ключевые аргументы

def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', a c равно', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

# Переменное число параметров

def total(a=5, *numbers, **phonebook):
    print('a', a)

    #проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

        #проход по все элементам словаря
        for first_part, second_part in phonebook.items():
            print(first_part,second_part)

print(total(10,123,Jack=1123,John=2231,Inge=1560))

# Только ключевые параметры

# Оператор "return"

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y

print(maximum(2, 3))

# Строки документации

def printMax(x, y):
    '''Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые если возможно
    y = int(y)

    if x > y:
        print(x, 'найбольшее')
    else:
        print(y, 'наибльшее')

printMAx(3, 5)
print(printMax.__doc__)


# Модули

import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)


print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')


# Оператор from ... import ...

from math import *
n = int(input("Введите диапазон:- "))
p = [2, 3]
count = 2
a = 5
while (count < n):
    b=0
    for i in range(2,a):
        if ( i <= sqrt(a)):
            if (a % i == 0):
                print(a, "непростое")
                b = 1
            else:
                pass

    if (b != 1):
        print(a,"простое")
        p = p + [a]
    count = count + 1
    a = a + 2
print(p)

# Имя модуля -__name__

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('меня импортировали в другой модуль.')

# Создания собственных модулей

def sayhi():
    print('Привет! Это говорит мой модуль.')

__version__ = '0.1'

# Конец модуля mymodule.py

# ещё один модуль

import mymodule

mymodule.sayhi()
print ('Версия', mymodule.__version__)

# Вот версия, использующая синтаксис from..import

from mymodule import sayhi, __version__

sayhi()
print('Версия', __version__)

#Это импортирует все публичные имена, такие как sayhi
from mymodule import *

# Структура данных

# Краткое введение в обьекты и классы

# Это мой список покупок
shoplist = ['яблоко', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), 'покупки.')

print('Покупки', end='')
for item in shoplist:
    print(item, end='')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)


# Кортеж

zoo = ('питон', 'слон', 'пингвин') # помните, что скобки не обьязательны
print('Количество животных в зоопарке -', len(zoo))

new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные,привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1 + \
    len(new_zoo[2]))

# Словарь

# 'ab' - сокращение от 'a'ddress'b'ook

ab = {  'Swaroop'   :  'swaroop@swaroopch.com',
        'Larry'     :  'larry@wall.org',
        'Matsumoto' :  'matz@ruby-lang.org',
        'Spammer'   :  'spammer@hotmail.com'
    }

print("Адрес Swaroop'a:", ab['Swaroop'])


# Удаление пары ключ-значение
del ab['Spammer']

print('\nB адресной книге {0} контакта\n' .format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}' .format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])


# Последовательность

# Операцыя индексирования 
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Символ 0 -', name[0])

# Вырезка из списка
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 до конца:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])

# Вырезка из строки 
print('Символ с 1 по 3:', name[1:3])
print('Символ с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])

# Ссылки

print('Простое присваивание')
shoplist = ['яблоки','манго','морковь','бананы']
mylist = shoplist # mylist - лишь ещё одно имя, указывающие на тот же обьект!

del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один
# объект.

print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # создаём копию путём полной вырезки
del mylist[0] # удалаем первый элемент

print('shoplist:', shoplist )
print('mylist', mylist)
# Обратите внимание, что теперь списки разные

# Ешё о строках

name = 'Swaroop' # Это обьект строки

if name.startswith('Swa'):
    print('Да, строка начинаеться на "Swa"')

if 'a' in name:
    print('Да, она содержит строку "a"')

if name.find('war') != -1:
    print('Да, она содержит строку "war"')

delimeter = '_*_'

mylist = ['Бразилия','Россия','Индия','Китай']
print(delimiter.join(mylist))

# Решение задач

# Решение

import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"', 'C:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'E:\\Backup' # Подставте ваш путь.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Создаём каталог если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# Имя zip-файла
target = today + os.sep + now + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ''.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')


# Классы
class Person:
    pass # Пустой блок

p = Person()
print(p)

# Методы обьектов

class Person:
    def sayHi(self):
        print('Привет! Как дела?')

p = Person()
p.sayHi()

# Метод __init__
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Привет! Меня зовут', self.name)

p = Person('Swaroop')
p.say_hi()

# Переменные класса и обьекта

class Robot:
    '''Представляет робота с именем'''
    # Переменная класса содержащая количество роботов
    population = 0

    def __init__(self, name):
        '''Инициализация данных'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))

        # При создании этой личности, робот добавляеться
        # к переменной 'population'
        Robot.population += 1

    def __del__(self):
        '''Я умираю'''
        print('{0} уничтожаеться!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))
        
    def sayHi(self):
        '''Приветствие робота.

        Да, они это могут.'''
        print('Приветствую! мои хозяева называют меня {0}.'.format(self.name))

    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут поделать какуе-то роботу.\n")

print("Роботы закончили свою роботу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()

#  Наследование

class SchoolMember:
    '''Представляет любого человека в школе.'''
    def ___init___(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0}'.format(self.name))
    def tell(self):
        '''Вывести информацию'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def ___init___( self, name, age, salary):
        SchoolMember.___init___(self, name, age)
        self.salary = salary
        print('(Созадан Teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0-d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def ___init___(self, name, age, marks):
        SchoolMember.___init___(self, name, age)
        self.marks = marks
        print('(Создан Student: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки:"{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell() # работает как для приподавателя, так и для студента


# Метаклассы

from abc import *

class SchoolMember(metaclass=ABSMeta):
    '''Представляет любого человека в школе'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0}'.format(self.name))

    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

#m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"

print() # печатаем пустую строку

memberes = [t, s]
for member in members:
    member.tell() # работает кака для приподавателя, так и для студента


# Ввод-вывод

# Ввод от пользователя

def reverse(text):
    return text[::-1]

def  is_palindrome(text):
    return text == reverse(text)

someting = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, не палиндром")

# Файлы

poem = '''\
Програмировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python!
'''

f = open('poem.txt', 'w') # открываем для записи (writing)
f.write(poem) # записываем текст файла
f.close() # закрываем файл

f = open('poem.txt') # если не указан режим, по умолчанию подразумевается
                     # режим чтения ('r'eading)
while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')

f.close() # закрываем файл


# Pickle

import pickle

# имя файла, в котором мы сохраним обьект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем обьект в файл
f.close()

del shoplist # уничтожаем переменную shoplist
# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем обьект из файла
print(storedlist)

# Обработка исключений

try:
    text = input('Введите что-нибуть -->')
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))

# Вызов исключения

class ShortInputException(Exception):
    '''Пользовательский класс исключения'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
    
try:
    text = input('Введите чот-нибудь --> ')
    if len(text) <3:
        raise ShortInputException(len(text), 3)
    # Здесь может происходить  обычная робота
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введённой строки -- {0};\
        ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Не было искючений.')

# Try .. Finally

import time

try: 
    f = open('poem.txt')
    while True: # наш обычно способ читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) # Пусть подождёт некоторое время
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')

# Оператор with

with open("poem.txt") as f:
    for line in f:
        print(line, end='')
        
