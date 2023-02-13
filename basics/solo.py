list_ = [] 
name1 = input("Введите имя и фамилию: ") 
name2 = input("Введите имя и фамилию: ") 
name3 = input("Введите имя и фамилию: ") 
name4 = input("Введите имя и фамилию: ") 
name5 = input("Введите имя и фамилию: ") 
list_.append(name1) 
list_.append(name2) 
list_.append(name3) 
list_.append(name4) 
list_.append(name5) 
target = " " 
surnames = [] 
for x in list_: 
    t = x.find(target) 
    v = x.rfind(target) 
    if x.count(target) > 1: 
        surnames.append(x[v+1:]) 
    else: 
        surnames.append(x[t+1:])
print(sorted(surnames))