#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import sys

num_ticket = 3136   # 总共发出的票数量
luckers = []        # 已经中奖号码，若重复领票，废票号要提前写入
late = []           # 未到现场的抽奖券
late_record = []    # 未到现场的抽奖卷记录列表

num_nova = 1        # 一等奖数量
num_stereo = 3     # 二等奖数量
num_scales = 5     # 三等奖数量

def draw_prize(lucker, later):
    '''
    生成随机票号，返回中奖号码
    
    @param lucker: 中奖号码
    @param later: 未到现场号码
    '''
    number = random.randint(1, num_ticket)
    while number in lucker or number in later:
        number = random.randint(1, num_ticket)
    lucker.append(number)
    return lucker


def print_list(left, right, lucker):
    '''
    打印中奖选手名单
    
    @param left:打印起始位置
    @param right:打印终点位置
    @param lucker:中奖号码
    '''
    for i in range(left, right, 1):
        print("恭喜\tNo.{0}\t同学".format(lucker[i]))
        print(" ")


def remove(lucker, later):
    '''
    去除未到现场的票号，返回中奖名单和未到现场数量
    
    @param lucker:中奖号码
    @param later:未到现场号码
    '''
    for i in range(len(later)):
        lucker.remove(later[i])
    return lucker, len(later)


def toNum(lates, later, later_record):
    '''
    将输入字符串转换成列表
    
    @param lates:现场输入的未到现场号码
    @param later:未到现场号码
    '''
    lates = lates.split(" ")
    for i in range(len(lates)):
        lates_int = int(lates[i])
        later.append(lates_int)
        later_record.append(lates_int)
    return later


print(" ")
print(" ")
print("+++++++++++++++++++")
print(" ")
print(" ")
print("赞助鸣谢：华为北京终端业务部")
print(" ")
print(" ")
print("现在终于开始激动人心的抽奖环节，谁会是今晚最亮的崽崽？")
print(" ")
print(" ")
print("+++++++++++++++++++")
print(" ")
print(" ")
'''
三等奖抽奖
'''
print("即将进行三等奖抽取")
print(" ")
print(" ")
start_scales = input("下面请抽奖嘉宾为我们抽取今天的三等奖")
print(" ")
print(" ")

while True:
    for i in range(21):
        time.sleep(0.1)
        print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
    if input() == ' ':
        break

#if start_scales == 'y':
for i in range(num_scales):
    luckers = draw_prize(luckers, late_record)
        
#end_scales = input("是否停止？")
#if end_scales == 'y':
print(" ")
print_list(0, 5, luckers)
print("恭喜以上中奖同学，快快上台领奖")
print(" ")
print(" ")
 

flag_late_scales = input("是否有未到现场的同学？")
print(" ")
print(" ")
while flag_late_scales == ' ':
    late_scales = input("让我们开始补位，遗憾地输入未到现场的票号：")
    print(" ")
    print(" ")
    late = toNum(late_scales, late, late_record)
    [luckers, num_late_scales] = remove(luckers, late)
    late.clear()
    #end_scales = 'n'
    while True:
        for i in range(21):
            time.sleep(0.1)
            print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
        if input() == ' ':
            break
    #end_scales = input()
    #if end_scales == ' ':
    for i in range(num_late_scales):
        luckers = draw_prize(luckers, late_record)
        
    
    #if end_scales == 'y':
    print(" ")
    print_list(5 - num_late_scales, 5, luckers)
    print("恭喜以上中奖同学，快快上台领奖")
    print(" ")
    print(" ")
    flag_late_scales = input("是否还有未到现场的崽崽？")
    print(" ")
    print(" ")

print("恭喜获得华为体脂秤的同学，他们是：")
print(" ")
print_list(0, 5, luckers)


'''
# 程序空转，等待二等奖开启
'''
start_second = 1
while start_second == 1:
    start_second = input()

'''
# 二等奖抽奖
'''
print("即将进行二等奖抽取")
print(" ")
start_stereo = input("下面请抽奖嘉宾为我们抽取今天的二等奖")
print(" ")
print(" ")

while True:
    for i in range(21):
        time.sleep(0.1)
        print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
    if input() == ' ':
        break
    
#if start_stereo == 'y':
for i in range(num_stereo):
    luckers = draw_prize(luckers, late_record)
        
#end_stereo = input("(y/n)")
#if end_stereo == 'y':
print(" ")
print_list(5, 8, luckers)
print("恭喜以上中奖同学，快快上台领奖")
print(" ")
print(" ")
 

