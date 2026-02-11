class Dog:

    def __init__(self,name,breed,hasfur):
        self.name = name
        self.breed = breed
        self.hasfur = hasfur



    def bark(self):
        print("woof!! woof!!")


    def locomotive(self):
        print("Dog is walking")


dog1 = Dog("JJ","Bulldog",True)
print(dog1.name,dog1.breed,dog1.hasfur)
dog1.bark()
dog2 = Dog("Rodney","German Shepherd",True)
print(dog2.name,dog2.breed,dog2.hasfur)
dog2.bark()
dog3 = Dog("Robert","chihuahua",True)
print(dog3.name,dog3.breed,dog3.hasfur)
dog3.bark()

