from mathutils import BasicMath 
from mathutils import AdvancedMath

basic = BasicMath()
advance = AdvancedMath()
print("add", BasicMath.add(10, 5))
print("sub", BasicMath.sub(10, 5))
print("power", advance.power(2, 3))
print("factorial", advance.factorial(5))