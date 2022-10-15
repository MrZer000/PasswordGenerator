import string , random , os
from colorama import Fore
"""
Date : 15/10/2022 
Time : 22:41 
By : Zero 
Description : This Is A Script For Creating A Passwords And Writing Them To A Specific File
 Called By PasswordList.txt

"""

LCaseAlphabet = string.ascii_lowercase
UCAlphabets = string.ascii_uppercase
Numbers = string.digits
Symbols = string.punctuation

def GeneratePassword(PasswordType : int , PasswordCount : int , PasswordLength : int):

    with open("PasswordList.txt",'a+') as PasswordFile :
        PasswordFile.truncate(0)
    Passwords = []
    if PasswordType <= 4 :
        if PasswordType == 1 :
            ChosenType = LCaseAlphabet
        if PasswordType == 2 :
            ChosenType = UCAlphabets
        if PasswordType == 3 :
            ChosenType = Numbers
        if PasswordType == 4 :
            ChosenType = Symbols
        for i in range(PasswordCount):
            Passwords.append( random.choice(ChosenType) )
        for item in range(len(Passwords)):
            for x in range(PasswordLength):
                Passwords[item] += random.choice(ChosenType) 
        PasswordFile = open("PasswordList.txt",'a')
        for password in Passwords :
            PasswordFile.write(password + "\n")
        print(Fore.GREEN , "Done , Check The Password List.txt File" , Fore.RESET)
    if PasswordType == 0 or PasswordType > 4 :
        print(Fore.RED , "Error" , Fore.RESET)

while True :
    print(Fore.YELLOW  , """
    Password Types :\n
    1 - For Lower Case Alphabets | 2 - For Upper Case Alphabets | 3 - For Digits | 4 - For Symbols
    """ , Fore.RESET )
    PasswordType = int(input("Choose Password Type : "))
    PasswordCount = int(input("How Many Password To Generate : "))
    PasswordLengeth = int(input("How Many Characters Should The Password Countain : "))
    GeneratePassword(PasswordType,PasswordCount,PasswordLengeth)
    break
