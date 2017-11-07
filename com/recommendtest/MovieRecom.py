import sys
import math
from texttable import Texttable

#计算余弦距离
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
    if sum_xy == 0.0:
        return 0
    demo = math.sqrt(sum_x * sum_y)
    return sum_xy / demo

#读取文件，读取以行为单位，每一行是列表里的一个元素
def readFile(filename):
    contents = []
    f = open(filename, "r")
    contents = f.readlines()
    f.close()
    return contents


# 数据格式化为二维数组
def getRatingInfo(ratings):
    rates = []
    for line in ratings:
        rate = line.split(",")
        if(rate[0].isdigit()):
          rates.append([int(rate[0]), int(rate[1]), float(rate[2])])

    print('记录总量：'+str(len(rates)))
    return rates


# 生成用户评分数据结构
def getUserScoreDataStructure(rates):
    # userDict[2]=[(1,5),(4,2)].... 表示用户2对电影1的评分是5，对电影4的评分是2
    userDict = {}
    itemUser = {}
    for k in rates:
        user_rank = (k[1], k[2])
        if k[0] in userDict:
            userDict[k[0]].append(user_rank)
        else:
            userDict[k[0]] = [user_rank]

        if k[1] in itemUser:
            itemUser[k[1]].append(k[0])
        else:
            itemUser[k[1]] = [k[0]]
    print('用户总量：'+str(len(userDict)))
    print('电影总量：'+str(len(itemUser)))

    return userDict, itemUser


# 计算与指定用户最相近的邻居
def getNearestNeighbor(userId, userDict, itemUser):
    neighbors = []
    print(str(userId)+'  电影数量: '+str(len(userDict[userId])))
    #找出有相同电影评价的所有用户
    for item in userDict[userId]:
        print(str(item[0])+' '+str(len(itemUser[item[0]])))
        for neighbor in itemUser[item[0]]:
            if neighbor != userId and neighbor not in neighbors:
                neighbors.append(neighbor)

    print('邻居数量：'+str(len(neighbors)))
    neighbors_dist = []
    for neighbor in neighbors:
        dist = getCosDist(userDict[userId], userDict[neighbor])
        print(str(dist)+' '+str(userDict[userId])+' '+str(userDict[neighbor]))
        neighbors_dist.append([dist, neighbor])
        if(len(neighbors_dist)>100):
            break
    neighbors_dist.sort(reverse=True)
    return neighbors_dist


# 使用UserFC进行推荐，输入：文件名,用户ID,邻居数量
def recommendByUserFC(filename, userId, k=5):
    # 读取文件
    contents = readFile(filename)

    # 文件格式数据转化为二维数组
    rates = getRatingInfo(contents)
    contents.clear()
    # 格式化成字典数据
    #userDict ={用户:[(电影,评分),(电影,评分)]}
    #itemUser={电影:[用户，用户]}
    userDict, itemUser = getUserScoreDataStructure(rates)
    rates.clear()
    # 找邻居 [[相似度，用户],[相似度，用户]]
    neighbors = getNearestNeighbor(userId, userDict, itemUser)[:k]

    # 建立推荐字典
    recommand_dict = {}
    for neighbor in neighbors:
        neighbor_user_id = neighbor[1]
        movies = userDict[neighbor_user_id]
        for movie in movies:
            if movie[0] not in recommand_dict:
                recommand_dict[movie[0]] = neighbor[0]
            else:
                recommand_dict[movie[0]] += neighbor[0]

                # 建立推荐列表
    recommand_list = []
    for key in recommand_dict:
        recommand_list.append([recommand_dict[key], key])
    recommand_list.sort(reverse=True)
    user_movies = [k[0] for k in userDict[userId]]
    return [k[1] for k in recommand_list], user_movies, itemUser, neighbors


# 获取电影的列表
def getMovieList(filename):
    contents = readFile(filename)
    movies_info = {}
    for movie in contents:
        single_info = movie.split(",")
        movies_info[int(single_info[0])] = single_info[1:]
    return movies_info


# 从这里开始运行
if __name__ == '__main__':



    # 获取所有电影的列表
    movies = getMovieList("/Users/yehua.zyh/Downloads/ml-20m/movies.csv")
    #获取推荐的数据recommend_list[[距离，电影],]
    #user_movie[电影,]
    #items_movie {电影:[用户，用户]}
    #neighbors  [[相似度，ID],[相似度，ID]]
    recommend_list, user_movie, items_movie, neighbors = recommendByUserFC("/Users/yehua.zyh/Downloads/ml-20m/ratings1.csv", 103521, 80)

    print(recommend_list)
    print(user_movie)
    print(items_movie)
    print(neighbors)

    neighbors_id = [i[1] for i in neighbors]
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t', 't', 't'])
    table.set_cols_align(["l", "l", "l"])
    rows = []
    rows.append([u"movie name", u"release", u"from userid"])
    for movie_id in recommend_list[:20]:
        from_user = []
        for user_id in items_movie[movie_id]:
            if user_id in neighbors_id:
                from_user.append(user_id)
        rows.append([movies[movie_id][0], movies[movie_id][1], ""])
    table.add_rows(rows)
    print(table.draw())



