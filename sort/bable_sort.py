# -*- coding: utf-8 -*-
import random



# def bable_sort(numbers):
#   last = 1
#   for i in range(len(numbers) - last):
#     if numbers[i] > numbers[i + 1]:
#       # 次の要素と比較して大きかったら、入れ替える
#        numbers[i + 1] = numbers[i]
#        last+=1
#   return numbers

def bable_sort(numbers):
  len_numbers = len(numbers)
  for i in range(len(numbers)):
    for j in range(len_numbers - 1 - i):
      if numbers[j] > numbers[j + 1]:
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
  return numbers


if __name__ == '__main__':
  # nums = [2, 5, 1, 8, 7, 3]
  nums = [random.randint(0, 1000) for _ in range(10)]
  print(bable_sort(nums))
