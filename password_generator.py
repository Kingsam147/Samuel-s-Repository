import string 
import random
import sys
import os

# Goal: 
# Generates a designated number of random unique passwords and stores them in a list
# the passwords can have a specified length or random length between 8 and 30 characters


class Password: 
    def __init__(self, p): # parameter is the password itself
        self.p = p

    def __str__(self): 
        return f"{self.p}"  


# method to create random password of a designated that contains at least one upper and lower letter, a number, and a special character
def createPassword(length: int): 
    listOfCharacters = [string.ascii_uppercase, string.ascii_lowercase, string.digits, '!@#$%*']
    password: str = '' # string that's going to become password
    contains: bool # used to check password contais numbers and special characters

    for i in range(length): 
            randomList = random.choices(listOfCharacters, [1, 2, 2, 1])[0] # one of the 3 groups of letters
            char = random.choice(randomList) # character to be added to password
    
            password += char
    # need to make sure the password is somewhat secure 
    # so if the password doesn't contain an upper and lower case letter, a number, and a special character 
    # then replace a random character in the password with whatever is missing
    
    # first add a special character 
    contains = False
    for c in '!@#$%*': 
        if (c in password):
            contains = True
    # if contains still equals false then the password doesn't contain any of the special characters
    # in that case, replace a random character with a special one character
    if(contains == False):
        index: int = random.randint(0, length - 1)
        password.replace(password[index], random.choice('!@#$%*'), 1)
    
    # do the same thing to make sure temp includes a number 
    contains = False
    for d in string.digits:
        if(d in password):
            contains = True
    if(contains == False):
        index: int = random.randint(0, length - 1)
        password.replace(temp[index], random.choice(string.digits), 1) 

    # Once again do the same thing for lower case letters 
    contains = False 
    for l in string.ascii_lowercase:
        if(l in password):
            contains = True
    if(contains == False): 
        index: int = random.randint(0, length - 1)
        password.replace(password[index], random.choice(string.ascii_lowercase), 1)  

    # finally do it one last time for upper case letters 
    for u in string.ascii_uppercase: 
        if(u in password): 
            contains = True
    if(contains == False): 
        index: int = random.randint(0, length - 1)
        password.replace(temp[index], random.choice(string.ascii_uppercase), 1)    
    
    # if the string still doesn't contain a digit and special character run recursively until it does 
    containsC: bool = False
    containsD: bool = False
    containsL: bool = False 
    containsU: bool = False

    for d in string.digits:
        if(d in password):
            containsD = True
    for c in '!@#$%*': 
        if(c in password):
            containsC = True
    for l in string.ascii_lowercase: 
        if(l in password): 
            containsL = True
    for u in string.ascii_uppercase: 
        if(u in password):
            containsU = True
    if(not(containsC == True and containsD == True and containsL == True and containsU == True)):
        return createPassword(length)
    else: 
        return password

print("Program generates a unique password with an assigned key reference")    
print("1: Generate a completely random password with a random length between 10 - 15 characters")
print("2: Generate password with a designated base and adds special characters to it     \nEx.Ben****")
print("3: Enter unique a password of your choice")
print("4: Remove a password along with it's key")
print("5: List all the passwords and their keys")
print("6: Use a key to find a password")
print("7: Use a password to find a key")
print("Please select option: ", end="")

listOfPasswords = {}
length: int # length of special characters generated
key: str

# if the passwords text isn't empty than upload the passwords into the list of passwords dictionary 
# so that the passwords can be accessed in the code 
if (os.path.getsize('passwords.txt') != 0):
    try: 
        with open('passwords.txt', 'r') as file:
                    for passwords in file: 
                        words = passwords.split()
                        listOfPasswords[words[0][0: len(words[0]) - 1]] = words[1]
    except FileNotFoundError:
        print("no passwords have been saved")
        sys.exit(0)

