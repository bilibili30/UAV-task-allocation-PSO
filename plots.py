# -*- coding: utf-8 -*-
"""
文件目的：所有画图函数

@author: liu
"""
import numpy as np

import matplotlib.pyplot as plt

import globalv



#无人机/任务坐标初始图
def tu_scatter(UandT):
    
    #散点图绘制
    plt.scatter(globalv.UAV_start[:,0], globalv.UAV_start[:,1], marker='<', c='b', s=100, label='UAV')
    
    plt.scatter(globalv.target_pos[:,0], globalv.target_pos[:,1], marker='o', c='r', s=100, label='target')

    #添加图例
    plt.legend()
    
    #设置标题，坐标轴标签
    plt.title('UAV/target position', fontsize=20)
    
    plt.xlabel('Y', fontsize=14)
    
    plt.ylabel('X', fontsize=14)
    
    #坐标轴刻度大小
    plt.tick_params(axis='both', labelsize=13)
    
    #标记无人机序号
    n=np.arange(1,globalv.numU + 1)
    
    for i,num in enumerate(n):
        
        xynum = (globalv.UAV_start[i][0] + 5, globalv.UAV_start[i][1])#标记点坐标
        
        plt.annotate(num, xynum)

    #标记任务序号
    n=np.arange(1, globalv.numT + 1)
    
    for i,num in enumerate(n):
        
        xynum = (globalv.target_pos[i][0] + 5, globalv.target_pos[i][1])
        
        plt.annotate(num, xynum)
               
    #保存散点图
    plt.savefig("tu_scatter.png", dpi=800)
    
    fly(UandT)
    
    plt.show()

#程序运行曲线图
def tu_diagram(time_mat, fitness_mat):
    
    plt.plot(time_mat, fitness_mat, c='y', lw=2, label='PSO')
    
    plt.legend()
    
    plt.title('fitness-time', fontsize=20)
    
    plt.xlabel('time', fontsize=14)
    
    plt.ylabel('fitness', fontsize=14)
    
    plt.tick_params(axis='both', labelsize=13)
    
    plt.savefig("tu_diagram.png", dpi=800)
    
    plt.show()    


#绘制甘特图
def gante(timeufly,UandT,timeu):
    #形参为飞行时间列表,分配结果列表,执行时间

    plt.plot(0)
    
    plt.xlabel("time/min", fontsize=14)
    
    plt.ylabel("UAV", fontsize=14)

    y = range(0, globalv.numU, 1)
    
    #纵轴刻度表示
    uavlist = []
    
    for i in range(globalv.numU):
        
        uavlist.append(r'$UAV%d$'%(i+1))
    
    plt.yticks(y, uavlist)
    
    plt.title('UAV/target gan', fontsize=20)

    for j in range(globalv.numU):#无人机个数
        
        if len(UandT[j]) == 0:#没任务的无人机画白色表示空
            
            plt.barh(j, 5, height=0.5, color="w")
                        
        else:
            
            for i in range(len(UandT[j])):
                
                if i == 0:#如果任务是第一个任务
                    
                    time = timeufly[j][i]
                    
                    plt.barh(j, timeu[j][i], left=time, height=0.35)
                    
                    plt.text(time+10, j, 'task%d'%(UandT[j][i]+1), verticalalignment="center", color="white", size=5)

                   
                else:#如果任务不是第一个任务
                    
                    time = time + timeufly[j][i] + timeu[j][i-1]
                
                    plt.barh(j, timeu[j][i], left=time, height=0.35)
                    
                    plt.text(time+5, j, 'task%d'%(UandT[j][i]+1), verticalalignment="center", color="white", size=5)
                
    plt.savefig("tu_gante.png", dpi=800)
                            
    plt.show()
 
    
#绘制飞行路线图
def fly(UandT):
    
    for i in range(globalv.numU):
        
        listut = np.array([globalv.UAV_start[i]])#每个无人机飞过的任务点坐标
        
        if len(UandT[i]) == 0:
            
            pass
        
        else:
            
            listut = np.row_stack((listut, globalv.target_pos[UandT[i]]))
            
        if len(UandT[i]) != 1:
            
            listut = np.row_stack((listut, globalv.UAV_start[i]))
                                        
        plt.plot(listut[:,0], listut[:,1], lw=1, linestyle='-.')
                
    plt.savefig("tu_fly.png", dpi=800)