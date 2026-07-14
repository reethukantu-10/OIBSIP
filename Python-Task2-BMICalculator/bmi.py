def feet_inches_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254


def calculate_bmi(weight, height_m):
    return weight / (height_m ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("=" * 40)
print("        BMI CALCULATOR")
print("=" * 40)

while True:
    try:
        weight = float(input("Enter your weight (kg): "))
        feet = int(input("Enter your height (feet): "))
        inches = int(input("Enter additional inches: "))

        if weight <= 0 or feet < 0 or inches < 0:
            print("\nWeight and height cannot be negative.\n")
            continue

        if feet == 0 and inches == 0:
            print("\nHeight must be greater than zero.\n")
            continue

        height_m = feet_inches_to_meters(feet, inches)

        bmi = calculate_bmi(weight, height_m)
        category = classify_bmi(bmi)

        print("\n========== RESULT ==========")
        print(f"Weight           : {weight:.1f} kg")
        print(f"Height           : {feet}' {inches}\"")
        print(f"Height (meters)  : {height_m:.2f} m")
        print(f"BMI              : {bmi:.2f}")
        print(f"Category         : {category}")
        print("============================\n")

    except ValueError:
        print("\nPlease enter valid numeric values.\n")
        continue

    choice = input("Do you want to calculate again? (yes/no): ").strip().lower()

    if choice != "yes":
        print("\nThank you for using the BMI Calculator!")
        break