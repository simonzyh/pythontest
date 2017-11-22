a = 2


def ChangeInt(a):
    a = 10
    print(a);


ChangeInt(a)
print(a)  # 结果是 2


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)

num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()

print(num)

a = set(['abracadabra', '123'])

for i in a:
    print(i)

d = ('sape', 4139)

print(type(d))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(v)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(basket):
    print(f)

print(basket)
