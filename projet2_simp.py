from math import acos, trunc, pi

valid=False
while valid == False:
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    valid = (a > 0) and (a+b > c)
    if valid == False:
        print("forme impossible")

while not (a <= b and b <= c):
    if (a > b):
        x = b
        b = a
        a = x

    if (b > c):
        x = c
        c = b
        b = x

print(a, b, c)

A=acos((a ** 2 + b ** 2- c ** 2)/(2 * b * a))
A=trunc(A*180/pi)

if (a == b and b == c):
    print("triangle équilateral")
elif (a == b or b == c) and A == 90:
    print("triangle isocele rectangle")
elif (a == b or b == c):
    print("triangle isocele")
elif(A > 90):
    print("triangle obtus d'angle", A)
else:
    print("triangle quelconque")