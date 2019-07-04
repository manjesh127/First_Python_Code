# ====================>>>  python classes  <<====================
# class Point:
#     def move(self):
#         print("move function ")

#     def draw(self):
#         print("draw function")


# point1 = Point()  # create the object of class
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()  # create another object instance of class
# # print(point2.x)    #eror because point2 object not x instance             each object has different instance
# point2.x = 2
# print(point2.x)


# ==============================>>> constructor  <<==========================
# class Point:
#     def __init__(self, x, y):  # self is the refrence of the current objects and this init method in create or construct the oject
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move function ")

#     def draw(self):
#         print("draw function")


# point = Point(10, 20)
# print(point.x)

# ===============================>>>  example   <<<==========================
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print("talk function ")
#         print(f'hii i am {self.name}')


# manjesh = Person("manjesh")
# # print(manjesh.name)
# manjesh.talk()


# =================================>>  inheritance   << =======================
class Inherit:
    def walk(self):
        print("inherit method to class")


class Dog(Inherit):
    def bark(self):
        print("dog class method define")


# the Inherit class all method are inherit in Dog class if empty class pass keyword use     
class Cat(Inherit):
    pass



dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
