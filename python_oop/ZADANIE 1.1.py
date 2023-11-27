# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Student:
   def __init__(self, name, marks):
       self.name = name
       self.marks = marks

   def is_passed(self):
       average_marks = sum(self.marks) / len(self.marks)
       return average_marks > 50


student1 = Student("basia", [75,30,40])
student2 = Student("asia", [65,90,20])

result1 = student1.is_passed()
result2 = student2.is_passed()

print(f"{student1.name} passed: {result1}")
print(f"{student2.name} passed: {result2}")

