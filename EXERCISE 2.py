cabinClass = input("Please enter the cabin class (LUX, A, B, C):")
if cabinClass == "LUX" or cabinClass == "lux":
    print("LUX: upperDeck cabin with a balcony.")
elif cabinClass == "A" or cabinClass =="a":
    print("A: Above the car deck, equipped with a window.")
elif cabinClass == "B" or cabinClass =="b":
    print("B: Windowless cabin above the car deck.")
elif cabinClass == "C" or cabinClass =="c":
    print("C: Windowless cabin below the car deck")
else:
    print("Invalid cabin class")