match input():
    case('1'): 
        length = random.randint(10, 15)
        print("Length: " + str(length)) 
        # generate a random password of the designated length
        # add a password that isn't in the list 
        temp:str = createPassword(length)
        
        while (temp in listOfPasswords.values()): 
            temp = createPassword(length)
        p = Password(temp)
        print(str(p))
        key = input("please enter a key for the password: ")
        while(key in listOfPasswords.keys()):
            print(listOfPasswords)
            key = input("Please enter a new unique key: ")
        listOfPasswords[key] = p

    case('2'): 
        base: str = input("What is the string you want to append to?\n")
        length:int = int(input("how many special characters and/or numbers do you want added to it?\n")
)
        specialChars = ''.join(random.choices(string.digits + '!@#$%*', k = length))
        temp = base + specialChars
        while(temp in listOfPasswords.values()):
            specialChars = ''.join(random.choices(string.digits + '!#$*', k = length))
            temp = base + specialChars 
        p = Password(temp)
        print(p)
        key = input("Please enter a key for the password: ")
        while(key in listOfPasswords.keys()):
            print(listOfPasswords) 
            key = input("please enter a unique password")
        listOfPasswords[key] = p 
    case('3'):
        key = input("Enter key for password: ")
        p = Password(input("Enter password")) 
        if(key in listOfPasswords.keys() or p in listOfPasswords.values()): 
            print("both the key and password are already being used") 
            print("please make sure both the password and key are unique")
            sys.exit(0)
        elif(key in listOfPasswords.keys):
            print("this key is already being used")
            print("please make sure both the password and key are unique")
            sys.exit(0)
        elif(p in listOfPasswords.values()):
            print("The password is already being used")
            print("please make sure both the password and key are unique")
            sys.exit(0)
    case ('4'): 
        # need to delete password then update file, by rewriting it
        k = input("Key of the designated password: ")
        if(k in listOfPasswords.keys()): 
            listOfPasswords.pop(k)
        else:
            print("this key doesn't exist")
            sys.exit(0)
        # before we change the file we need to clear it
        with open('passwords.txt', 'w') as file:
            pass
    
        # rewrite file
        for k in listOfPasswords.keys():  
            file = open("passwords.txt", "a")
            file.write(str(k) + ": " + str(listOfPasswords[k]) + "\n")
            file.close()
        sys.exit(0)
    case('5'): 
        try: 
            with open('passwords.txt', 'r') as file:
                for passwords in file: 
                    print(passwords)
                if (os.path.getsize('passwords.txt') == 0):
                    print("\nThere are no passwords saved\n")
                sys.exit(0)
        except FileNotFoundError: 
            print("No passwords have been saved\n") 
            sys.exit(0)
    case('6'):
        if (os.path.getsize('passwords.txt') == 0):
            print("\nThere are no passwords saved\n")
            sys.exit(0) 
        else: 
            key = input("Enter the key: ")
            if(listOfPasswords.get(key, -1) == -1):
                print("\nkey was not found in list\n")
                sys.exit(0)
            else: 
                print("\npassword: " + str(listOfPasswords[key]))
                print()
                sys.exit(0) 
    case('7'):
        pd = input("Enter the password: ")
        contains: bool 
        # check to see if the password is there before anything else 
        if(pd in listOfPasswords.values()): 
            for k in listOfPasswords.keys(): 
                if(listOfPasswords[k] == pd):
                    print('\nKey: ' + str(k) + '\n')
                    sys.exit(0) 
        else: 
            print("password was not found")
            sys.exit(0)
    case(default): 
        print("\nPlease enter 1, 2, or 3")
        sys.exit(0) 

# only reaches this point if a password was actually created
print("password successfully created\n" + str(key) + ": " + str(listOfPasswords[key]))

# opens a file to save the passwords into
file = open("passwords.txt", "a")
file.write(str(key) + ": " + str(listOfPasswords[key]) + '\n')
file.close()