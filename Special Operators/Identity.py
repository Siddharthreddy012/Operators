num=10
num_1=10
print(id(num))
print(id(num_1))
loc=num is num_1
print(loc)
loc=num is not num_1
print(loc)
num_1=10.0
print(id(num_1))
loc=num is num_1
print(loc)
loc=num is not num_1
print(loc)
