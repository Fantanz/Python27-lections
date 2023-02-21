# "==============Встроенные функции===================="
# # enumerate 

# string = 'Hello'
# enum=enumerate(string)
# #print(enum)
# # <enumerate object at 0x7f7884dfdb40>
# print(list(enum))
# # [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
# string1='world'
# enum1=enumerate(string1, 5)
# print(list(enum1))
# # [(5, 'w'), (6, 'o'), (7, 'r'), (8, 'l'), (9, 'd')]

# # дан список с числами , умножьте на 2 все числа под нечетным индексом, умножьте на 3 все числа под индексом

# list1=[1,4,78,3,7,0,4,2,7]

# for ind in range(len(list1)):
#     element=list1[ind]
#     if ind % 2 : #ind % 2 !=0
#         list1[ind]=element*2
#     if not ind % 3: #ind % 3==0 
#         list1[ind] = element * 3
# print(list1)          

# list1=[1,4,78,3,7,0,4,2,7]
# for ind, element in enumerate(list1):
#     if ind % 2 : #ind % 2 !=0
#         list1[ind]=element*2
#     if not ind % 3: #ind % 3==0 
#         list1[ind] = element * 3
# print(list1)        

# import string

# alfa = string.ascii_lowercase 
# #enum2=enumerate(alfa,1)
# print(dict(enumerate(alfa,1)))

# #zip

# list1=[1,2,3,4,5,6]
# list2='abcdefg'
# list3= [0.5, 0.3 ,0.6]
# print(list(zip(list1,list2,list3)))
# # [(1, 'a', 0.5), (2, 'b', 0.3), (3, 'c', 0.6)]


# "===================функция высшего порядка==================="
# # это функция , котороя:
# # принимает в аргументв другую функцию 
# #  возвращает функцию
# # создает внутри функцию
# # вызывает внутри функцию


# # map -принимает в аргументы функцию и итерируемый обьект , возвращает генератор , в котором все элементы результат принимаемой функции , в которую передали элементы последовательности

# mapped= map(int,['1','2','3']) 
# print(mapped)
# # <map object at 0x7fee40f53f70>
# print(list(mapped))
# # [1, 2, 3]

# list1=[1,2,3,4]
# def func(i):
#     i+=1
#     return i
# print(list(map(func,list1)))
# # [2, 3, 4, 5]
# list1=[1,2,3,4]

# print(list(map(lambda i:i+1,list1)))
# # [2, 3, 4, 5]


# #filter-принимает в аргументы функцию и итерируемый обьект , возвращает генератор , в котором элементы из последовательности прошедшие фильтр(функция вернула True)


# list1=[-3,7,0,34,-23,435,10]

# def is_positive(i):
#     return i>0
# print(list(filter(is_positive,list1)))

# print(list(filter(lambda i:i>0,list1)))



# list1=['Hello',"world",'MAKERS']
# def func(i):
#     i.istitle()
#     return i
    

# print(list(filter(lambda i:i.istitle(),list1)))
# res=[i for i in list1 if i[0].isupper()]
# print(res)

# print(list(filter(lambda i:i[0].isupper(),list1)))

# def first_is_upper(word):
#     first=word[0]
#     return word.isupper()
# print(list(filter(first_is_upper,list1)))

# #reduce - функция, которая импортирурет из functools.
# # тоже принимает функцию и итерирумый обьект возвращает 1 результат


# from functools import reduce

# list1=[2,4,6,3,65,8]

# def mul(x,y):
#     return x*y

# res =reduce(mul,list1)
# print(res)


from functools import reduce
list1=['hello' ,'world','makers','bootcamp']

print(reduce(lambda x ,y: x if len(x) > len(y) else y,list1))

list1=['hello' ,'world','makers','bootcamp']
def func(x,y):
    if len(x)>len(y):
        return x
    return y
print(reduce(func,list1))