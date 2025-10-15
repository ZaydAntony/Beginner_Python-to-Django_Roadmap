from datetime import date;

current_year = date.today().year
print(current_year)


name =str(input("Enter name: "));
age = int(input("Enter age: "));

century_difference = 100 - age;

print(f"Hello {name} you will be 100 yrs old in {current_year + century_difference}")
