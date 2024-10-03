'''
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
Ans:
a=input()
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print('Vowel')
elif(a>'a' and 'a'<a):
    print("Consonant")
else:
    print("Not an alphabet# Take input from the user
'''


a = input("Enter a character: ")
# Check if the input is a single alphabet character
if len(a) == 1 and a.isalpha():
    if a.lower() in 'aeiou':
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Not an alphabet')



