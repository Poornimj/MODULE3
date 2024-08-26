def check_leap_year():

    year = int(input("Enter a year: "))


    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = "a leap year"
    else:
        result = "not a leap year"

    # Notify the user of the result
    print(f"The year {year} is {result}.")

check_leap_year()