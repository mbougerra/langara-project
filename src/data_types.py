import sys
print(dir(sys))
x=[1,2,3,4,'Hello',False]
print(f'The size of the list x is {sys.getsizeof(x)} byte(s)')
y=1e6
print(f'y={y}')
print(f'The data type of y is {type(y)}')
