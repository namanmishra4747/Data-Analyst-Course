class clal:

    result = 0

    def show(self):
        return self.result

    def add(self,n1,n2):
        self.result = n1+n2

    def sub(self,n1,n2):
        self.result = n1 - n2

    def mul(self,n1,n2):
        self.result = n1*n2

    def square(self,n1):
        self.result = n1*n1

    def div(self,n1,n2):
        self.result = n1/n2

c = clal()
c.add(10,20)
#print(c.result)
print(c.show())

c.sub(12,3)
print(c.show())

c.square(5)
print(c.show())

c.div(8,2)
print(c.show())
