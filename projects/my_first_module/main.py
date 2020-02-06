import mymath
import mymath  # will not print anything

# pi  # NameError -> could be solved via __init__

print(mymath.pi)  # 3.14159

print(mymath.area(2))  # 12.56636

print(mymath.__doc__)  # 'mymath - our example math module'

print(mymath.area.__doc__)  # 'area(r): return the area of a circle with radius r.'

from mymath import pi

print(pi)  # 3.14159

from math import pi

print(pi)  # 3.141592653589793

import math

print(mymath.pi, math.pi)  # 3.14159 3.141592653589793