# Counter it is a adictionary sub class which is used to count the hashtable objects
#Orderedd dict
from collections import Counter,OrderedDict,defaultdict
# count each element is a list accurence
rohit_score=[70,89,120,230,100,50,70,67,70,90,87,90,100]
score_count=Counter(rohit_score)
print(score_count)
print(score_count.keys())
print(score_count.values())
# create a list of tupples
print(score_count.items())

# od=OrderedDict()
od=defaultdict(int)
od[1]="53.10"
od[2]='21.0'
od[3]="45.0"
print(od)
print(od[3])
print(od[4]) #using defaultdict retun 0 insted of an error