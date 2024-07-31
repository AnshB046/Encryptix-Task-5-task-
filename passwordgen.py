import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue

            password = generate_password(length)
            print(f"Generated password: {password}")
            
            again = input("Do you want to generate another password? (yes/no): ").lower()
            if again != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
