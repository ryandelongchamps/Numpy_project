import numpy as np
import random


#2 rows and 3 columns.... 1,2,3 are first row, within each element each item represents a column
arr01 = np.array([[1,2,3],[4,5,6]])

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

for row in arr01:
    print(row)
    for col in row:
        print(col, end= ' ')
    print()

for i in arr01.flat:
    print(i, end = ' ')


arr03 = np.zeros(5)

#create 2 rows and 4 columns with all ones
arr04 = np.ones((2,4), dtype = int)

#create 3 rows and 5 columns with all 13
arr05 = np.full((3,5),13)


a = np.array([[random.randint(1,10) for i in range(5)],
            [random.randint(1,10) for i in range(5)]])


b = np.array(np.random.randint(1,10,size = (2,5)))

arr06 = np.arange(5)

#show values between 5 and 10
arr07 = np.arange(5,10)

#show values between 10 and 1 stepping down every 2
arr08 = np.arange(10,1,-2)


#create values equally spaced between a range
arr09 = np.linspace(0.0,1.0,num=5)

#create array from 1-20 and then put into 4 rows and 5 columns
arr10 = np.arange(1,21).reshape(4,5)


#use BROADCASTING to apply functions to all elements in an array
num01 = np.arange(1,6)
num02 = num01 * 2
num03 = num01 ** 3

#augmented assignment
num01 += 10

#multiplication between different vars, but ranges must be same size
num04 = num01 * num02

#see which values are higher than 13, returns true/false
num05 = num01 > 13


#see which elements in num 4 are higher than num 1, returns true/false
num06 = num04 > num01



#array of 4 students grades on 3 examps
#row = student
#col = exam
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

#calculate average on all rows for each column
grades_by_exam = grades.mean(axis=0)

#calculate average on all columns for each row
grades_by_student = grades.mean(axis=1)


print(grades_by_exam)
print(grades_by_student)

#take sqrt of numbers
num07 = np.array([1,4,9,16,25,36])
num08 = np.sqrt(num07)



#add two arrays together, have to be same size
num09 = ([10,20,30,40,50,60])
num10 = np.add(num07,num09)

#multiply numbers in an array
num11 = np.multiply(num09,5)

num12 = np.reshape(num09(2,3))
num13 = np.array(2,4,6)

num14 - np.multiply(num12,num13)




print()

