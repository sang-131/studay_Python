class person(object):
    tall = 180
    hobbies = []
    def __init__(self, name, age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def infoma(self):
        print('%s is %s weights %s'%(self.name,self.age,self.weight))
Bruce = person("Bruce", 25,180)

print("person.tall is Bruce.tall: ", person.tall is Bruce.tall)
Bruce.tall = 185    #重新赋值或者修改
print( "person.tall is Bruce.tall: ", person.tall is Bruce.tall)
print( person.__dict__)
print( Bruce.__dict__)
del Bruce.tall   #再次删除实例的赋值
print("person.tall is Bruce.tall: ", person.tall is Bruce.tall)  #person.tall is Bruce.tall为True


Bruce.tall += 3    
print("person.tall is Bruce.tall: ", person.tall is Bruce.tall)
print(person.__dict__)
print(Bruce.__dict__)


del Bruce.tall

print("person.hobbies is Bruce.hobbies: ", person.hobbies is Bruce.hobbies)
Bruce.hobbies = ["C#", "Python"]
print ("person.hobbies is Bruce.hobbies : ", person.hobbies is Bruce.hobbies)
print( person.__dict__)
print( Bruce.__dict__)
del Bruce.hobbies
print( "person.hobbies is Bruce.hobbies: ", person.hobbies is Bruce.hobbies)

print() 

Bruce.hobbies.append("CSS")
print("person.hobbies is Bruce.hobbies: ", person.hobbies is Bruce.hobbies)
print(person.__dict__)
print(Bruce.__dict__)
