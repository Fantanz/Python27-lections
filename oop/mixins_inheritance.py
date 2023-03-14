"""
Миксины - классы , которые будут исполбзоваться для наследие но от миксинов не создаются объекты
2. Миксины - классы-примеси , которые служат для расширения функционала класса
""" 
# От миксинов нельзя создавать объекты, поскольку миксины -несамостоятельные классы
# При наследовании миксины должны идти в первую очередь
class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плыть')

class FlyMixin:
    def fly(self):
        print('я могу летать')

class Human(WalkMixin,SwimMixin):
    name = 'Человек'
    
    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'Рыба'



class Exocoetidae(SwimMixin,FlyMixin):
    name = 'летучая рыба'

class Duck(WalkMixin,SwimMixin,FlyMixin):
    name = 'утка'

objects = [Human(),Fish(), Exocoetidae(),Duck()]

for obj in objects:
    print(obj.name)
    
    attrs = ['fly','swim','walk','talk']
    for attr in attrs:
        if hasattr(obj,attr):
            method = getattr(obj,attr)
            method()
#obj = Human()

#obj.walk()
#obj.fly()
#obj.swim()



