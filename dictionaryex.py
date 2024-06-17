mystock={"TCS":2700,"Infosys":3000,"IDBI":140,"NTPC":220}
# print(type(mystock))

# mydicy={} ----empty dict creation
# if duplicate key latest value taken

print("Price of Infosys:",mystock["Infosys"])   #cannot access using index
# add new item
mystock['SBI']=1700
print(mystock)

# print(len(mystock)) ---- length

# print("values:",mystock.values())
# print("keys",mystock.keys())

# itreate through dict
for stock in mystock:
    print(stock,"price",mystock[stock])
#
# print(mystock.items())  #return list of tupples
# for stock in mystock.items():  #retuens as a tuple and after we can access using index  ----- for key,value in mystock.items()
#     print(stock)
#     print(stock[0])

# to change values to key
# swap={}
# for key,value in mystock.items():
#     swap[value]=key
# print(swap)