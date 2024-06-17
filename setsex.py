luckydaw=set()
print(type(luckydaw),luckydaw)

luckydaw_o={14,18,35,75,84,90,35,40,18}
luckydaw_s={23,4,56,7,5,89,76,18,40}

# # add
# luckydaw_o.add(33)
# # delete
# luckydaw_s.discard(7)
print("online",luckydaw_o)
print("online",luckydaw_s)

for i in luckydaw_o:
    print(i)

print("Intersection",luckydaw_o & luckydaw_s)
print("union",luckydaw_o | luckydaw_s)
print("Difference",luckydaw_o - luckydaw_s)

if luckydaw_s == luckydaw_o:
    print("equal")
else:
    print("not equal")


