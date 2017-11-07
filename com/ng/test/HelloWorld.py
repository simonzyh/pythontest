import sys

print('hello world');

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")

item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

print(total)

paragraph = "1h哈"
pd = paragraph.encode("utf-8", "strict");
print(type(pd))
print(type(pd.decode("utf-8", "")));

print('================Python import mode==========================');
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

print(2 ** 132)

print()
