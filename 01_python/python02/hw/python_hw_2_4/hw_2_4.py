# 아래에 코드를 작성하시오.
class Animal:
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    pass

class Dog(Animal):
  def speak(self):
    return "Woof!"

class Cat(Animal):
  def speak(self):
    return "Meow!"
  
class Flyer:
  def fly(self):
    return "Flying"
  
class Swimmer:
  def swim(self):
    return "Swimming"

class Duck(Animal,Flyer,Swimmer):
  def __init__(self, name):
    super().__init__(name)
  
  def speak(self):
    return "Quack!"

def make_animal_speak(animal:Animal):
  print(animal.speak())

dog = Dog("Dog")
cat = Cat("Cat")
duck = Duck("Duck")
make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(duck)
print(duck.fly())
print(duck.swim())