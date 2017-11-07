# 打开一个文件
import math

def getCosDist(user1, user2):
    sum_x = 0.0
    sum_y = 0.0
    sum_xy = 0.0
    for key1 in user1:
        for key2 in user2:
            if key1[0] == key2[0]:
                sum_x += key1[1] * key1[1]
                sum_y += key2[1] * key2[1]
                sum_xy += key1[1] * key2[1]
                print(str(sum_x)+' '+str(sum_y)+' ')
    if sum_xy == 0.0:
        return 0
    demo = math.sqrt(sum_x * sum_y)
    return sum_xy / demo

def readFile(filename):
    contents = []
    f = open(filename, "r")
    contents = f.readlines()
    f.close()
    return contents


user1=[(1,2),(2,3),(3,4)]
user2=[(1,3),(2,4),(3,5)]
user3=[(1,2),(2,3),(3,5)]
user4=[(11,2),(12,4),(3,8)]

##print(getCosDist(user1,user2))
##print(getCosDist(user1,user3))
print(getCosDist(user1,user4))
f = open("/Users/yehua.zyh/Downloads/store.txt", "r")
contents = f.readlines()

print(contents)

store={}

for line in contents:
    s=line.replace("\n","").split("\t");
    if(s[1] not in store):
        store[s[1]]=[s[0]]
    else:
        store[s[1]].append(s[0])

print(store)