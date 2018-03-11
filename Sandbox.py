class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("otti",20)
p2 = person("otti2",30)

allPersons = [p1,p2]

for person in allPersons:
    print(person.name)
    print(person.age)