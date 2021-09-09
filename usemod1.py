import sys
import os
from john.math import geometry
import john

print(john.ANIMAL)

# find and run geometry.py


print(geometry.circle_area(18))

print(geometry.square_area(15))

# 1. current folder
print(os.getcwd())
# 2. folders in PYTHONPATH
print(os.getenv("PYTHONPATH"))
# 3. folders and archives in sys.prefix/lib
print(sys.prefix)  # + '/lib'
print()

for path in sys.path:
    print(path)





