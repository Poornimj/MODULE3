Size_limit = 42
Zander_length = float(input(" Enter the length of the Zander in centimeters: "))
if Zander_length >= Size_limit:
    print(" The Zander meets the size limit, You can keep the fish.")
else:
    Difference = Size_limit - Zander_length
    print(f"The Zander is below the size limit by {Difference:.1f} centimeters.")
    print(" Kindly release the fish back into the lake.")












