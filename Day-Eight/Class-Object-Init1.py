class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
name =input("Enter your name: ")
age = input("Enter your Age: ")
p1 = person(name, age)
print(p1.name)
print(p1.age)
