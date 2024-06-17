# Itreators are method that are iused to itrete collections like list tuples etc

prime_nu=[1,3,5,7,11,13,17,19,23,29]
prim_tr=iter(prime_nu)
# moves to the next elemt for each next()
print(next(prim_tr)) #1
print(next(prim_tr)) #3
print("*"*30)

# itreator already passed to the second elemnt then for loop will excute from the 3rd element 5
for i in prim_tr:
    print(i)

print("*" * 30)
class PowThree:
# class implemnt san itreator of power of three
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=3**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
num=PowThree(11)
i=iter(num)
count=0
for x in i:
    print("11 power of",count,"=",next(i))
    count += 1
#
# print("3 power of",count,"=",next(i))
#
# print("3 power of",count,"=",next(i))
# count+=1
# print("3 power of",count,"=",next(i))
# count+=1
# print("3 power of",count,"=",next(i))
# count+=1


