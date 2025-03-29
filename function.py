def calculate_discounted_price(price, discount_percent):

    if discount_percent >= 20:
       final_price = price - (price * discount_percent / 100)
       return final_price
    else:
       return price
    
#print(calculate_discounted_price(500, 25))# 25% discount applied
#print(calculate_discounted_price(500, 15))# No discount applied
#print(calculate_discounted_price(500, 10))# No discount applied
#print(calculate_discounted_price(500, 20))# 20% discount applied
# Prompts the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discounted_price(price, discount_percent)

# Print the final price
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    # If no discount is applied, print the original price
    # and indicate that no discount was applied
    #print(f"The final price after applying the discount is: {final_price}")
    print(f"No discount applied. The original price is: {price}")

