'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''

L1 = int(input())
L2 = int(input())
L3 = int(input())
ACE_lab = input()  # This will take the lab allocated for ACE training

# Exclude the ACE lab and find the minimum seating capacity among the remaining labs
if ACE_lab == "L1":
    if L2 < L3:
        print("L2")
    else:
        print("L3")
elif ACE_lab == "L2":
    if L1 < L3:
        print("L1")
    else:
        print("L3")
else:  # ACE_lab is "L3"
    if L1 < L2:
        print("L1")
    else:
        print("L2")
