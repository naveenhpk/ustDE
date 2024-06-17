# Generator is a function that returns an itreator that produces a sequence of values when itretor over

def custom_generator(n):
    value=0
    while value<n:
        yield value
        value+=1
value=custom_generator(10) # give the genrator stored value
print(value)
print("**************")
print(next(value)) # retuens a itreatir
print(next(value))
print("**************")
for value in custom_generator(10):
    print(value)



print("**************")
cubes_genrator=(i*i*i for i in range(5))
for j in cubes_genrator:
    print(j)

print("********")
class PowerThree:
    def __init__(self,max=0):
        self.n=0;
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>self.max:
            raise StopIteration
        result=3**self.n
        self.n+=1
        return result

 # genertaor
def GenPoerThree(max=0):
    value=0
    while value<max:
        yeild 3**value
        value +=1
