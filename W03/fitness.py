# from distutils.log import error
# from email.errors import MalformedHeaderDefect
#^^ From previous assignment?


# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("What is your gender? (Male or Female): ")
    birth_str = input("Enter your date of birth (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in U.S. pounds: "))
    inches = float(input("Enter your height in U.S. inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    years = compute_age(birth_str)
    weight = kg_from_lb(pounds)
    height = cm_from_in(inches) 
    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, years)
    
    #Prints age, weight in kg, height in cm, BMI, and BMR.
    # Print the results for the user to see.
    print("These are the specifications given: ")
    print(f"Age:(yrs. old) {years}")
    print(f"Weight in KG: {weight:.2f}")
    print(f"Hieght in CM {height:.2f}")
    print(f"Your BMI rating is: {bmi:.2f}")
    print(f"Your BMR rating is: {bmr:.1f}")
    print("Thanks for using the BMI & BMR calulator")
    
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 2
        #changed 1 to 2. With one, the age was one year higher than example. Only chnage made in year formula.

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight = pounds * 0.45359237
    return weight


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height = inches * 2.54

    return height


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / height**2
    return bmi


def basal_metabolic_rate(gender, weight, height, years):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
     
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * years)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * years)
    else:
        print("gender error")
    return bmr


# Call the main function so that
# this program will start executing.
main()