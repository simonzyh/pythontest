a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素


###dictionary
dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict1['one'])  # 输出键为 'one' 的值
print(dict1[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


#print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))

t={'Runoob':1}

print(type(t))


def example(a,b):
     return (a,b)

print(example(1,2))



#

def example1(d):
    # d 是一个字典对象
    for c in d:
        print(c)

print(example1((1,2,3,4)))


print(example1({1:11,2:22,3:33,4:44}))


list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]

print(type(list[2]))

print(type(list[2:3]))

a=10


b=19

print(a and b)

w = dict()
w[1]=123
print(type(w))

for i in w:
    print(str(i));