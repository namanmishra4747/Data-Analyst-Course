class Dog:
    def __init__(self, breed, age, color):
        self.breed =  breed
        self.age = age
        self.color = color


class Cat:
    def __init__(self,name,gender,is_wild):
        self.name = name
        self.gender = gender
        self.is_wild = is_wild

class Burger:
    def __init__(self,bread,topping, price,is_veg,filling): #dunder method
        self.bread = bread
        self.bread = topping
        self.price = price
        self.is_veg = is_veg
        self.filling = filling

tiger = Dog('German Shepherd', 2 , 'golden')
sheru = Dog('Pug', 3 , 'black')
tommy = Dog ('Labrador', 1 , 'white')

mao = Cat('mau', 'M' ,False)
mini = Cat ('mini', 'M' , True)
max = Cat ('max', ' F' , True)
oreo = Cat ('oreo', 'F' , False)

burger1 = Burger('brown','lettuce',50,True, 'mayo')
burger2 = Burger('white','chunks',70,False,'sinque')

print("tiger is a", tiger.breed, "Dog")

    


