cabin_class = input("Please enter the cabin class (LUX, A, B, C): ")

if cabin_class == "LUX or lux":
    print("LUX: Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")