monthly_income =int(input("Enter your monthly_income")
monthly_expenses =int(input("Enter your total monthly_expenses:"))
monthly_savings = monthly_income - monthly_expenses
yearly_savings = monthly_savings * 12
yearly_income = monthly_savings * 12 * 0.05
projected_savings = yearly_savings + yearly_income
print(f"your monthly savings are {monthly_savings}")
print(f"projected savings after one year with interest is {projected_savings}")

