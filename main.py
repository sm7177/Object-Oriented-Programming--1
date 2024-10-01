# class student:
#     grade=12
#     name="Subrina"
#     def intro(self):
#         print("My name is",self.name)
#     def details(self):
#         print("My name is",self.name)
#         print("I study in grade",self.grade)


# obj=student()
# obj.intro()
# obj.details()




#-----------------------------

class Parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        # print(self.name, "sings a ",song)
        return self.name,"sings a ",song
        
    def dance(self):
        print("my name is ",self.name,"and my age is ",self.age,"is dancing")

    
obj=Parrot("andy",26)
print(obj.sing("happy"))
obj.dance()

obj1=Parrot("Dustin",19)
print(obj1.sing("sad"))
obj1.dance()















# parrot1=Parrot("a",10)
# parrot2=Parrot("b",20)
# print("parrot1 is a ",parrot1.species)
# print("parrot2 is a ",parrot2.species)
# print("My name is",parrot1.name,"and my age is",parrot1.age)
# print("My name is",parrot2.name,"and my age is",parrot2.age) 