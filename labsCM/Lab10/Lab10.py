sizex = 200
sizey = 200
x_start = 0
y_start = 0
x_end = 0.9
y_end = 0.9
hx = (x_end-x_start) / (sizex-1)
hy = (y_end-y_start) / (sizey-1)
matrix  = [[0 for element in range(sizex)] for row in range(sizey)]
top_matrixdy = [0 for i in range(sizex)]
bot_matrixdy = [0 for i in range(sizex)]
x = [i * hx + x_start for i in range(sizex)]
y = [i * hy + y_start for i in range(sizey)]
################################################################
def u_for_x0(y):
    return 0.3 * y * y + 0.5 * y + 1.3
def u_for_xL1(y):
    return 0.3 * y * y + 1.85 * y + 1.687
def uy_for_y0(x):
    return 1.5 * x + 0.5 
def uy_for_yL2(x):
    return 1.5 * x + 1.04
for i in range(sizey):
    matrix[i][0] = u_for_x0(y[i])
    matrix[i][-1] = u_for_xL1(y[i])
for i in range(sizex):
    top_matrixdy[i] = uy_for_y0(x[i])
    bot_matrixdy[i] = uy_for_yL2(x[i])
matrix[0][0] = matrix[-1][0] = matrix[0][-1] = matrix[-1][-1] = 0
################################################################
real_matrix  = [[0 for element in range(sizex)] for row in range(sizey)]

def u(x, y):
    return -0.3 * (x*x - y*y) + 1.5 * x *y + 0.7 * x + 0.5 * y + 1.3

for i in range(sizey):
    for j in range(sizex):
        real_matrix[i][j] = u(x[j],y[i])
################################################################
for i in range(sizey):
    for j in range(sizex):
        print(round(matrix[i][j],3), end = " ")
    print()
for i in range(1, sizey - 1):
    dliniar = (matrix[i][-1] - matrix[i][0]) / (sizey+1)
    for j in range(1,sizex-1):
        matrix[i][j] = dliniar * j + matrix[i][0]

for i in range(1, sizex - 1):
    matrix[0][i] = matrix[1][i] - hy * top_matrixdy[i]
    matrix[-1][i] = matrix[-2][i] + hy * bot_matrixdy[i]

def itteration(matrix):
    sizex = len(matrix[0])
    sizey = len(matrix)
    matrix2 = [[0 for element in range(sizex)] for row in range(sizey)]
    for i in range(1, sizey - 1):
        for j in range(1, sizex - 1):
            justh_hart = (2/(hx*hx) + 2/(hy*hy))
            dx_part = (matrix[i][j-1]+matrix[i][j+1])/(hx*hx)
            dy_part = (matrix[i-1][j]+matrix[i+1][j])/(hy*hy)
            matrix2[i][j] = (dx_part + dy_part) / justh_hart
    for i in range(sizey):
        matrix2[i][0] = matrix[i][0]
        matrix2[i][-1] = matrix[i][-1]
    for i in range(1, sizex - 1):
        matrix2[0][i] = matrix2[1][i] - hy * top_matrixdy[i]
        matrix2[-1][i] = matrix2[-2][i] + hy * bot_matrixdy[i]
    return matrix2

def div_matrix_abs(matrix, matrix2):
    sizex = len(matrix[0])
    sizey = len(matrix)
    matrix3 = [[0 for element in range(sizex)] for row in range(sizey)]
    for i in range(sizey):
        for j in range(sizex):
            matrix3[i][j] = abs(matrix[i][j] - matrix2[i][j])
    return matrix3

def div_matrix(matrix, matrix2):
    sizex = len(matrix[0])
    sizey = len(matrix)
    matrix3 = [[0 for element in range(sizex)] for row in range(sizey)]
    for i in range(sizey):
        for j in range(sizex):
            matrix3[i][j] = matrix[i][j] - matrix2[i][j]
    return matrix3

print(max(max(matrix)))

i = 0
while True:
    matrix2 = itteration(matrix)
    div = max(max(div_matrix_abs(matrix,matrix2)))
    if(div < 1E-6):
        print("In result {%s} iterations" % (i))
        matrix = matrix2
        break
    matrix = matrix2
    i += 1


print()
div_mat = div_matrix(matrix, real_matrix)
div_mat[0][0] = div_mat[-1][0] = div_mat[0][-1] = div_mat[-1][-1] = 0


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
a = np.array(div_mat)
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()
