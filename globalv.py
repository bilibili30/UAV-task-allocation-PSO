# -*- coding: utf-8 -*-
"""
文件目的：所有全局变量，初始变量

@author: liu
"""
import numpy as np



#无人机/目标点坐标（随机分布）
'''
#情景一：
UAV_start = np.array([[684,536],[709,548],[737,548],[761,532]])

target_pos = np.array([[691,243],[868,300],[785,413],[569,324],[766,167],[938,213]])
'''

#情景二：
UAV_start = np.random.uniform(100, 200, (8, 2))

target_pos = np.random.uniform(300, 700, (20, 2))


#情景三：



#无人机/目标点数目
numU = len(UAV_start)

numT = len(target_pos)

#无人机任务执行时间
timeu = np.random.uniform(50, 80, (numU, numT))

#最大飞行半径,单位m
max_flight = 2000

#无人机飞行速度，单位m/s
flyv = 3

#种群数量
population_size = 20

#最大迭代时间，单位s
max_time = 0.01
