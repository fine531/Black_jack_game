import os
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# Function to clear the console
def clear():
    # Clear command for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Clear command for Mac and Linux
    else:
        _ = os.system('clear')

# Function to deal cards to the player
def deal_cards(cards, n):
    return random.choices(cards, k=n)

# Function to display user's cards and current score
def show_user_cards(user):
    print(f"Your cards: {user}, current score: {sum(user)}")

# Function to display the computer's first card
def show_computer_card(computer):
    print(f"Computer's first card: {computer[0]}")

# Initialize game
continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if continue_game == 'y':
    clear()
    continue_game = True
else:
    continue_game = False

while continue_game:
    print(logo) 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = deal_cards(cards, 2)
    computer = deal_cards(cards, 2)
    show_user_cards(user)
    show_computer_card(computer)

    # Game logic
    game_in_progress = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while game_in_progress == 'y':
        user.append(random.choice(cards))
        show_user_cards(user)
        game_in_progress = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    print("You chose to stand.")
    while sum(computer) < 17:
        computer.append(random.choice(cards))
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")

    # Calculate scores
    if sum(user) > 21:
        print("You went over. You lose 😭")
    elif sum(computer) > 21:
        print("Opponent went over. You win 😁")
    elif sum(user) == 21: 
        print("Win with a Blackjack 😎")
    elif sum(computer) == 21:
        print("Lose, opponent has Blackjack 😱")
    elif sum(computer) < sum(user):
        print("You win! 😃")
    else:
        print("It's a draw!")

    # Continue game or not
    continue_game = input("Do you want to play another round of Blackjack? Type 'y' or 'n': ").lower() 
    if continue_game != 'y':
        continue_game = False
    else:
        clear()

print("Thanks for playing!")
