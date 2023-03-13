# class A:
#     def method(self):
#         print("Метод в классе А")

# obj_a = A()
# obj_a.method()
# # Метод в классе А

# class B(A):
#     pass


# obj_b = B()
# obj_b.method()
# # Metод в классе А

# class C(A):
#     def method(self):
#         print("Метод в классе С")

# obj_c = C()
# obj_c.method()
# # Метод в классе С


class A:
    def method(self):
        print("Метод в классе А")
        return "AAA"
    
class B(A):
    def method(self):
        print("Метод в класс В")
        return_from_super = super().method()
        print("supr().method() вернул", return_from_super)
        return "BBB"

obj_a = A()
res_a = obj_a.method()
print("A.method вернул" ,res_a)    

obj_b = B()
res_b = obj_b.method()
print("B.method() вернул ", res_b)

class Range:
    def create(self ,n):
        '''
        Принимает число и возвращает список чисел от 0 до данного числа включительно
        '''
        return list(range(n+1))
    
class Range10(Range):
    def create(self, n):
        '''
        Возвращает список чисел от 0 до 10 включительно
        '''
        return super().create(10)
    
range_obj = Range()
res = range_obj.create(5)
print(res)
#[0, 1, 2, 3, 4, 5]

range10_obj = Range()
res = range10_obj.create(10)
print(res)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class A:
    attr1 = 'a'
    def method(self):
        print("Метод в классе А")

class B:
    attr2 = 'b'
    def method(self):
         print("Метод в классе В")

class C(A,B):
    pass

obj_c = C()

print(obj_c.attr1)#'a'
print(obj_c.attr2)#'b'
obj_c.method()#Метод в классе А

print(C.mro())#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


# перекрестное наследованние

class A:
    pass

class B:
    pass
class C(A,B):
    pass
class D(B,A):
    pass
class E(C,D):
    pass
#TypeError: Cannot create a consistent method resolution
#order (MRO) for bases A, B
