# 1, 2, 3 could be website links
browsing_data = []
browsing_data.append(1)
browsing_data.append(2)
browsing_data.append(3)
y = browsing_data.pop()  # removes last item in list
print(y)
print(browsing_data)
if not browsing_data:
    browsing_data = [-1]
    print("disable")


    #QUEUES
from collections import deque
browsing_data = []
browsing_data.append(1)
browsing_data.append(2)
browsing_data.append(3)
y = browsing_data.popleft() #popleft for Queues not pop as in Stack