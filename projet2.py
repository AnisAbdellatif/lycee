from math import acos, degrees

def getAngle(x, y, z):
    return round(degrees(acos((pow(x, 2) + pow(y, 2) - pow(z, 2)) / (2 * x * y))))

while True:
    try:
        a, b, c = sorted([int(input(f"Segment {i}: ")) for i in ["a", "b", "c"]])
    except ValueError:
        print("Valeur non numerique")
        continue
    
    if (a > 0) and (a+b > c):
        print("Forme possible!")
        break
    print("Forme impossible!")

print(f"{a}, {b}, {c}")
type = []
angle = getAngle(a, b, c)

if a == b and b == c:
    type.append("equilateral")

elif angle > 90:
    type.append(f"obtus d'angle {angle}°")

else:
    if angle == 90:
        type.append("rectangle")

    if a == b or b == c:
        type.append("isocele")

    if type == []:
        type.append("quelconque")

print("Ce triangle est " + ' '.join(type))