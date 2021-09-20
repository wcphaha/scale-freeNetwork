import random
import time
import pandas as pd
import pygame

Title = '无标度网络生成过程'
Width = 1000
Height = 700
M0 = 4  # 初始状态是M0都等于4的完全图
M = 2
Node_size = 8
# 线条颜色
Black = (0, 0, 0)
white = (255, 255, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)
GreenYellow = (173, 255, 47)
Green = (50, 205, 50)
Purple = (160, 32, 240)
Datapath = 'datas/Network_info.txt'


class Node:

    def __init__(self, position, seq, degree=0):
        self.position = position
        self.seq = seq
        self.degree = degree

    def update_degree(self):
        self.degree += 1

    def __str__(self):
        return f'序号:{self.seq},度:{self.degree},位置:{self.position}'


def choose_node(nodes):
    weights = {}  # 保存每个节点的权重，即被选择建立连边的概率
    total_degree = 0
    for i in nodes:
        total_degree += i.degree
    for node in nodes:
        weights[node.seq] = node.degree / total_degree
    # 把每个节点被选择的概率以几何分布的形式标记在一个数轴(line)上
    line = list(weights.values())
    line.insert(0, 0)
    for i in range(1, len(line)):
        line[i] += line[i - 1]
    scale = []
    for i in range(len(line) - 1):
        scale.append([line[i], line[i + 1]])
    for i in range(len(scale)):
        weights[i] = scale[i]
    random_number = random.random()
    for item in weights.values():
        if item[0] <= random_number <= item[1]:
            for i in weights.keys():
                if weights[i] == item:
                    return i
