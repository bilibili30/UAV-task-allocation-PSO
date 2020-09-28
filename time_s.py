# -*- coding: utf-8 -*-
"""
文件目的：所有与时间有关函数

@author: liu
"""
import time, globalv, distance

a = 0#标志位，timestart只在第一次赋值

time_start = time_end = 0#初始化


#计时函数
def timer():#单位为秒
        
    global a,time_start,time_end
    
    if a == 1:
        
       time_end = time.time() 
              
    elif a == 0:
        
        time_start = time.time()
        
        a = 1
        
    return time_end - time_start#返回当前运行时间


#计算无人机各段飞行所需时间，虽然同计算fit_dis，但是程序最后执行不占用时间，所以没必要合并到fit_dis
def time_ufly(UandT):
    
    UtoT, TtoT, max_dis = distance.normal()
    
    UtoT = UtoT * max_dis
    
    TtoT = TtoT * max_dis#还原到归一化之前的距离
    
    timeU = [[] for k in range(globalv.numU)]
        
    for i in range(globalv.numU):
        
        UAV = UandT[i]
        
        if len(UAV) == 0:#无人机没有任务
            
            pass
            
        elif len(UAV) == 1:#无人机有一个任务
                
            time0 = UtoT[i][UAV[0]] / 3#距离除以速度等于飞行时间
                
            timeU[i].extend([time0, time0])
                                    
        else:#无人机有超过一个任务
                
            time1 = UtoT[i][UAV[0]] / 3
                
            timeU[i].append(time1)
                                   
            for j in range(len(UAV)-1):
                    
                time2 = TtoT[UAV[j]][UAV[j + 1]] / 3
                    
                timeU[i].append(time2)
                    
            time3 = UtoT[i][UAV[len(UAV)-1]] / 3
                
            timeU[i].append(time3)
            
    return timeU

#计算各个无人机执行各个任务的时间段

        
    
    
    
    
    
    
    
    
