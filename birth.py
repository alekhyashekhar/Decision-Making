'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''

# Get the last two digits of the birth year and current year from the user
birth_year_last_two = int(input("Enter the last two digits of your birth year: "))
current_year_last_two = int(input("Enter the last two digits of the current year: "))

# Calculate the full years based on the input
if current_year_last_two < birth_year_last_two:
    # Assume the current year is in the next century
    current_year_full = 2000 + current_year_last_two
else:
    # Assume the current year is in the same century
    current_year_full = 1900 + current_year_last_two

birth_year_full = 1900 + birth_year_last_two

# Calculate age
age = current_year_full - birth_year_full

# Print the age
print(age)
