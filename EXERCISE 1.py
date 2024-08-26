size_limit = 42
zander_length = float(input("Enter the length of the zander in centimeters: "))

if zander_length >= size_limit:
    print("The zander meets the size limit, You can keep the fish.")
else:
    difference = size_limit - zander_length
    print(f"The zander is below the size limit by {difference:.1f} centimeters.")
    print(" Kindly release the fish back into the lake.")