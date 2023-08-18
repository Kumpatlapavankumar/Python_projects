# Function to determine BMI category based on BMI value
def determine_bmi_category(child_name, bmi_value):
    if bmi_value < 16:
        print("BMI of {0} is {1} and he (she) is Severely Underweight.".format(child_name, bmi_value))
    elif 16 <= bmi_value < 18.5:
        print("BMI of {0} is {1} and he (she) is Underweight.".format(child_name, bmi_value))
    elif 18.5 <= bmi_value < 25:
        print("BMI of {0} is {1} and he (she) is Healthy.".format(child_name, bmi_value))
    elif 25 <= bmi_value < 30:
        print("BMI of {0} is {1} and he (she) is Overweight.".format(child_name, bmi_value))
    elif bmi_value >= 30:
        print("BMI of {0} is {1} and he (she) is Obese.".format(child_name, bmi_value))

# Function to calculate total calories consumed by a child
def calculate_calories(total_calories_consumed):
    calories_count = {"Milk": 100, "Vegetables": 85, "Meat": 143, "Lentils": 113, "Egg": 155, "Rice": 130}
    total_calories = 0
    for food, quantity in total_calories_consumed.items():
        calorie = quantity
        while calorie != 0:
            if calorie - 100 >= 0:
                calorie -= 100
                total_calories += calories_count[food]
            else:
                fraction = calorie / 100
                total_calories += calories_count[food] * fraction
                calorie = int(calorie - (calories_count[food] * fraction))
                break
    return total_calories

# Function to assess nourishment based on age and total calories intake
def assess_nourishment(child_name, child_age, total_calories_intake):
    if 0 <= child_age < 2:
        if total_calories_intake < 800:
            print("The daily calorie consumption of {0} is 800 and he (she) is taking {1}, "
                  "he or she requires more calories and is under-nourished.".format(child_name, total_calories_intake))
        else:
            print("The daily calorie consumption of {0} is 800 and he (she) is taking {1}, he or she is nourished.".format(child_name, total_calories_intake))
    elif 2 <= child_age < 4:
        if total_calories_intake < 1400:
            print("The daily calorie consumption of {0} is 1400 and he (she) is taking {1}, "
                  "he or she requires more calories and is under-nourished.".format(child_name, total_calories_intake))
        else:
            print("The daily calorie consumption of {0} is 1400 and he (she) is taking {1}, he or she is nourished.".format(child_name, total_calories_intake))
    elif 4 <= child_age < 8:
        if total_calories_intake < 1800:
            print("The daily calorie consumption of {0} is 1800 and he (she) is taking {1}, "
                  "he or she requires more calories and is under-nourished.".format(child_name, total_calories_intake))
        else:
            print("The daily calorie consumption of {0} is 1800 and he (she) is taking {1}, he or she is nourished.".format(child_name, total_calories_intake))
    else:
        print("He (or She) is not a child!")

# Main program
print("WELCOME TO CHILD NUTRITION CALCULATOR")
child_name = input("Name: ")
child_age = int(input("Age: "))
child_height = float(input("Height (inches): "))
child_weight = float(input("Weight (lb): "))
print("")

print("Calorie Consumption of child")
calories_consumed = {}
calories_consumed["Milk"] = int(input("Milk: "))
calories_consumed["Vegetables"] = int(input("Vegetables: "))
calories_consumed["Meat"] = int(input("Meat: "))
calories_consumed["Lentils"] = int(input("Lentils: "))
calories_consumed["Egg"] = int(input("Egg: "))
calories_consumed["Rice"] = int(input("Rice: "))
print("")

# Calculate BMI
bmi = (child_weight / (child_height ** 2)) * 703
bmi_rounded = round(bmi, 2)

# Determine and display BMI category
determine_bmi_category(child_name, bmi_rounded)
print("")

# Calculate total calories consumed
total_calories = calculate_calories(calories_consumed)
total_calories_rounded = round(total_calories, 2)

# Assess and display nourishment status
assess_nourishment(child_name, child_age, total_calories_rounded)
