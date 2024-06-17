def fibonacci_number(num):
    x,y=0,1
    for i in range(num):
        x,y=y,x+y
        yield x

def square(num):
    for num in num:
        yield num**2

for value in fibonacci_number(7):
     print(value)
print("*********")
for value in square(fibonacci_number(7)):
     print(value)
print("*********")
print(sum(square(fibonacci_number(7))))
