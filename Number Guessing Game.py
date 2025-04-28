import random #module to generate random numbers.The module is built into python, so no need to install it.

top_of_range=input("Type a number: ") #prompts the user to enter a number.

if top_of_range.isdigit(): #checks if the input is a digit.
    top_of_range=int(top_of_range) #converts the input to an integer.
    if top_of_range <= 0: #checks if the input is less than or equal to 0.
        print("Please enter a number greater than 0.") #prompts the user to enter a number greater than 0.
        quit() #exits the program.
else:   #if the input is not a digit.
    print("Please enter a number next time.") #prompts the user to enter a number next time.
    quit() #exits the program.
# The input is a digit and greater than 0.

random_number=random.randint(0,top_of_range) #generates a random number between 0 and the input number.

guesses=0 #initializes the number of guesses to 0.


while True: #infinite loop.
    guesses += 1 #increments the number of guesses by 1.
    # The user has to guess the number.
    user_guess = input("Make a guess (or type 'I give up' to quit): ").strip()#prompts the user to enter a guess. The strip() method removes any leading or trailing whitespace from the input.
    # The user can also type 'I give up' to quit the game.

    if user_guess.lower() in ["i give up", "ok i give up", "give up"]:#
        print(f"You gave up! The number was {random_number}.")
        break# #exits the loop and prevents the program from running again.
   
    if user_guess.isdigit(): #checks if the input is a digit.
        user_guess=int(user_guess) #converts the input to an integer.
    else: #if the input is not a digit.
        print("Please enter a number next time.") #prompts the user to enter a number next time.
        continue #continues to the next iteration of the loop.

    if user_guess == random_number: #checks if the guess is equal to the random number.
        print("You got it!") #prints that the user got it right.
        break #exits the loop and prevents the program from running again.
    #if the guess is not equal to the random number
    elif user_guess > random_number: #if the guess is greater than the random number.
        print("You are above the number!")#prints that the guess is above the random number.
    elif user_guess < random_number: #if the guess is less than the random number.
        print("You are below the number") #prints that the guess is too low.
  
print(f"You got it in {guesses} guesses!" if user_guess == random_number else f"Game over after {guesses} guesses.")
#prints the number of guesses it took to get the correct answer.
# The f-string is used to format the string and insert the value of the variable guesses into the string.



