# -*- coding: utf-8 -*-
"""
文件目的：计算航迹成本

@author: liu
"""

import globalv, distance

from decode import deco

import numpy as np

from condition import cont


class calculate_tcost(object):
    
    def __init__(self):
        
        #初始化参数
        self.fitness = np.array([])
        
        self.UtoT, self.TtoT, self.max_dis = distance.normal()
        
        self.disU = [[] for k in range(globalv.numU)]#存储每个无人机飞过的每段距离

    #计算航迹代价
    def trackcost(self,taskcode):
           
        for k in range(globalv.population_size):
        
            cost_sum = 0
            
            UandT = deco(taskcode[k])#每架无人机分配了哪些任务
                    
            for i in range(globalv.numU):
                                
                UAV = UandT[i]
                
                cost = 0
                
                if len(UAV) == 0:#无人机没有任务
                    
                    pass
                
                elif len(UAV) == 1:#无人机有一个任务
                    
                    dis0 = self.UtoT[i][UAV[0]]
                    
                    self.disU[i].extend([dis0,dis0])
                                        
                else:#无人机有超过一个任务
                    
                    dis1 = self.UtoT[i][UAV[0]]
                    
                    self.disU[i].append(dis1)
                                       
                    for j in range(len(UAV)-1):
                        
                        dis2 = self.TtoT[UAV[j]][UAV[j + 1]]
                        
                        self.disU[i].append(dis2)
                        
                    dis3 = self.UtoT[i][UAV[len(UAV)-1]]
                    
                    self.disU[i].append(dis3)

                cost = sum(self.disU[i])
                
                cost = cost + cont(cost*self.max_dis)
                
                cost_sum = cost_sum + cost
                    
            self.fitness = np.append(self.fitness,cost_sum)
                        
        return self.fitness
