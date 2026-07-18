import random
import string

characterList = ""

#Getting password length
while True:
    try:
        length = int(input("Enter password length: "))
        if length > 0:
            break
        print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

#Getting password complexity
print('''Choose the complexity of the password:
1.Weak
2.Strong
3.Very Strong''')

while True:
    try:
        complexity = int(input("Choose Complexity(1-3):"))
        if complexity == 1:
            characterList += string.ascii_letters
            break
        elif complexity == 2:
            characterList += string.digits + string.ascii_letters
            break
        elif complexity == 3:
            characterList += string.punctuation +string.ascii_letters + string.digits
            break
        else:
            print("Please pick a valid option (1,2 or 3)!")
    except ValueError:
        print("Invalid input! Please enter a number.")

password = random.choices(characterList, k = length)
print("The random password is " + "".join(password))