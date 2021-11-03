# -*- coding: utf-8 -*-

class Student:

  def __init__(self, name, id, score = 0):
    self.name = name
    self.id = id
    self.score = score

  def getId(self):
    return self.id

  def getName(self):
    return self.name

  def setScore(self, score):
    self.score = score

  def getScore(self, score)
    return self.score


class CalcScore:

  def __init__(self)
    self.students = []

  def addStudent(self, student)
    self.students.append(student)

  def average():
    v = 0
    for i in self.students:
      v += i.getScore()
      ave_v = v / len(self.students)
      return ave_v

pl = Student("たかし", 10)
pl.setScore(80)
p2 = Student("鈴木", 11, score=79)
p3 = Student("鈴木", 12, score=84)
