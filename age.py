from datetime import date, datetime

birth_date = input("Enter your date of birth (DD-MM-YYYY): ")
birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()
today = date.today()
age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month , birth_date.day):
    age -= 1

print(f"You are {age} years old.")