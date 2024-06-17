def fibonacci_number(num):
    x,y=0,1
    for i in range(num):
        x,y=y,x+y
        yield x

def prime(num):
    flag=0
    for num in num:
        for i in range(2,num):
            if (num%i)==0:
                flag=0
                break
            else:
                flag=1
        if flag==1:
            yield num

for value in prime(fibonacci_number(20)):
    print(value)



# print(prime(fibonacci_number(6)))