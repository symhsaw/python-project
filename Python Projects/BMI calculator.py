def calculate_bmi():
    print("Welcome to the BMI Calculator!")

    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                raise ValueError("Height must be a positive number.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            break
        except ValueError as e:
            print(e)

    # Calculate BMI
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    # Provide health advice based on BMI categories
    if bmi < 18.5:
        print("Category: Underweight. Advice: You may need to gain weight. Consult a healthcare provider for guidance.")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight. Advice: Maintain a balanced diet and regular exercise.")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight. Advice: Consider healthy eating and increasing physical activity.")
    else:
        print("Category: Obesity. Advice: Consult a healthcare provider for personalized advice and support.")

if __name__ == "__main__":
    calculate_bmi()
