"=======================loops======================="
#   ЦИКЛ -блок кода б который отрабратывается нксколько раз # for - цикл , который работает с итерируемыми обьектами , цикл заканчивает свою работу когда он доходит до последнего элемента витерируемом обьекте 

#while - цикл  который работает до тех пор рока условие верное

"=================for================="


# list1=['hello', 10,True ,[1,2,3]]
# for element in list1:
#     print(element)


# string1 = 'hello world'
# for letter in string1:
#     print(letter)



# "====================while===================="

# i = 1
# while i!=10  :
#     print(f'hello {i}')
#     i=i+1

# i=0 #0 equal to False loop while read if i is TRUE (0=false)
# while i:
#     print("hello world")
#     i = i+1


# "===========Ключевые слова в циклах==========="    
# # break- полностью останавливает цикл
# # continue - переход к селедующей итерации


# for i in range(10):
#     if i == 3:
#         break
#     print(i)

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)    


list1=[1,2,3,4,1,1,2,12,1,2,1,1,]
res=list1.count(1)
while res>=0:
    list1.remove(1)
    res=res-1
print(list1)

