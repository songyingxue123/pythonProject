"""
课程里面所有的演示代码，自己独立完成（基础不好的同学， 选做）
使用简单工厂方法， 实现timo 和 police 两个英雄
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是timo和police。每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力

每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜

每个英雄都一个speak_lines方法
调用speak_lines方法，不同的角色会打印（讲出）不同的台词
timo : 提莫队长正在待命
police: 见识一下法律的子弹
"""

from Hero import *


class Timo(Hero):
    # hp = 0
    # power = 0
    # name = 'timo'
    # slogan = '提莫队长正在待命'
    # # 通过创建父亲构造函数来创建对象

    def __init__(self):
        pass

    def createTimo(self, hp, power):
        return Hero(hp, power, 'timo', '提莫队长正在待命')