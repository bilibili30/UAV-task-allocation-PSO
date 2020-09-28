# -*- coding: utf-8 -*-
"""
文件目的：所有与距离有关的函数


@author: liu
"""

import math

import globalv

import numpy as np



UAV_start = globalv.UAV_start

target_pos = globalv.target_pos

row = globalv.numU

column = globalv.numT


#无人机到各目标点距离
def dis_UT():
                
    UtoT = np.zeros((row,column))#初始化矩阵信息
        
    for i in range(row):
            
        for j in range(column):
                
            d_x = UAV_start[i][0] - target_pos[j][0]
                
            d_y = UAV_start[i][1] - target_pos[j][1]
                
            UtoT[i][j] = math.sqrt(d_x**2 + d_y**2)
                
    return UtoT#函数返回距离矩阵
    
#各目标点之间的距离    
def dis_TT():
            
    TtoT = np.zeros((column,column))
    
    for i in range(column):
            
        for j in range(column):
                
            d_x = target_pos[i][0] - target_pos[j][0]
                
            d_y = target_pos[i][1] - target_pos[j][1]
                
            TtoT[i][j] = math.sqrt(d_x**2 + d_y**2)
                
    return TtoT   

#距离标准化
def normal():
    
    UtoT = dis_UT()
    
    TtoT = dis_TT()
    
    max_dis = max(UtoT.max(), TtoT.max())
    
    UtoT = UtoT / max_dis
    
    TtoT = TtoT / max_dis
    
    return UtoT, TtoT, max_dis