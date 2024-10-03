'''
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''


L1 = int(input())  # Seating capacity of L1
L2 = int(input())  # Seating capacity of L2
L3 = int(input())  # Seating capacity of L3
n = int(input())   # Number of students

# Create a dictionary to store lab names and their capacities
labs = {'L1': L1, 'L2': L2, 'L3': L3}

# Filter labs that can accommodate 'n' students
suitable_labs = {lab: capacity for lab, capacity in labs.items() if capacity >= n}

# Find the lab with the minimum unused capacity
if suitable_labs:
    best_lab = min(suitable_labs, key=suitable_labs.get)
    print(best_lab)
else:
    print("No lab can accommodate the students")
