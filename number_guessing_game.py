import random #Import the randint module
def number_guessing_game():
    print("Welcome to Margaret's Number Guessing Game!")
    print("Choose your difficulty level: ")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard(1-100)")

    #--Good Practice: Perform Code Refactoring to know what the numbers represent (Avoid Magic Numbers)---#
    easy = "1"
    medium = "2"
    hard = "3"
    #---Let users choose the difficulty of the game---#
    choice = input("Choose your level of difficulty(1-3): ")

    #maximum : The maximum number that the user can guess---#
    #---Set the maximum number a user can guess---#
    if choice == easy:
        maximum = 10 
    elif choice == medium:
        maximum = 50 
    else:
        maximum = 100

    #----Generate the random number---#
    number = random.randint(1,maximum)
    #Initialise the attempts#
    attempts = 0

    while True: #This is an infinite loop, which breaks when user guesses correctly#
        #Code to handle errors#
        try: #try block - Contains code that may cause errors
            guess = int(input(f"Guess a number between 1 and {maximum}: ")) #The int(input()) line should be within the try block, so if user enters anything invalid, program won't crash---#
            attempts += 1
            if guess > number:
                print("Too high! Try again")
            elif guess < number:
                print("Too low! Try again")
            else: #When the user finally guesses right, the loop ends naturally
                print(f"Correct!, You got it in {attempts} attempts.")
                break #Used to break the while loop when user guesses correctly--#
        except ValueError: #ValueError - When you convert something that's not a number to a number using int()
            #except block - Contains code that can handle those errors
            print("Please enter a valid number!")
            continue #Skip the rest of the code, and go back to the start of the loop#


#---Play Again Option : Put It Outside The Main Loop As It is Cleaner---#
while True:
    number_guessing_game() #Call the function to run the entire game once - You need to play the game before asking user to replay#
    play_again = input("Do you want to play again? (Y/N): ").upper() #Ask whether user wants to replay, after playing, make sure that users only enter capital letters
    if play_again != "Y":
        print("Thanks for playing! Hope you enjoyed!")
        break #Exits the loop if user does not want to play---#





        