flag_late_stereo = input("是否有未到现场的同学？")
print(" ")
print(" ")
while flag_late_stereo == ' ':
    late_stereo = input("让我们开始补位，遗憾地输入未到现场的票号：")
    print(" ")
    print(" ")
    late = toNum(late_stereo, late, late_record)
    [luckers, num_late_stereo] = remove(luckers, late)
    late.clear()
    while True:
        for i in range(21):
            time.sleep(0.1)
            print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
        if input() == ' ':
            break
    #start_stereo = input("下面请抽奖嘉宾为我们补位抽奖(y/n)")
    #print("正在抽奖中，我们的音响会是谁的？")
    #if start_stereo == 'y':
    for i in range(num_late_stereo):
        luckers = draw_prize(luckers, late_record)
        
    #end_stereo = input("y/n")
    #if end_stereo == 'y':
    print(" ")
    print_list(8 - num_late_stereo, 8, luckers)
    print("恭喜以上中奖同学，快快上台领奖")
    print(" ")
    print(" ")
    flag_late_stereo = input("是否还有未到现场的崽崽？")
    print(" ")
    print(" ")

print("恭喜获得华为AI音响的同学，他们是：")
print(" ")
print_list(5, 8, luckers)


'''
# 程序空转，等待二等奖开启
'''
start_first = 1
while start_first == 1:
    start_first = input()
    

'''
# 一等奖抽奖
'''
print("即将进行一等奖抽取")
print(" ")
start_nova = input("下面请抽奖嘉宾为我们抽取今天的一等奖")
print(" ")
print(" ")

while True:
    for i in range(21):
        time.sleep(0.1)
        print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
    if input() == ' ':
        break
        
#if start_nova == 'y':
for i in range(num_nova):
    luckers = draw_prize(luckers, late_record)
        
#end_nova = input("y/n")
#if end_nova == 'y':
print(" ")
print_list(8, 9, luckers)
print("恭喜以上中奖同学，快快上台领奖")
print(" ")
print(" ")
 

flag_late_nova = input("是否有未到现场的同学？")
print(" ")
print(" ")
while flag_late_nova == ' ':
    late_nova = input("遗憾地输入未到现场的票号，让我们开始补位：")
    print(" ")
    print(" ")
    late = toNum(late_nova, late, late_record)
    [luckers, num_late_nova] = remove(luckers, late)
    late.clear()
    while True:
        for i in range(21):
            time.sleep(0.1)
            print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
        if input() == ' ':
            break
    #print("正在抽奖中，我们的音响会是谁的？")
    #if start_nova == 'y':
    for i in range(num_late_nova):
        luckers = draw_prize(luckers, late_record)
        
    #end_nova = input("y/n")
    #if end_nova == 'y':
    print(" ")
    print_list(9 - num_late_nova, 9, luckers)
    print("恭喜以上中奖同学，快快上台领奖")
    print(" ")
    print(" ")
    flag_late_nova = input("是否还有未到现场的崽崽？")
    print(" ")
    print(" ")

print("恭喜获得华为nova5的同学，全场最亮的崽崽就是你：")
print(" ")
print_list(8, 9, luckers)

'''
# 程序空转，是否需要补充抽奖
'''
start_first = 1
while start_first == 1:
    start_first = input()
    

num_addition = int(input("请输入放回奖品池中的奖品数量："))
print(" ")
print(" ")
start_addition = input("请主持人为我们抽取最后的奖品")
print(" ")
print(" ")
while True:
    for i in range(21):
        time.sleep(0.1)
        print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
    if input() == ' ':
        break
    
for i in range(num_addition):
    luckers = draw_prize(luckers, late_record)

print(" ")
print_list(9, 9 + num_addition, luckers)
print("恭喜以上中奖同学，快快上台领奖")
print(" ")
print(" ")
flag_late_addition = input("是否有未到现场的同学？")
print(" ")
print(" ")
while flag_late_addition == ' ':
    late_addition = input("遗憾地输入未到现场的票号，让我们开始补位：")
    print(" ")
    print(" ")
    late = toNum(late_addition, late, late_record)
    [luckers, num_late_addition] = remove(luckers, late)
    late.clear()
    while True:
        for i in range(21):
            time.sleep(0.1)
            print('\r正在抽奖中：{0}'.format('▉▉'*i), end='')
        if input() == ' ':
            break
    #print("正在抽奖中，我们的音响会是谁的？")
    #if start_nova == 'y':
    print(" ")
    for i in range(num_late_addition):
        luckers = draw_prize(luckers, late_record)
        
    #end_nova = input("y/n")
    #if end_nova == 'y':
    print_list(9 + num_addition - num_late_addition, 9 + num_addition, luckers)
    print("恭喜以上中奖同学，快快上台领奖")
    print(" ")
    print(" ")
    flag_late_addition = input("是否还有未到现场的崽崽？")


print("恭喜获得华为奖品的同学")
print(" ")
print_list(9, 9 + num_addition, luckers)
time.sleep(100)
sys.exit(0)
