
import datetime
def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month (1-12): "))
birth_day = int(input("Enter birth day (1-31): "))

age = calculate_age(birth_year, birth_month, birth_day)
print("Your age is:", age)