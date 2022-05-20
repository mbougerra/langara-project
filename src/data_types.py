import sys
print(dir(sys))
x=[1,2,3,4,'Hello',False]
print(f'The size of the list x is {sys.getsizeof(x)} byte(s)')
y=1e6
print(f'y={y}')
print(f'The data type of y is {type(y)}')
z=('a','b','c')
w=['a','b','c']
print(f'The size of the tuple {z} is {sys.getsizeof(z)} bytes')
print(f'The size of the list {w} is {sys.getsizeof(w)} bytes')