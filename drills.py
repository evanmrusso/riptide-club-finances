# Midterm Exam Drills

# Drill A: Concession Stand

Nachos_price = 4.50
Nachos_sold = 70
Bottled_water_price = 1.25
Bottled_water_sold = 148
tax_rate = 0.06
Starting_cash = 75.00
water_bottles_per_case = 24
Sales_goal = 500

# Calculate total revenue of Nachos and Bottled Water
Nachos_revenue = Nachos_price * Nachos_sold
Bottled_water_revenue = Bottled_water_price * Bottled_water_sold

# Calculate total revenue
total_sales = Nachos_revenue + Bottled_water_revenue

# Calculate Tax
tax = total_sales * tax_rate

# Calculate total amount to be collected
total_amount = (total_sales + tax) + Starting_cash

# Amount of full cases of water used
full_cases_used = Bottled_water_sold // water_bottles_per_case

# Bottles sold from the partly used cases
Bottle_from_partial_cases = Bottled_water_sold % water_bottles_per_case

# If the stand hit $500 sales goal
is_hit_sale_goal = total_sales >= Sales_goal


print(f"total_sales: ${total_sales:,.2f}")
print(f"tax: ${tax:,.2f}")
print(f"total_amount: ${total_amount:,.2f}")
print(f"full_cases_used: {full_cases_used}")
print(f"Bottles_sold_from_partial_cases: {Bottle_from_partial_cases}")
print(f"is_hit_sale_goal: {is_hit_sale_goal}")
