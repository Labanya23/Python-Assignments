import random

class GuessingGame:
    def __init__(self):
        pass

    def user_guesses_game(self):
        number = random.randint(1,100)
        attempts=0
        while True:
            try:
                guess = int(input("Guess num(1 t0 100):"))
                attempts +=1
                if guess<number:
                    print("Too low!")
                elif guess>number:
                    print('Too high!')
                else:
                    print(f"Correct! The number was{number}.You guessed correct {attempts}")
                    break
            except ValueError:
                print("plz enter a valid integer")
                    
    def computer_guesses(self):
        low,high = 1,100
        attempts= 0
        try:
            secret_num = int(input())
            if not 1 <= secret_num <=100:
                print("num 1 to 100")
                return 
        except ValueError:
            print("plz enter valid num")
            return 
        
        while low<=high:
            guess=(low+high)//2
            attempts +=1
            print(f"computer guesses:{guess}")
            if guess>secret_num:
                high=guess-1
            elif guess<secret_num:
                print("L")
                low = guess+1
            else:
                print(f"gess num{attempts}")
                break

    def start(self):
        while True:
            print("\nChoose an option:")
            print("1. your guess the num (computer selects)")
            print("2.Computer guesses num")
            print("3.exit")

            choice = input("enter ur choice")

            if choice == "1":
                self.user_guesses_game()

            elif choice =="2":
                self.computer_guesses()
            elif choice =="3":
                print("Goodluck!")
                break
            else:
                print("invalid choice")

if __name__ =="__main__":
   game= GuessingGame()
   game.start()
        
                



            
