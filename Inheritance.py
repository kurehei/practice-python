# 元になったクラスを基底クラス、新たに定義されたクラスをサブクラスと呼ぶ
# class 派生クラス(基底クラス)
#   ....

class Car:
  def __init__(self, weight):
    self.weight = weight

# 基底クラス
class Wagon(Car):
  def __init__(self, weight):
    super().__init__(weight)
