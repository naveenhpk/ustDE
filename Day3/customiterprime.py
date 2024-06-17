# create a custom itretor that give next prime number b/w given number

class PrimeIter:
    def __init__(self,frange,lrange):
        self.frange=frange
        self.lrange=lrange
    def __iter__(self):
        self.n=self.frange
        return self
    def __next__(self):
        if self.n<self.lrange:
            raise StopIteration
        a=self.Prime(self.n)
        self.n+=1
        return a
    def Prime(self,n):
        flag = 0
        for num in num:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                yield num
        #


p=PrimeIter(10,30)
i=iter(p)
for x in i:
    print(p.Prime(next(i)))

