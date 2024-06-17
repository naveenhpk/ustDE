class Prime:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        self.num=self.start #setting the initial number
        return self
    def __next__(self):
        while self.num<=self.stop:
            if self.PrimeCheck(self.num):# checking if the numbber is prime using prime function
                value=self.num #setting prime number to a vlue
                self.num+=1# increementing the num value to the next
                return value
            else:
                self.num+=1 #if not incrementing to the next number
        raise StopIteration  # when the all ement is check raise excepotion

    def PrimeCheck(self,x):
        for i in range(2,int(x/2)):
            if (x % i == 0):
                return False
            else:
                return True

pr=Prime(1,11)

for i in pr:
    print(i)


