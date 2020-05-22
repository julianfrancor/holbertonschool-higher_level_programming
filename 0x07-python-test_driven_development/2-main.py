#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix_divided(matrix, 3))
print(matrix_divided(matrix, 1))
print(matrix)
print(type(matrix))

matrix_2 = [
    [1, 2, 3, 3],
    [4, 5, 6, 7]
]

print(matrix_divided(matrix_2, 3))
print(matrix_divided(matrix_2, 1))
print(matrix_2)
print(type(matrix_2))

matrix_3 = [
    [1.3, 2.5, 3.6, 4.5],
    [4.7, 5.3, 6, 7.2]
]
print(matrix_divided(matrix_3, 3))
print(matrix_3)
print(type(matrix_3))


'''matrix_4 = "Hello world!"
print(matrix_divided(matrix_4, 3))
print(matrix_4)
print(type(matrix_4))'''


matrix_5 = [
    [1, 2, 3, 3],
    [4, 5, 6, 7],
    [2, 7, 9, 5],
    [14, 25, 12, 4]
]
print(matrix_5)
print(matrix_divided(matrix_5, 4))
print(type(matrix_5))

'''matrix_6 = [
    [],
    [4, 5, 6]
]

print(matrix_6)
print(matrix_divided(matrix_6, 3))
print(matrix_divided(matrix_6, 1))
print(type(matrix_6))

matrix_6 = []

print(matrix_6)
print(matrix_divided(matrix_6, 3))
print(matrix_divided(matrix_6, 1))
print(type(matrix_6))'''


matrix_7 = [
    [1, 2, 3, 3],
    [4.5, 5.4, 6.3, 7.7]
]
print("Matrix 7")
print(matrix_7)
print(matrix_divided(matrix_7, 3))
print(matrix_divided(matrix_7, 1))
print(type(matrix_7))

print("------------------")

'''matrix_8 = [
    [1, 3, "hello", "julian"],
    [4.5, 5.4, 6.3, 7.7]
]

print(matrix_8)
print(matrix_divided(matrix_8, 3))
print(matrix_divided(matrix_8, 1))
print(type(matrix_8))'''

matrix_9 = [[-1, -2, -3], [-4, -5, -6]]

print(matrix_9)
print(matrix_divided(matrix_9, 3))
print(matrix_divided(matrix_9, 1))
print(type(matrix_9))


