import random

num_to_guess = random.randint(1, 100)
num_of_attempts = 0

print("WELCOME TO NUMBER GUESSONG GAME!\n I'm Thinking of a number between 1 to 100")
Choice = (input("CHOOSE THE LEVEL OF DIFICULTY .Type 'EASY' or 'HARD' : ")).upper()

# Now giving no of attempts based on the difficulty

if Choice == 'HARD':
    num_of_attempts = 5

elif Choice == 'EASY':
    num_of_attempts = 10

else:
    print("Invalid Choice !!")
    exit(0)

# Now time for guessing
while num_of_attempts > 0:
    print(f"You have {num_of_attempts} to guess ")
    user_Choice = int(input("Enter your guess:"))
    num_of_attempts = num_of_attempts - 1

    if user_Choice == num_to_guess:
        print(" Your Guess is correct ")
        exit(0)

    elif user_Choice > num_to_guess:
        print("Too High , Guess Lower!")

    elif user_Choice < num_to_guess:
        print("Too Low , Guess Higher!")

    print('\n')

print("You Failed ,Try again")