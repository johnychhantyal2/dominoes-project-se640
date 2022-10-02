# Import necessary libraries
import random
import time

# Define Classes
# CDominoes - contains the data structure with pieces
class CDominoes:
    def __init__(self):
        self.dominoes = [
            [0,0],
            [1,1], [1,0],
            [2,2], [2,1], [2,0],
            [3,3], [3,2], [3,1], [3,0],
            [4,4], [4,3], [4,2], [4,1], [4,0],
            [5,5], [5,4], [5,3], [5,2], [5,1], [5,0],
            [6,6], [6,5], [6,4], [6,3], [6,2], [6,1], [6,0]
        ]

# CRandom - as sorting approach for the sequence that the domino pieces will be shown/picked
class CRandom:
    def __init__(self, dominoes):
        self.picked = []
        count = 0
        while count < 10:
            choice = random.choice(dominoes)
            self.picked.append(choice)
            dominoes.remove(choice)
            count = count + 1

# CPlayer - to select a randomly picked and sequentially show the selected pieces
class CPlayer:
    def __init__(self, id, tiles):
        self.id = id
        self.tiles = tiles

# CTable - to show/display the sorted pieces
class CTable:
    def __init__(self, player, snake):
        count = 1
        print("Snake: ", snake, "\n")
        print("Player ", player.id, " Hand:")
        for tile in player.tiles:
            print(count, ": ", tile)
            count = count + 1

# Game Setup
# Selecting the tiles
tiles = CDominoes()

firstPick = CRandom(tiles.dominoes)
secondPick = CRandom(tiles.dominoes)

firstPlayer = CPlayer("1", firstPick.picked)
secondPlayer = CPlayer("2", secondPick.picked)

startingTile = random.choice(tiles.dominoes)
tiles.dominoes.remove(startingTile)
snake = [startingTile]
head = startingTile[0]
tail = startingTile[1]

# Selecting the player to play first
currentPlayer = random.choice([firstPlayer, secondPlayer])

print("\nWelcome to Dominoes!")
print("Let's play!\n")
print("Randomly selecting turn order...")
time.sleep(2)
print("Player ", currentPlayer.id, " will go first!")
print("\nRandomly picking Snake and Player Hands...\n")
time.sleep(2)

# Gameplay & Winning Conditions
isWinner = False
while not isWinner:
    playable = False
    nextPlayer = False
    
    while not playable:
        for tile in currentPlayer.tiles:
            if tile[0] == head or tile[0] == tail or tile[1] == head or tile[1] == tail:
                playable = True

        if not playable:
            if len(tiles.dominoes) == 0:
                CTable(currentPlayer, snake)
                print("Bummer! You cannot play a domino and there are no more domnimoes to draw.")
                nextPlayer = True
                playable = True

            else: 
                CTable(currentPlayer, snake)
                print("You cannot play a domino and need to draw. Select which domino to draw: \n")
                count = 1

                for tile in tiles.dominoes:
                    print(count, ": ???")
                    count = count + 1

                validPlay = False
                play = ''

                while not validPlay:
                    play = input("Which domino would you like to draw?\n")
                    if int(play) > 0 and int(play) < (len(tiles.dominoes) + 1):
                        validPlay = True
                    else:
                        print("Oofta, that was not a valid choice.")
                
                chosenTile = tiles.dominoes[int(play)-1]
                print("Chosen Domino: ", chosenTile)
                currentPlayer.tiles.append(chosenTile)
                tiles.dominoes.remove(chosenTile)

    if playable and not nextPlayer:
        validChoice = False

        while not validChoice:
            CTable(currentPlayer, snake)
            validPlay = False
            play = ""

            while not validPlay:
                play = input("Which domino would you like to play? (Select a number.)\n")
                if int(play) > 0 and int(play) < (len(currentPlayer.tiles) + 1):
                    validPlay = True
                else:
                    print("Please make a valid choice.")
            
            chosenTile = currentPlayer.tiles[int(play)-1]
            print("Chosen Domino: ", chosenTile)

            if (chosenTile[0] == tail and chosenTile[0] == head) or (chosenTile[1] == tail and chosenTile[1] == head) or (chosenTile[0] == head and chosenTile[1] == tail) or (chosenTile[1] == head and chosenTile[0] == tail):
                validEnd = False
                while not validEnd:
                    print("This domino can be played on either the head or the tail of the snake.")
                    print("1: Head")
                    print("2: Tail")
                    end = input("Where would you like to play this domino?\n")
                    if int(end) == 1 or int(end) == 2:
                        validEnd = True
                    else:
                        print("Please make a valid choice.")
                if int(end) == 1:
                    if chosenTile[0] == head:
                        snake.insert(0, [chosenTile[1], chosenTile[0]])
                        head = chosenTile[1]
                        validChoice = True
                        currentPlayer.tiles.remove(chosenTile)
                    else:
                        snake.insert(0, [chosenTile[0], chosenTile[1]])
                        head = chosenTile[0]
                        validChoice = True
                        currentPlayer.tiles.remove(chosenTile)
                else:
                    if chosenTile[0] == tail:
                        snake.append([chosenTile[0], chosenTile[1]])
                        tail = chosenTile[1]
                        validChoice = True
                        currentPlayer.tiles.remove(chosenTile)
                    else:
                        snake.append([chosenTile[1], chosenTile[0]])
                        tail = chosenTile[0]
                        validChoice = True
                        currentPlayer.tiles.remove(chosenTile)

            elif chosenTile[0] == head:
                snake.insert(0, [chosenTile[1], chosenTile[0]])
                head = chosenTile[1]
                validChoice = True
                currentPlayer.tiles.remove(chosenTile)

            elif chosenTile[1] == head:
                snake.insert(0, [chosenTile[0], chosenTile[1]])
                head = chosenTile[0]
                validChoice = True
                currentPlayer.tiles.remove(chosenTile)

            elif chosenTile[0] == tail:
                snake.append([chosenTile[0], chosenTile[1]])
                tail = chosenTile[1]
                validChoice = True
                currentPlayer.tiles.remove(chosenTile)

            elif chosenTile[1] == tail:
                snake.append([chosenTile[1], chosenTile[0]])
                tail = chosenTile[0]
                validChoice = True
                currentPlayer.tiles.remove(chosenTile)

            else:
                print("Invalid domino. Please make another choice.")

    # Diplay winner and the final snake            
    if len(currentPlayer.tiles) == 0:
        print("Congratulations Player ", currentPlayer.id, ". You've won!")
        if currentPlayer.id == '1':
            print("Player 2 has the following remaining dominoes: ")
            count = 1
            for tile in secondPlayer.tiles:
                print(count, ': ', tile)
                count = count + 1
        else:
            print("Player 1 has the following remaining dominoes: ")
            count = 1
            for tile in firstPlayer.tiles:
                print(count, ': ', tile)
                count = count + 1
        print("Final Snake: ", snake)
        isWinner = True
    else:
        if int(currentPlayer.id) == 1:
            currentPlayer = secondPlayer
        else:
            currentPlayer = firstPlayer

print('\n*************************************************\n')
