import random
import string
from ASCII import welcomeKPMG

def password_generator():
    print(welcomeKPMG)
    
    your_chosen_word = input("Enter a word to base your password on: ")
    
    while True:
        try:
            password_length = int(input("Enter the password length you need (12 or more characters): "))
            if password_length >= 12:
                break
            else:
                print("Password length should be 12 or more characters.")
        except ValueError:
            print("Please enter a valid number.")

    num_uppercase = int(input("Enter the number of uppercase letters you want in your password (4 or more, as KPMG suggests): "))
    
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_characters = input("Include special characters? (y/n): ").lower() == 'y'

    if not (include_lowercase or include_digits or include_special_characters):
        print("At least one character must be selected to create the password.")
        return
    
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    elif include_digits:
        characters += string.digits
    elif include_special_characters:
        characters += string.punctuation

    your_chosen_word = your_chosen_word.replace(" ", "").lower()
    max_available_characters = password_length - len(your_chosen_word) - num_uppercase
    additional_characters_needed = random.choices(characters, k=max_available_characters)
    

    additional_characters_needed = additional_characters_needed[:max(0, password_length - len(your_chosen_word) - num_uppercase)]
    
    uppercase_letters = random.sample(string.ascii_uppercase, num_uppercase)
    password_characters = list(your_chosen_word) + additional_characters_needed + uppercase_letters
    random.shuffle(password_characters)
    password = ''.join(password_characters)
    
    print("\nYour new KPMG password is:")
    print(password)

if __name__ == "__main__":
    password_generator()

