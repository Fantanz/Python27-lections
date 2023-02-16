"=================Функции================="
# функция - именованный блок кода, который принимает аргументы и возвращает результат
 

func = lambda num1, num2: num1 + num2
res=func(5,10)
print(res)

# lambda -ключевок слово, для создания анонимной  функции

def my_sum2(num1, num2):
    return num1 + num2
print(my_sum2) #<function my_sum2 at 0x7f6a62a52050>

res=my_sum2(13,45)
print(res)


def calc(num1,num2,oper):
    """
    oper-строкас, с операцией для вычислений
    "+" - сложение
    "-" - вычитание
    """

    if oper=='+':
        return num1+num2
    elif oper=='-':
        return num1 - num2
    elif oper=='*':
        return num1*num2
    elif oper=='/':
        return num1 / num2
    
print(calc(10,2,'+'))
print(calc(10,2,'-'))    
print(calc(10,2,'*'))    
print(calc(10,2,'/'))    
print(calc(10,2,'5'))#> None

def my_len(obj):
    "Возвращает длину обьекта"
    count = 0
    for i in obj:
        count+=1
    return count

print(my_len([15,23,64,23,12]))#5
print(my_len('sdaffasfaf'))#10
print(my_len({'a':1,'b':2}))#2


def super_len(obj):
    try:
        #если мы можем итерировать его
        return my_len(obj)
    except TypeError:
        #если не можем , то будем итерироавать его в виде строки
        return my_len(str(obj))
print(super_len([1,2,3,4]))#4    
print(super_len(123456789))# 9 ('123456789')
print(super_len(None))#4

"======================DRY======================"
#DRY -don't repeat yourself (Не повторяйся)
#представим , что  у нас нет функции len

str_='Hello world'
count = 0
for i in str_:
    count+=1

list_=[1,2,3,4,5,6,7,8,9]
count = 0
for i in str_:
    count+=1

def len_(obj):
    count=0
    for i in obj:
        count+=1
    return count

print("damp")
str_='Hello world'
print(len_(str_))
list__=[1,2,3,5,6,3,26,23,535]
print(len_(list_))

"============Аргументы и параметры============"
# Параметры - локальные переменные , значения которым мы задаем при вызове функции
# Аргументы - значения которым мы задаем ппараметры при вызове функции

def func(var):
    local_var=5
    print(locals())
    #{'var': 6, 'local_var': 5}
func(6)
#print(local_var) NameError
#print(var) NameError

"==========Виды параметров=========="

#1. обязательные 
#2. необязательные 
#2.1 с дефолтным значением (по умолчанию) 
#2.2 args (arguments)
#2.3 kwargs (key word arguments)

def func(a):
    print(a)

# func()
# TypeError: func() missing 1 required positional argument: 'a'

func('hello')

def func(a,b='default'):
    print(a,b)

func('hello')# 'hello' 'default'
func('hello', 100) #'hello' 100


"""+++++++++++++ARGS+++++++++++"""
def func(a,b='default',*args):
    print(a,b ,args)
func('hello',100,84,23,'world')
#hello 100 (84, 23, 'world')


"""===================KWARGS++++=========="""
def func(a,b='default',*args,**kwargs):
    print(a,b ,args,kwargs)
func('hello',100,84,23,key1='value',key2=500)
#hello 100 (84, 23, 'world')




"=============Виды аргументов============="
# позиционные(по порядку параметров)
# именнованные(по имены параметров)

def func2(a,b):
    print(f"a={a},b={b}")
func2(10,20)#a=10,b=20 позиционно

func2(a=30 ,b=50)#именнованные
func2(b=50, a=30)#именнованные

"============Звездочки============"
list1='hello'
list2=[*list1]#распоковает list1
print(list2)

dict1={'a':1,'b':2}
list3=[*dict1]
#list3 = ['a','b']
dict1={'a':1,'b':2}
list3=[**dict1]
#list3 = ['a':1,'b':2]