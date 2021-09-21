from sys import *
from pygame.locals import *
import pygame
from src.constant import *
import random


class Network:
    def __init__(self):
        self.title = Title
        self.width = Width
        self.height = Height
        self.screen = None
        self.M = M
        self.M0 = M0
        self.Nodes = []
        self.seq = []
        self.init_pygame()
        self.init_nodes()
        self.init_arcs()
        self.export_datas()
        self.update()

    def init_nodes(self):
        # 初始化一个节点为4的完全图
        for i in range(self.M0):
            pos = [random.randint(50, self.width - 50), random.randint(50, self.height - 50)]
            self.Nodes.append(Node(pos, i))
            self.seq.append(i)
            pygame.draw.circle(self.screen, Green, pos, Node_size)
            # time.sleep(0.5)
            pygame.display.update()

    def init_arcs(self):
        # 初始化节点之间的连边
        s, match = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]], []
        for i in self.Nodes:
            for j in self.Nodes:
                if [i.seq, j.seq] in s:
                    match.append([i, j])
        for i in match:
            i[0].update_degree()
            i[1].update_degree()
            pygame.draw.line(self.screen, Purple, i[0].position, i[1].position, 1)
            pygame.display.update()

    def add_node(self):
        # 通过巴拉巴西-阿尔伯特模型，选择新增节点连接的边
        n = []
        while len(n) < self.M:
            t = choose_node(self.Nodes)
            if t not in n:
                n.append(t)
        # 添加节点
        pos = [random.randint(50, self.width - 50), random.randint(50, self.height - 50)]
        self.Nodes.append(Node(pos, len(self.seq), M))
        self.seq.append(len(self.seq))
        # 画出新节点
        pygame.draw.circle(self.screen, Green, self.Nodes[-1].position, Node_size)
        # 更新被选择连接的节点的度数,并画出连边
        for i in n:
            for j in self.Nodes:
                if j.seq == i:
                    j.update_degree()
                    pygame.draw.line(self.screen, Purple, j.position, self.Nodes[-1].position, 1)

    def export_datas(self):
        pass

    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill(white)

    def update(self):
        while True:
            self.event_handler()
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    # 当按下回车键时，新增加2个节点
                    for i in range(2):
                        self.add_node()
                if event.key == K_r:
                    # 当按下R键时，重新绘制一下所有节点
                    for node in self.Nodes:
                        pygame.draw.circle(self.screen, Green, node.position, Node_size)
                        pygame.display.update()
                if event.key == K_m:
                    # 当按下M键时，输出一下所有节点的度
                    degrees = []
                    for i in self.Nodes:
                        degrees.append(i.degree)
                    degrees.sort(reverse=True)
                    print(degrees)
