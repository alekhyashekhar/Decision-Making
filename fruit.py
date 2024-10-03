'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''

# Get the total cost for a dozen bananas and the selling price of one banana
X = float(input("Enter the total cost of a dozen bananas (X): "))
Y = float(input("Enter the selling price of one banana (Y): "))

# Calculate the cost price per banana
cost_price_per_banana = X / 12

# Calculate the total selling price for a dozen bananas
total_selling_price = Y * 12

# Calculate profit or loss
profit_or_loss = total_selling_price - X

# Determine and print the result
if profit_or_loss > 0:
    print(f"Profit : Rs.{profit_or_loss:.2f}")
elif profit_or_loss < 0:
    print(f"Loss : Rs.{abs(profit_or_loss):.2f}")
else:
    print("No Profit No Loss")
