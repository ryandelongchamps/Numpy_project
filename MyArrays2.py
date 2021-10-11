import numpy as np
import random

#rows = student
#cols = test
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

student1 = grades[1]

student0_test1 = grades[0,1]

#upper bound not included
#using colon to get range (sequential)
students0_1 = grades[0:2]

#to select all tests for students 1 and 3
students1and3 = grades[[1,3]]

#select students 1 and 3 but only test 2

students1and3test2 = grades[[1,3],2]

all_students_test0 = grades[:,0]

all_students_test1and2 = grades[:,0:2]


grades = np.random.randint(60,101,12).reshape(3,4)

grades.mean()

#average by col
grades.mean(axis = 0)

#average by row
grades.mean(axis = 1)


#shallow copies (use view)
numbers = np.arange(1,6)
numbers_view = numbers.view()

numbers[1] *= 10

numbers_view[1] /= 10

numbers_slice = numbers[0:3]

numbers[1] *= 20


#deep copies (use copy)
numbers_copy = numbers.copy()

numbers[1] *= 10


grades = np.array([[87,96,70],[100,87,90]])


#reshape method produces a shallow copy
grades_reshaped = grades.reshape(1,6)

#resize 
grades_resized = grades.resize(1,6)

#flatten creates a deep copy
grades_flattened = grades.flatten()

#ravel creates a shallow copy
grades_ravel = grades.ravel()

grades_ravel[0] = 100

grades_flattened[1] = 100

grades = np.array([[87,96,70],[100,87,90]])

grades.T


grades2 = np.array([[94,77,90],[100,81,82]])

h_grades = np.hstack((grades,grades2))

v_grades = np.vstack((grades,grades2))




print()