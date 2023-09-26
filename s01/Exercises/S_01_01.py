import math
#importtation of the math library giving us access to the sin function

angle = 60

sinus = math.sin(angle/180*math.pi)
#conversion from degrees to radian and then using the sin function to return the sinus

print(f"The sinus of {angle} is {sinus}")
#using the f print to include the different variable directly in the function