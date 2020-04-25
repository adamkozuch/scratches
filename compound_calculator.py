def calculate_revenue(number_of_years, income_tax, annual_return, yearly_savings):
    result = 0
    for n in range(number_of_years):
        result += yearly_savings
        result = (result * annual_return/100) * (1 - income_tax/100) + result
    return result

x1 = calculate_revenue(20, 0, 8, 2500)
print(x1 * 0.81)

x2 = calculate_revenue(20, 18, 8, 2500)
print(x2 * 0.81)



