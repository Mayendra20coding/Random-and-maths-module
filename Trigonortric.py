import math
angle_degrees = float(input("Enter an angle in degrees: "))
angle_radians = math.radians(angle_degrees)
sine_value = math.sin(angle_radians)
cosine_value = math.cos(angle_radians)
tangent_value = math.tan(angle_radians)
print(f"sin({angle_degrees}°) = {sine_value}")
print(f"cos({angle_degrees}°) = {cosine_value}")
print(f"tan({angle_degrees}°) = {tangent_value}")