#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   Title: pc_viewer.py
#
#   author: Ryota Amano
#
#---------comment-----------
# pointcloudをpython上で2D(バードビュー), 3D
# 両方で表示するクラス
#
# 引数のx, y, z, layerはnumpy.array
#
# def __init__()の引数、layer_numは出力時の色のリスト
# を作成するために使用
#
# レーザが8レイヤなら8を入れればrainbowを8当分した色で
# 描画してくれる
# 
#
#---------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm



class PC_VIEWER():
    def __init__(self, layer_num):
        self.fig = plt.figure(figsize=(16,10))
        self.ax1 = self.fig.add_subplot(121, projection='3d')
        self.ax2 = self.fig.add_subplot(122)

        self.ax1.set_xlabel("x[m]")
        self.ax1.set_ylabel("y[m]")
        self.ax1.set_zlabel("z[m]")
        self.ax1.set_title("PointCloud with 3D")

        self.ax2.set_xlabel("x[m]")
        self.ax2.set_ylabel("y[m]")
        self.ax2.set_title("PointCloud TopDownView")

        diff = 1.0 / float(layer_num)
        self.color_list = np.arange(0.0, 1.0, diff)

        self.cmap = "gist_rainbow"

        plt.grid(True)
    
    # x,y,z: np.array
    def Draw3dPoints(self, x, y, z, layer):
        color = self.color_list[layer]
        self.ax1.scatter3D( x, y, z, s=10, c=color, cmap = self.cmap, marker='.', vmin=0.0, vmax=1.0, alpha=1.0, linewidths=None, edgecolors=None)

    def Draw2dPoints(self, x, y, z, layer):
        color = self.color_list[layer]
        self.ax2.scatter( x, y, s=10, c=color, cmap = self.cmap, marker='.', vmin=0.0, vmax=1.0, alpha=0.4, linewidths=None, edgecolors=None)

    def ShowAnimation(self):
        plt.pause(.01)

    def Show(self):
        plt.show()

    def Close(self):
        plt.close()

if __name__ == '__main__':
    pcv = PC_VIEWER(8)

    for i in range(10000):
        X = Y = np.arange(-15, 15, 0.5)
        #X, Y = np.meshgrid(x, y)
        sigma = 4
        Z = np.exp(-(X**2 + Y**2)/(2*sigma**2)) / (2*np.pi*sigma**2)

        layer = np.random.randint( 0, 7, 60)

        pcv.Draw3dPoints(X, Y, Z, layer)
        pcv.Draw2dPoints(X, Y, Z, layer)
        pcv.ShowAnimation()
    #pcv.Show()
    pcv.Close()

