

def func_start_game():
    print("Welcome to the Number Guessiing Game. \n")
    
    
def func_increase_list_count():
    list_count.append(input_guessed_num)


list_count = []    

import random

correct_num = random.randrange(51)
print(correct_num)
      
func_start_game()

while True:
    try:
        input_guessed_num = int(input("Please guess a number 0 - 50: "))
        if input_guessed_num > 50:
            print("Must guess 0 - 50\n")
            continue
        elif input_guessed_num < 0:
            print("Must guess 0 - 50\n")        
            continue
        if input_guessed_num < correct_num:
            print("It's higher.\n")
            func_increase_list_count()
            continue
        elif input_guessed_num > correct_num:
            print("It's lower.\n")
            func_increase_list_count()
            continue
        elif input_guessed_num == correct_num:
            break
    except ValueError:
        print("Numnbers only please.\n") 
        continue       

print(f"Got it in {len(list_count) + 1} attempts \nGreat job!\n")
input_play_again = input("Play again? Y/N: ")

while input_play_again.upper == "Y":
    try:
        input_guessed_num = int(input("Please guess a number 0 - 50: "))
        if input_guessed_num > 50:
            print("Must guess 0 - 50\n")
            continue
        elif input_guessed_num < 0:
            print("Must guess 0 - 50\n")        
            continue
        if input_guessed_num < correct_num:
            print("It's higher.\n")
            func_increase_list_count()
            continue
        elif input_guessed_num > correct_num:
            print("It's lower.\n")
            func_increase_list_count()
            continue
        elif input_guessed_num == correct_num:
            break
    except ValueError:
        print("Numnbers only please.\n") 
        continue       




  #insert count of attemnpts
  #call exception for invalid guesses