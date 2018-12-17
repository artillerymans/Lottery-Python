from collections import Counter, deque

import random


# 创建红球队列
def createRedDeque():
    return deque(range(1, 34))


# 创建蓝球队列
def createBlueDeque():
    return deque(range(1, 17))


# 随机生成一组 6 + 1的随机数
def randomOnelist():
    ball_list = []
    red_list = createRedDeque()
    blue_list = createBlueDeque()
    num = 6
    while num:
        red_ball = random.choice(red_list)
        red_list.remove(red_ball)
        num -= 1
        ball_list.append(int(red_ball))
    ball_list = sorted(ball_list)
    ball_list.append(int(random.choice(blue_list)))
    # print("ball List = %s" % (ball_list))
    return ball_list


#  随机生成 nums 组 6 + 1的随机数
def randomList(nums):
    list_dict = []
    while nums:
        list_dict.append(randomOnelist());
        nums -= 1
    return list_dict


# 筛选前七出现概率最高的数字
def filterFirstSeven(ls_dict):
    sum_red_list = []
    sum_blue_list = []
    for top_item in ls_dict:
        # print(top_item)
        deque_top = deque(top_item)
        # print("列表原始状态:%s" % (deque_top))
        remove_item = deque_top.pop()
        # print('移除的值:%s' % (remove_item))
        # print("列表移除后的状态:%s" % (deque_top))
        sum_red_list.extend(deque_top)
        sum_blue_list.append(remove_item)
    red_Counter = Counter(sum_red_list)
    blue_Counter = Counter(sum_blue_list)
    red_top_6 = red_Counter.most_common(6)
    blue_top_1 = blue_Counter.most_common(1)
    number_red_list = []
    for number in red_top_6:
        number_red_list.append(number[0])
    number_list = sorted(number_red_list)
    number_list.append(blue_top_1[0][0])
    return number_list

def randomNumberList(number):
    num = 1
    while number:
        random_list = randomList(100000)
        sum_list = filterFirstSeven(random_list)
        number -=1
        print("结果数据 %s:%s" %(num, sum_list))
        num +=1


randomNumberList(10)



# 结果数据 1:[4, 5, 7, 16, 17, 18, 7]
# 结果数据 2:[3, 8, 14, 20, 23, 32, 15]
# 结果数据 3:[3, 4, 10, 16, 19, 29, 6]
# 结果数据 4:[6, 11, 16, 19, 21, 32, 12]
# 结果数据 5:[1, 2, 9, 13, 18, 26, 15]
# 结果数据 6:[3, 11, 12, 14, 17, 22, 5]
# 结果数据 7:[3, 5, 7, 24, 27, 28, 3]
# 结果数据 8:[2, 6, 23, 26, 28, 33, 10]
# 结果数据 9:[9, 15, 18, 20, 31, 32, 14]
# 结果数据 10:[4, 5, 8, 10, 13, 21, 5]


# 结果数据 1:[3, 9, 12, 16, 17, 31, 12]
# 结果数据 2:[7, 10, 11, 20, 28, 29, 13]
# 结果数据 3:[5, 7, 14, 16, 25, 28, 3]
# 结果数据 4:[2, 7, 13, 21, 23, 25, 2]
# 结果数据 5:[5, 12, 17, 24, 25, 27, 12]
# 结果数据 6:[1, 7, 8, 9, 12, 30, 14]
# 结果数据 7:[12, 16, 18, 21, 22, 25, 9]
# 结果数据 8:[4, 15, 18, 20, 21, 33, 1]
# 结果数据 9:[2, 11, 14, 22, 28, 30, 15]
# 结果数据 10:[1, 4, 8, 11, 21, 28, 16]





