def main():
    print("-" * 55)
    print("""Welcome to the body mass index calculator!
    A measure of body fat in adults. \n """)

    unit_sys = input("""Do you use the METRIC system or the IMPERIAL system?
    Chose 1 for METRIC or 2 for IMPERIAL: """)


    if unit_sys == "1":
        print("\n You have chosen the METRIC system!")
        kg = float(input("\n What is your WEIGHT in KILOGRAMS?: "))
        cm = float(input("\n What is your HEIGHT in CENTIMETERS?: "))
        m = (cm / 100)
        bmi = (kg / m ** 2)
        bmi2 = round(bmi, 2)

        if bmi2 <= 18.5:
            cls = "underweight"
        if 18.6 <= bmi2 <= 24.9:
            cls = "in the normal range"
        if 25.0 <= bmi2 <= 29.9:
            cls = "overweight & preobese"
        if 30.0 <= bmi2 <= 34.9:
            cls = "obese class I"
        if 35.0 <= bmi2 <= 39.9:
            cls = "obese class II"
        if bmi2 >= 40.0:
            cls = "obese class III"

        print(f"\n Your BMI is equal to: {bmi2}. This means you're {cls}.")
        temp = input("Do you want to continue? Yes = 1 & No = 2: ")

        if temp == "1":
            main()
        elif temp == "2":
            print("\n Please exit the program. :)")


    elif unit_sys == "2":
        print("\n You have chosen the IMPERIAL system!")
        lb = float(input("\n What is your WEIGHT in POUNDS?: "))
        ft = float(input("\n Enter the FOOT amount of your HEIGHT:"))
        inch = float(input("\n Enter the INCH amount of your HEIGHT:"))
        h = ((ft * 12) + inch)
        bmi = ((lb * 703) / h ** 2)
        bmi2 = round(bmi, 2)
        if bmi2 <= 18.5:
            cls = "underweight"
        if 18.6 <= bmi2 <= 24.9:
            cls = "in the normal range"
        if 25.0 <= bmi2 <= 29.9:
            cls = "overweight & preobese"
        if 30.0 <= bmi2 <= 34.9:
            cls = "obese class I"
        if 35.0 <= bmi2 <= 39.9:
            cls = "obese class II"
        if bmi2 >= 40.0:
            cls = "obese class III"


        print(f"\n Your BMI is equal to: {bmi2}. This means you're {cls}.")
        temp = input("Do you want to continue? Yes = 1 & No = 2: ")
        if temp == "1":
            main()
        elif temp == "2":
            print("\n Please exit the program. :)")


    else:
        main()
main()
