from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

#class Dog(AbstractAnimal):
#    pass

#obj = Dog()

class Dog(AbstractAnimal):
    def speak(self):
        print("gav-gav")
        