sizeLimit = 42
zanderLength = float(input(" Enter the length of the Zander in centimeters:"))
if zanderLength >= sizeLimit:
    print("The Zander meets the size limit, You can keep the fish.")
else:
    difference = sizeLimit -zanderLength
    print(f"The Zander is below the size limit by {difference:.1f} centimeters.")
    print(" Kindly release the fish back into the lake.")













