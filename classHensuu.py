# -*- coding: utf-8 -*-

# クラス変数

class Human:
  age = 1
  # クラス変数はクラスに定義される変数である
  # インスタンスごとに変数が異なる→インスタンス変数 クラス全てに共通する変数→クラス変数

  def getAge(self):
    print(self.age)

human = Human()
print(human.age)
