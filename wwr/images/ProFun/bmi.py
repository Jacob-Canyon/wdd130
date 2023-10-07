from datetime import datetime

def main():


#setting up the inputs

    gender = input("Select gender M/F: ")
    gender = gender.lower()
    birth_str = input("Enter date of birth in this format - YYYY-MM-DD: ")
    lbs_weight = float(input("Enter weight in US pounds: "))
    in_height = float(input("Height in US inches: "))

#calling the functions
    
    age = compute_age(birth_str)
    weight = kilo_from_lbs(lbs_weight)
    height = cm_from_in(in_height)
    
    BMI = body_mass_index(height, weight)
    BMR = basal_metabolic_rate(gender, weight, height, age)
    
    print(f"Age: {age}")
    print(f"{weight:.2f}")
    print(height)
    print(f" Body Mass Index: {BMI}")
    print(f"Basal meta rate: {BMR:.1f}")




def compute_age(birth_str):
     birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
     today = datetime.now()
     years = today.year - birthdate.year
     if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

     return years



def kilo_from_lbs(lbs_weight):

    kilo_weight = lbs_weight * 0.453592

    return kilo_weight

def cm_from_in(in_height):
    
    cm_height = in_height * 0.0254

    return cm_height

def body_mass_index(height, weight):

    BMI = (10000 * weight)/ height**2

    return BMI

def basal_metabolic_rate(gender, weight, height, age):

    if gender == "m":

        BMR = float(88.362 + 13.397 * weight + 4.799 * height - 5.677 * age)
        return BMR

    else:

        BMR = float(447.593 + 9.247 * weight + 3.098 * height - 4.330 * age)
        return BMR
    
main()


    




    