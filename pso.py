# -*- coding: utf-8 -*-
"""
文件目的：粒子群算法

注：

@author: liu
"""

import numpy as np

from fit_dis import calculate_tcost

import decode, plots, globalv

from time_s import timer

 

class PSO(object):

    def __init__(self):
                
        #后期加速因子和惯性权重采用微分递减修改
        self.w = 1

        self.c1 = self.c2 = 2
        print(type(self.c2))


        self.population_size = globalv.population_size  # 粒子群数量
        
        
        self.dim = globalv.numT  # 搜索空间的维度

        #self.max_steps = globalv.max_steps   # 迭代次数

        self.x_bound = [0, globalv.numU]  # 解空间范围

        self.x = np.random.uniform(self.x_bound[0], self.x_bound[1],

                                   (self.population_size, self.dim))  # 初始化粒子群位置
        
        self.v = np.random.rand(self.population_size, self.dim)  # 初始化粒子群速度

        fitness = self.calculate_fitness(self.x)

        self.p = self.x  # 个体的最佳位置

        self.pg = self.x[np.argmin(fitness)]  # 全局最佳位置

        self.individual_best_fitness = fitness  # 个体的最优适应度

        self.global_best_fitness = np.min(fitness)  # 全局最佳适应度
        
        #存储时间与与之对应的适应值
        self.time_mat = []
        
        self.fitness_mat = []


 
    #适应值计算
    def calculate_fitness(self,x):
        
        ctc = calculate_tcost()

        fitness = ctc.trackcost(x)
        
        return fitness

 
    #进化过程
    def evolve(self):
        
        time_pso = 0#存储程序当前运行时间
                        
        while(time_pso < globalv.max_time):
            
            time_pso = timer()

            r1 = np.random.rand(self.population_size, self.dim)

            r2 = np.random.rand(self.population_size, self.dim)

            # 更新速度和权重
            self.v = self.w*self.v+self.c1*r1*(self.p-self.x)+self.c2*r2*(self.pg-self.x)
            
            self.v = np.clip(self.v,-1,1)#限定速度范围
            
            self.x = self.v + self.x
            
            self.x = np.clip(self.x,0,globalv.numU)
            

            fitness = self.calculate_fitness(self.x)

            # 需要更新的个体
            update_id = np.greater(self.individual_best_fitness,fitness)
            
            self.p[update_id] = self.x[update_id]

            self.individual_best_fitness[update_id] = fitness[update_id]

            # 新一代出现了更小的fitness，所以更新全局最优fitness和位置
            if np.min(fitness) < self.global_best_fitness:

                self.pg = self.x[np.argmin(fitness)]

                self.global_best_fitness = np.min(fitness)
                
            self.time_mat.append(time_pso)
            
            self.fitness_mat.append(self.global_best_fitness)
            
                
            print('当前运行时间：%.5f' % (time_pso))

            print('当前最优值: %.5f' % (self.global_best_fitness))

            print('分配方案：' , decode.deco(self.x[np.argmin(fitness)]))#显示任务分配结果
            
            
        plots.tu_diagram(self.time_mat, self.fitness_mat)#绘制fitness曲线图
            
        scheme = decode.deco(self.x[np.argmin(fitness)])
                    
        return scheme
             
 



