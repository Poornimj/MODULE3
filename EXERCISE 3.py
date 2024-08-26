def check_hemoglobin():
    
    gender = input("Enter your biological gender (male/female): ").strip().lower()
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))


    if gender == "male":
        if hemoglobin < 134:
            result = "low"
        elif 134 <= hemoglobin <= 167:
            result = "normal"
        else:
            result = "high"
    elif gender == "female":
        if hemoglobin < 117:
            result = "low"
        elif 117 <= hemoglobin <= 155:
            result = "normal"
        else:
            result = "high"
    else:
        result = "invalid"

    # Output the result
    if result == "invalid":
        print("Invalid input for gender.")
    else:
        print(f"Your hemoglobin value is {result}.")

check_hemoglobin()