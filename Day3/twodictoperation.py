# chainmap  is a dictionaru like a class which is able to make a asingle view porfoli.csv

from collections import ChainMap
# create 2 dict
tmodule_1={1:"anglar",2:"Python"}
tmodule_2={3:"React",4:"Angular",5:"Django"}
# combining 2 dict
modulelist=ChainMap(tmodule_1,tmodule_2)
print(modulelist)

# adding new child to chaimap dict
tmodule_3={6:"Java",7:"Html"}
updatemodulelist=modulelist.new_child(tmodule_3)
print(updatemodulelist)
print(updatemodulelist.keys())
# accesing keys
print(list(updatemodulelist.keys()))
# accessing values
print(list(updatemodulelist.values()))