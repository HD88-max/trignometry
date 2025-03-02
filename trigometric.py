import math
userinput = float(input("Enter a number: "))
userinput2 = input("Enter s for sin, c for cos and t for tangent: ")
if userinput2 == "s" or userinput2 == "S":
    print("The value is {0}.".format(math.sin(userinput)))    
elif userinput2 == "C" or userinput2 == "c":
    print("The value is {0}.".format(math.cos(userinput)))   
elif userinput2 == "t" or userinput2 == "T":
    print("The value is {0}.".format(math.tan(userinput)))
else:
    print(False)