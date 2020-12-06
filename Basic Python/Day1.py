current_age = input("what is your age? ")
age_at_death = 90
years_to_live = age_at_death - int(current_age)
months_to_live = years_to_live * 12
weeks_to_live = years_to_live * 52
days_to_live = years_to_live * 365
print(f"You have {months_to_live} months to live, weeks to live {weeks_to_live}, days to live{days_to_live}")


