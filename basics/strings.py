"=====================Сторки====================="
# строки - это неизменяемый тип данных . предназначенный для хранения тексты( последовательсности символов)
string1='строка в  одинарнвх кавычках'
string2="строка в двойных кавычках"
string3="Don't"
string4='Study in "Makers Incubator"'
string5='''
Многострочные
текст
тут можно использовать 'любые'  "2кавычки" 
'''
print(string5)
string7= 'hello' + ' '+ 'world' #'hello world'
string8= 'Hello'*3 #HelloHelloHello
string9= 'Hello' +str(1)
"=================Экранизация строк================="
print('hello\nworld')# back slash and  перенос на строку
'\t'# отступ (табуляция)
'\\'# отображение \
'\''# отображение '
'\"'# отображение "
'\r'# перенос каретки в начало строки
'\v'# перенос на новую строку со смещением вправо на длину предыдущей строки
'hello\nworld'
#hello
#world
'hello\tworld'
#hello  world
'экранизация \\'
# экранизация \
'123456789\rhello'
#hello6789
print('hello\vworld\vmakers')
#hello
#     world
#          makers
"================Индексы================"
#индекс- порядковый номер символа в строке (начиная с 0)
'h e l l o'
#0 1 2 3 4
#     -2 -1
string = 'hello world'
string[0]
index =len(string)-1 
#print(string(index))=print(string-1)# same result
string[0]#'h'
string[-1]#'d'
string[5]#''

#срез - часть строки
string[6:9]#'wor' до 9 
string[0:5]#'hello' =string[:5] its same
string[:]# hello world
string[:6]#'hello'
string[7:]#'orld'
string[0:11:2]# 'hlowrd'
string[::2]# 'hlowrd'
string[::-1]#'dlrow ollenh'
#print(len(string))
"==============Форматирование строк=============="
title ='Пирог'
price = 35
string =f' Название : {title}, цена: {price}'
#print(string) Название : Пирог, цена: 35

formatl = 'Название: %s, цена: %s'
#print(formatl %("Яблоко", 80)) same
#print(formatl %('Яблоко' ,'80')) same
format2= 'Название: {}, цена: {}'
#print(format2.format('Груша', 60))
#Название: Груша, цена: 60
# метод - функция , которая принадлежит определенному типу данных, обращаемся к ней через точку

(dir(str))# посмотреть все доступные методы для данного типа данных
'hello'.upper# 'HELLO'
'HELLO'.lower#'hello'
'hello WORLD'.swapcase #'HELLO world'
'HelLo'.swapcase #"hELlo"
'hello world'.title# 'Hello World'
'hello world'.capitalize#"Hello world
'hello'.center(11)#'   hello   '
'hello'.center,(11 ,'-') #'---hello---'
'Hello'.count('l')#2
'hello'.count('ll')#1
'hello'.count('Hello')#0
'hello'.count('')#6
'hello world'.split()#['hello','world']
'hello world'.split('o')#['hell' ,'w' ,'rld'] {o}пропала
' '.join(['hello', 'world'])# 'hello world'
'%'.join(['hello' ,'world'])# "hello%world"
'hello world'.find('w')# 6 
'hello world'.find('wor')# 6 it find where is the index 'wor'
'hello world'.find('o')#4
'hello world'.rfind('o')# 7





