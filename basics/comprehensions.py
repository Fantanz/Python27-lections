"==============Comprehensions=============="

#генератор, с помощью которого можно создавать последовательность используя цикл for

list1 = []
for i in range(1 ,11):
    list1.append(i)
#print(list1)

    #list=[1,2,3,4,5,6,7,8,9,10]
list = [i for i in range(1,11)]
#print(list1)
# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр

comprehension = (i for i in range(1,4))
#print(comprehension)
## результат for элемент in последовательность
# генератор - итерируемый обьект , который не хранит в себе польностью их когда требуется

#print(next(comprehension)) #1
#print(next(comprehension)) #2
#print(next(comprehension)) #3
#print(next(comprehension)) # StopIteration

#next - функция  которая принимает в себя генератор, запрашивает следущий  элемент у генератора и возвращает его

comprehension = (i for i in range(1,4))

#print(list(comprehension))#[1,2,3]
#print(list(comprehension))#[]

"===============Синтаксический сахар==============="
# list comprehensoin
list_compr = [i for i in 'hello']
#print(list_compr)
#['h', 'e', 'l', 'l', 'o']

#dict comprehension 
dict_compr = {i:str(i) for i in range(1,11)}
#print(dict_compr)
#{1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

#фильтр
string = 'Hello World'
res = [i for i in string if i.islower()]
#print(res)
# ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
res =[]
for i in string:
    if i.islower():
        res.append(i)
#print(res)        

num=[i for i in range(1,11) if i%2==0]
#print(num)
num=[]
for i in range(1,11):
    if i%2==0:
        num.append(i)
#print(num)
num=[]

num = [i for i in range(2,11,2)]
#print(num)



res=[i*100 for i in range(1,11)]
#print(res)
res1=['hello' for i in range(5)]
#print(res1)

users=['test1', 'test2','test3']
#users=['hello test1']
res=['Hello'+name for name in users]
res=[f'Hello {name}' for name in users]

#print(res)
res10=[[x for x in range(1,i+1)] for i in range(1,6)]
#print(res10)
res=[]
for i in range(1,6):
    inner_list=[]
    for x in range(i,i+1):
        inner_list.append(x)
    res.append(inner_list)
#print(res)       
#res9=[list(range(1,i+1)) for i in range(1,6)]
#print(res9)


list1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#es=[1,2,3,4,5,6,7,8,9,10,11,12]
res=[i for inner_list in list1 for i in inner_list]
#print(res)



#[1,2,3,4]
#['не четное','четное','не четное','четное']
res=['четное' if i%2==0 else 'не четное' for i in range(1,7)]
#print(res)



dict1={'a':1, 'b':2,'c':3}
res={ v:k for k,v in dict1.items()}
#print(res)
for k,v in dict1.items():
    res.update({v:k})
#print(res)    


res={i:[x for x in range(1,i+1)] for i in range(1,6)}
print(res)