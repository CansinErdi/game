from game_utils import solve_riddle, end_game

def greeting():
    print("Welcome to the Treasure Hunt")
    print("You can navigate through room by giving the commands 'north', 'south', 'west and 'south'")
    print("In every room you find a clue. Solve the clue to continue with the hunt")
    print("The objective of the game is find the treasure. Good Luck!")

    def enter_room(room):
        if room == "Room 1":
            print("You enter room 1. Its dark and moist")
            print("A mysterious riddle reveals on the wall")

        elif room == "Room 2":
            print("You enter room 2. It smells like old books in here")
            print("you find another riddle on the desk")
        
        elif room == "Room 3":
            print("Room 3 is brightly lit, and you see a treasure chest in the corner")
            print("But first, you must solve one last riddle to open the chest.")
            


def main():
    greeting()

    current_room = "Room 1"
    while True:
        
        

        if current_room == "Room 1":
            solve_riddle("i am not alive, but i can grow. What am i?")
            current_room = "Room 2"
        elif current_room == "Room 2":
            solve_riddle("I have hands, but i can't clap. What am i?")
            current_room = "Room 3"
        elif current_room == "Room 3":
            solve_riddle("I have cities, but no houses. I have mountains, but no Land. What am i?")
            print("Congratulations! You have found the treasure")
            end_game()
            break

if __name__ == "__main__":
    main()



