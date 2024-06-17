# deque it is an optimiseed list to perform insertion and deletions easily
from collections import deque
team_list=['rohit','virat','hardik','rahul']
tque=deque(team_list)
print(tque)
tque.append('naveen') #APPEND THE LAST
tque.appendleft('Adarsh') #append the first position
print("after appending",tque)
tque.pop()
tque.popleft()
print("after pop and pop left",tque)