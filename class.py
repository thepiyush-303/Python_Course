class person:
    name="piyush"
    age=18
    type="veg"
    def info(self):
      print(self.name,"is",self.age,"year old and purely",self.type)
obj1=person()
obj2=person()
obj2.name="ayush"
obj2.age=20
obj2.type="veg"
# print(obj1.name)
# print(obj1.age)

# obj1.info()
# obj2.info()

# Self parameter is an reference to the current instance of the class and is used to access variables that belong to the class


# Making of constructor:it helps when we create a object in class it automaticlly calls itself.

class Person:
   
   def __init__(self,name,age):
      print("constructor called")
      self.age=age
      self.name=name

   def biodata(self):
        print(f"{self.name} is {self.age} year old")
a=Person("piyush",18)
a.name="piyush"
a.age=18
a.biodata()