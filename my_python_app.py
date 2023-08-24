from ASCII import welcomeKPMG
import random
import string


def password_generator():
    print(welcomeKPMG)

    while True:
        try:
            password_length = int(input("Enter the password length you need (12 or more characters): "))
            if password_length >= 12:
                break
            else:
                print("Password length should be 12 or more characters.")
        except ValueError:
            print("Please enter a valid number.")
    

    num_uppercase = int(input("Enter the number of uppercase letters you want in your password (enter 4 or more thats what KPMG wants :) : "))
    

    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_characters = input("Include special characters? (y/n): ").lower() == 'y'
    
  
    if not (include_lowercase or include_digits or include_special_characters):
        print("At least one character must be selected to create the password.")
        
        return
    character_sets = ""
    if include_lowercase:
        character_sets += string.ascii_lowercase
    if include_digits:
        character_sets += string.digits
    if include_special_characters:
        character_sets += string.punctuation


    uppercase_letters = random.sample(string.ascii_uppercase, num_uppercase)
    password_characters = random.choices(character_sets, k=password_length - num_uppercase)
    password_characters.extend(uppercase_letters)
    random.shuffle(password_characters)
    password = ''.join(password_characters)
    
    print("\nYour new KPMG password is:")
    print(password)

if __name__ == "__main__":
    password_generator()

