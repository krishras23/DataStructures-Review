from collections import deque
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)

print(myStack.pop())
print(myStack.pop())

print(myStack.pop())

myQueue = deque()

myQueue.append('a')
myQueue.append('b')
myQueue.append('c')

print(myQueue)

print(myQueue.popleft())
print(myQueue.popleft())

print(myQueue.popleft())


d = deque()
d.append(1)
print(d)
d.appendleft(2)
print(d)
d.clear()
print(d)
print("hi")
d.extend('1')
print(d)
deque(['1'])
d.extendleft('234')
print(d)
deque(['4', '3', '2', '1'])
print(d.count)
d.pop()
print(d)
deque(['4', '3', '2'])
d.popleft()
print(d)
deque(['3', '2'])
d.extend('7896')
print(d)
d.remove('2')
print("anvi the legend")
print(d)
d.reverse()
print(d)
d.rotate(3)
print(d)