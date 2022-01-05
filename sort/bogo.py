# -*- coding: utf-8 -*-
import random

def in_order(numbers):
  # len()は、要素数の取得
  # all()は、全て同じ結果だったら、trueを返す
  return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
  # for i in range(len(numbers) - 1):
  #   if numbers[i] > numbers[i + 1]:
  #     return False
  # return True


def bogo_sort(numbers):
  while not in_order(numbers):
    random.shuffle(numbers)
  return numbers


if __name__ == '__main__':
  nums = [random.randint(0, 1000) for _ in range(10)]
  print(bogo_sort(nums))
