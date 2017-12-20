# This is an exercise on "Importing Modules"

import this

# Importing math module, read more about this module
import math
x = math.sqrt(4)
print(x)

# Using from to import
from math import sqrt
x = sqrt(9)
print(x)

# Importing everything: This will often leads to a phenomenon called "Shadowing" caused by contaminating the namespaces
# from math import sqrt
# sqrt = 5