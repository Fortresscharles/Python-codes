
from math import *
class quadra():

    a = int(input("enter no1:"))
    b = int(input("enter no2:"))
    c = int(input("enter no3:"))
    d = -b
    e = b*b
    f = 4*a*c
    g = 2*a
    h = e-f
    i = sqrt(h)
    j = d+i
    k = d-i
    l = j/g
    m = k/g

t2 = quadra()
print(f'X = {t2.l}')
print("or")
print(f'X = {t2.m}')
print(f'X = {t2.l}' + " or " + f'X = {t2.m}')