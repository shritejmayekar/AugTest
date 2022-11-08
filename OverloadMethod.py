

# Python do not support the method overloading by default 
class OverloadMethod :
    
    def add(self,a=None,b=None):
        if a is None and b is None:
            return 0
        elif b is  None and a is not None:
            return a
        else:
            return (a+b)
            

myOverload = OverloadMethod()
print(myOverload.add(6,4))
print(myOverload.add(75))
print(myOverload.add())
