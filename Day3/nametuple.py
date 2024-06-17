from collections import namedtuple
# courses =namedtuple('course','name,tech')
courses =namedtuple('course',['name','tech']) #initializing thenamed tuple
# clist=courses('datascience','pyhton')
clist=courses(name='datascience',tech='pyhton') # assigning the value

print(clist)
print(clist.name)#accaesing the vlaue by attr name
print(clist[0]) # accessing the value by index
print(getattr(clist,'tech'))#accesing the valuee by getattr method

courselist=['web development','Angular']
print(courses._make(courselist)) # converting list to name tupple
print(courses._asdict(clist)) # converting to l=dictionary

