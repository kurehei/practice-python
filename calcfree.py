# -*- coding: utf-8 -*-

import math

class caclFree:
  def __init__(self):
    self.shipping_free = 0
    self.tax_rate = 0.08
    self.value = 0

  def addItem(self, price):
    self.value += price
    print(self.value)
  # 具体的な計算を行う
  def calc(self):
    total = self.value + self.shipping_free
    tax = math.ceil(total * self.tax_rate)
    v = math.ceil(total + tax)
    return v
feel = caclFree() # インスタンス化
feel.addItem(800)
feel.addItem(500)
print(feel.calc(), "円")
