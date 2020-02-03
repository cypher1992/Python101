# List as Queues

# Que follows FIFO = First In First Out
# List are not good for FIFO
# not efficient for this

# import collection library with deque
from collections import deque

# create a que with deque method
queue = deque(["Eric Forman","Donna Piniciotti","Steven Hyde","Jackie Burkhart","Michael Kelso","Fez ???"])

# kitty is append to the end of the list
queue.append("Kitty Forman")
# First index is out
queue.popleft()

print("QUE: ", queue)
print("Eric Forman is out from Popleft", queue)

