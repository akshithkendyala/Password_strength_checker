import re

def check_password_strength(password):
    strength = 0     #Calculates the strength of our password
    suggestions = [] #we will append suggestions to improve strength of password

    #We will consider length, alphabets, numbers, special characters for strength of our password

    #Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Make sure your password length is atleast 8 characters long.")

    
    #Check lowercase & uppercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Use both UPPER case & LOWER case letters.")

    #Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add atleast one number(0-9).")

    #Check for special characters
    if re.search(r"[!@#$%&*^?+-_=^]", password):
        strength += 1
    else:
        suggestions.append("Include atleast one special character(!, @, #, $, %, & etc...)")

    #Now after verifying password some sort of strength is calculated
    #Based on that strength let us assign some levels
    if strength >= 5:
        level = "Very Strong!"
    elif strength == 4:
        level = "Strong!"
    elif strength == 3:
        level = "Moderate!"
    else:
        level = "Weak!"

    return level, suggestions


#Main program
while True:
    password = input("\nEnter a password (or type 'exit' to quit): ").strip()

    if password.lower() == "exit":
        print("Bye, Stay Safe!")
        exit(0)
    
    level, suggestions = check_password_strength(password)

    #Output the strength/level of password & give some suggestions
    print(f"\nPassword strength: {level}")

    if suggestions: #if suggestions exist
        print("\n---Suggestions to make your password stronger & safer---")
        for i in suggestions:
            print(f"{i}")
