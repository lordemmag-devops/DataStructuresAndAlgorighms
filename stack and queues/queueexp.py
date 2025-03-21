data = []

#enqueue
data.append(5)
data.append(10)
data.append(15)
data.append(20)

#dequeue
data.pop(0) # The difference between stack and queue is than in queue you're poping the one at the position 0
element = data.pop(0)
print(data[0])
print(data)