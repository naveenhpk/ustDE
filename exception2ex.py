yob=int(input("enter the yob"))

age=2024-yob

if age<18:
    raise Exception(f'The age should be greater than 18 and you are {age}')
print(age)