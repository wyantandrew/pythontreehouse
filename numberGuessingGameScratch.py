

def func_start_game():
    print("Welcome to the Number Guessiing Game. \n")
    
    
def func_increase_list_count():
    list_count.append(input_guessed_num)


list_count = []    

import random

correct_num = random.randrange(51)
print(correct_num)
      
func_start_game()

try:
    input_guessed_num = int(input("Please guess a number 0-50: "))
    func_increase_list_count()
except ValueError:
    print("numbers only")    

while input_guessed_num != correct_num:
    try:
        if input_guessed_num < correct_num:
            print("It's higher\n")
            input_guessed_num = int(input("Please guess a number 0-50: "))
            func_increase_list_count()
        
        elif input_guessed_num > correct_num:
            print("It's lower.\n")
            input_guessed_num = int(input("Please guess a number 0-50: "))
            func_increase_list_count()
    except ValueError:
        print("Numbers only please.") 

            
print(f"Got it in {len(list_count)} attempts \nGreat job!\n")




  #insert count of attemnpts
  #call exception for invalid guesses