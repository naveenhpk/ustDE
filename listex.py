teams=['India','England','Australia','Pakistan','Srilanka']
print('total teams',len(teams))
teams.sort()
# print('Sorted',teams)
teams.append("bangladesh")  #single elemt add
teams.insert(3,'Newzeland') #Index add
teams.extend(['usa','uae']) # add new list
print(teams)

# teams.pop() ----popo last elemt return poped element
# teams.remove('srilanka')  ----remove srilanka from list
# update value use with index ------  teams[2]='Austra'

# if india in teams  ----check wheather elemt is present

# combination  of 2 list
# zip combine list with equal no of elements
# world=[2,1,4,5,6]
# index=1
# for teams,cup in zip(teams,world):
#     print('Teams-',index,teams,'won',cup)
#     index+=1

# join list as a string -----  x="  ".join(teams)