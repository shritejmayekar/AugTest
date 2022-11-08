# In Overriding the child class have an access of the parent class functions 

class Father :
    def eat(self):
        print("eat")
    def sleep(self):
        print("sleep")
    def walk(self):
        print("walk")
        

class Child(Father):
    def cry(self):
        print("cry")
    def play(self):
        print("play")
        
        
childObject = Child()
fatherObj = Father()
childObject.cry()
childObject.walk()
childObject.eat()
childObject.sleep()
