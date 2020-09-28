# -*- coding: utf-8 -*-
"""
文件目的：程序测试

@author: liu
"""

from pso import PSO

import time_s, plots, globalv


time_s.timer()#timestart进行赋值

pso = PSO()

scheme = pso.evolve()

timefly = time_s.time_ufly(scheme)

plots.tu_scatter(scheme)#绘制散点图

timefly = time_s.time_ufly(scheme)

plots.gante(timefly, scheme, globalv.timeu)#绘制甘特图

print('最佳方案：', scheme)#最终方案






