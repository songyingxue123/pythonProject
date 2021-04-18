import police

import timo


class HeroFactory:
    def createHero(self, name, hp, power):
        # print(f"{name}")
        if name == 'timo':
            # print(f"{hp},{power}")
            t = timo.Timo()
            # print(t.createTimo(hp, power))
            # retrun timo.Timo.createPolice(hp,power)报错不知道为啥报错，这样创建的对象是父类对象嘛，不是子类对象因为参数不同？？？
            return t.createTimo(hp, power)

        elif name == 'police':
            t = police.Police()
            return t.createPolice(hp, power)
        else:
            raise Exception("未拥有该人物角色！！")


if __name__ == '__main__':
    h = HeroFactory()
    timo1 = h.createHero('timo', 1000, 20)
    police1 = h.createHero('police', 2000, 300)
    timo1.fight(*police1.getValue())
    timo1.speak_lines()
    hero1 = h.createHero("hero1", 200, 20)

