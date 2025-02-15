import string
import random

#v1


def generate(length, special, nums):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specialChars = string.punctuation

    characters = lowercase+uppercase
    if nums:
        characters += digits
    if specialChars:
        characters += specialChars

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter desired password length: "))
    useSpecialChars = input("Include special characters? (y/n): ").lower() == 'y'
    useNums = input("Include numbers? (y/n): ").lower() == 'y'
    
    password = generate(length, useSpecialChars, useNums)
    print(f"Generated password: {password}")
    input("Press ENTER to exit.")

get_user_input()
