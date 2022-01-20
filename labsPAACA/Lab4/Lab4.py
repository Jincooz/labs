from math import sqrt
import math
import random

def f1(x,y,z):
    return -x*x-y*y+z
def f2(x,y, a):
    return x*x+y*y-a*x
def f3(z):
    return z
def Monte_Carlo(start_x, end_x, start_y, end_y, start_z, end_z, a , N):
    count = 0
    for i in range(N):
        x = random.randrange(math.floor(start_x*1000000), math.floor(end_x*1000000), math.floor((end_x-start_x)))/1000000
        y = random.randrange(math.floor(start_y*1000000), math.floor(end_y*1000000), math.floor((end_y-start_y)))/1000000
        z = random.randrange(math.floor(start_z*1000000), math.floor(end_z*1000000), math.floor((end_z-start_z)))/1000000
        if(f1(x,y,z)<0 and f2(x,y, a) < 0 and f3(z) > 0):
            count += 1
    return count

print("a = ", end="")
a = float(input())
big_start_x = 0
big_end_x = a
big_start_y = -a/2
big_end_y = a/2
big_start_z = 0
big_end_z = a*a
small_start_x = a/2
small_end_x = a/2 + a/(2*sqrt(2))
small_start_y = -a/(2*sqrt(2))
small_end_y = a/(2*sqrt(2))
small_start_z = 0
small_end_z = a*a/2
V1 = (big_end_x-big_start_x)*(big_end_y-big_start_y)*(big_end_z-big_start_z)
V2 = (small_end_x-small_start_x)*(small_end_y-small_start_y)*(small_end_z-small_start_z)
p2 = V2/V1
z = 1.96
m =0.01
N = int(z*z/m/m * (1-p2)/p2)
print("p2 = ", str(p2)," N = ", str(N))
Nreal = Monte_Carlo(big_start_x,big_end_x,big_start_y,big_end_y,big_start_z,big_end_z,a,N)
p = Nreal/N
V = p * V1
m_real = z * sqrt((1-p)/(p*Nreal))
print("З ймовірністю не меншою за ", str(0.95), " можна стверджувати, що об'єм належить інтервалу [", str(V*(1-m_real)), ";", str(V*(1+m_real)), "]")