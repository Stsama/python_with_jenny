# Here we  are supposed to calculate number of days,,week and month spend on earth if we live till 90 years
current_age = int(input("Enter your age\n"))
remaining_age = 90 - current_age 
nbr_of_days = remaining_age * 365
nbr_of_weeks = remaining_age * 52
nbr_of_months = remaining_age * 12

print(f"you have {nbr_of_days} days, {nbr_of_weeks} weeks and {nbr_of_months} month")