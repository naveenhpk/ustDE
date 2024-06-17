try:
    # x=int(input("Enter the number1"))
    # y=int(input("Enter the number2"))
    # print("Division result",x/y)

    # prime=[7,11,13,17]
    # prime[len(prime)]=19

    num = int(input('enter the even value'))
    assert num%2==0
except ZeroDivisionError:
        print("denominator cannot be zero")
# except IndexError:
#     print("Direct inserion with index is not allowed in list")
else:
    print(num)
finally:
    print("ITs over")
