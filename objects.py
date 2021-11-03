# -*- coding: utf-8 -*-

class Human:

  def search(self, place):
    pass

  def take(self, food):
    self.food = food

  def open_mouth(self):
    pass

  def eat(self):
    print(self.food + "を食べました")

  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name


# オブジェクトの生成時は、変数=クラス名()

hito = Human() # オブジェクト化
hito.take("Bana")
hito.eat()
hito.setName("山田隆")
print(hito.getName())
