from Hero import *


class Police(Hero):
    # 这个位置静态方法，与普通的方法的区别
    def __init__(self):
        pass

    def createPolice(self, hp, power):
        return Hero(hp, power, 'police', '见识一下法律的子弹')

