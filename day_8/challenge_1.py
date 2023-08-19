# paint
import math
def fun(height, width, can):
    area = height* width
    can_needed = math.ceil(area/can)
    print(f"u need {can_needed} can")
fun(5,5,5)
