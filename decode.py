# -*- coding: utf-8 -*-
"""
文件目的：解码

注：

@author: liu
"""



import globalv


#浮点型编码的解码方案
def deco(taskcode):

    UandT = [[] for k in range(globalv.numU)]#存储每架无人机需要执行的任务
    

    #为无人机分配任务
    for i in range(globalv.numT):
        
        for j in range(globalv.numU):
            
            if int(taskcode[i]) == j:
                
                a = 0#设置标志位判断当前值是否为列表中第一个元素
                                
                for l in range(len(UandT[j])):
                    
                    if taskcode[i] < taskcode[l]:
                        
                        UandT[j].insert(l,i)#为任务进行排序
                        
                        a = 1
                        
                        break
                        
                if a != 1:
                    
                    UandT[j].append(i)
                                        
    return UandT

