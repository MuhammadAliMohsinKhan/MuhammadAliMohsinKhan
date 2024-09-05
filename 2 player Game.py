#Try to make for 2 players

Player1 = input("Enter Player 1 input: ")
Player2 = input("Enter Player 2 input: ")

GameFeature = {
    "r":1,
    "p":-1,
    "s":0
}
GameDict = {
    1: "rock",
    -1: "paper",
    0: "scissor"
}

you = GameFeature[Player1]
otherplayer = GameFeature[Player2]
print(f"Player1 choose {GameDict[you]}\nPlayer2 choose {GameDict[otherplayer]}")


if(otherplayer == you):
    print("Its a draw!")  
elif(otherplayer == 1 and you == 0):
        print("Player1 lose!")

elif(otherplayer == 1 and you == -1):
        print("Player1 Win!")

elif(otherplayer == -1 and you == 0):
        print("Player1 Win!")

elif(otherplayer == -1 and you == 1):
        print("Player1 lose!")

elif(otherplayer == 0 and you == 1):
        print("Player1 Win!")

elif(otherplayer == 0 and you == -1):
        print("Player1 lose!")

else:
        print("Something went wrong")