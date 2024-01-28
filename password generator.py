import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            print("Please enter a valid password length.")
        else:
            generated_password = generate_password(password_length)
            print("Generated Password:", generated_password)
    except ValueError:
        print("Please enter a valid number for password length.")

if _name_ == "_main_":
    main()