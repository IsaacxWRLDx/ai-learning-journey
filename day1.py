name = input("What is your name? ")
hours = int(input("How many hours will you study AI today? "))

monthly_hours = hours * 30
yearly_hours = hours * 365
print("that equals", yearly_hours, "hours in a year")

print("Hello", name)
print("If you study", hours, "hours per day you will study", monthly_hours, "hours this month.")