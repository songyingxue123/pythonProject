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
'''
创建思路：想通过创建父类的构造函数，再定义子类过程当中无需再定义类类变量，减少代码的定义及使用。
问题：工厂创建子类对象时报错，原因创建英雄对象需要四个参数，创建子类对象函数有两个固定的参数，传参数是无法进行self的创建。
解决思路：重写子类构造函数
'''


class Hero:
    hp = 0
    power = 0
    name = ''
    slogan = ''

    def __init__(self, hp, power, name, slogan):

        """
       :param hp: 英雄血量
       :param power: 英雄攻击力
       :param name: 英雄名称
       """

        self.hp = hp
        self.power = power
        self.name = name
        self.slogan = slogan

    # 构造函数没有返回值
    # 获得作为攻击对象的参数方法
    def getValue(self):
        return self.hp, self.power, self.name

    def speak_lines(self):
        """
       问题：此函数，在想是否可以再fight中进行调用，则编译器报错。类中除了main函数中其余的函数不能够相互调用嘛？？？？
        :return:
        """
        print(self.slogan)

    def fight(self, fighter_hp: object, fighter_power: object, fighter_name: object) -> object:
        """
        问题1：这个过程是否可以使用多线程完成，该位置的攻击应该是同时进行的，而不是线性进行，由于时间有限先到这位置
        问题2 上面的object是怎么回事，再调用是使用时，报错通过使用格式纠正方法写出的不明白其原理
        :param fighter_hp: 对手血量
        :param fighter_power: 对手攻击力
        :param fighter_name: 对手名称
        :return:
        """
        while True:
            self.hp = self.hp - fighter_power
            if self.hp <= 0:
                print(f"{fighter_name}获得最终胜利")
                break
            fighter_hp = fighter_hp - self.power
            if fighter_hp <= 0:
                print(f"{self.name}获得最终胜利")
                # speak_lines()这个位置中不可以调用类的中的方法嘛？只可以main()中可以调用嘛
                break
