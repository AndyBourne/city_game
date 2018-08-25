#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Version : 1.0
# @Time    : 2018/8/25
# @Author  : AndyBourne
# @E-mail  : andybourne@163.com
# 实现一个城市名称接龙效果（输入城市的名字后一个字音为下一个城市出现的字音）
import numpy as np
import pandas as pd
import random
from pandas import Series, DataFrame
from pypinyin import pinyin, lazy_pinyin, Style

data = pd.read_csv("/Users/andybourne/Documents/GitHub/city_game/data/region.csv")
test_data = data[['REGION_NAME', 'REGION_NAME_EN']]
name = input(u"输入城市名称：")
left_pinyin_name = lazy_pinyin(name)
left_A = left_pinyin_name[-1]
left_A_upper = left_A.capitalize()
# print(left_A)
print(left_A_upper[0])
# test_data.head(3)
test_data_frame = DataFrame(test_data)
test_data_frame_list = np.array(test_data_frame)
train_x_list=test_data_frame_list.tolist()
# print(train_x_list)
new_answer = []
for each_list in train_x_list:
    if isinstance(each_list,list):
        for new_each in each_list:
            if str(new_each)[0:(len(left_A_upper))] == left_A_upper:
#                 print(new_each)
                new_answer.append(new_each)
# print(new_answer)
# print(len(new_answer))
new_answer_hanzi = []
for each_list in train_x_list:
    if isinstance(each_list,list):
        for new_each in each_list:
#                 print(new_each)
                new_answer_hanzi.append(new_each)
# print(new_answer_hanzi)
# print(len(new_answer_hanzi))
# print(new_answer_hanzi.index(new_answ er[random.randint(0,len(new_answer))]))
print(new_answer_hanzi[new_answer_hanzi.index(new_answer[random.randint(0,len(new_answer))])-1])