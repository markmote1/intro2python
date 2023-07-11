class Base:
    def __init__(self):
        self.a = "I have rights"
        self.__c = "and priviledges"
        self.d = "more rights"
        self.e = "and power"


class Derived(Base):
    def __init__(self, a, c, d, e):
        print(self.a) #accessible
        print(self.__c) #unaccessible
        print(self.d) #accessible
        print(self.e) #accessible




# create an instance of the parent class
obj1 = Base()
print(obj1.a)
# print(obj1.c) #- "you dont have rights and permission
print(obj1.d)
print(obj1.e)