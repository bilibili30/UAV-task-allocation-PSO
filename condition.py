# -*- coding: utf-8 -*-
"""
文件目的：约束条件

@author: liu
"""
import globalv


#最大飞行距离约束
def cont(dis_U):#形参为无人机飞行距离
    
    if dis_U < globalv.max_flight:
        
        cost = 0
        
    else:
        
        cost = float('inf')
        
    return cost
    
    
    