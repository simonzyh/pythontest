import random

L = ['Google', 'Runoob', 'Taobao'];

L.pop();

print(max(L));

list_2d = [[i for i in range(1, 5)] for i in range(5)]

print(list_2d);

for i in range(1, 5):
    print(i)

lt = tuple(L);

print(lt)

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict1 = {'Name1': 'Runoob', 'Age1': 7, 'Class': 'First'}

dict.update(dict1)

print(dict.pop('Name'))
print(dict)

a, b = 0, 1
while b < 10:
    print(b, end='')
    a, b = b, a + b

print()

print(random.choice([1, 2, 3]))

print(random.choice([1, 2, 3]))

print(random.choice([1, 2, 3]))

for i,j in  enumerate('123456'):
    print(str(i) +" "+j)
