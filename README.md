# LUDO
**Ludo** is strategy board game, which can be played by 2 to 4 players with each player having a set of 4 pieces (usually identified by color) placed in the starting zone, which is at the left corner for each player. By rolling the dice, players race their four pieces on the board from start to finish, while trying to avoid being killed or captured by their opponents.

The main objective for each player is to move all his/her tokens or pieces to the finish before his/her opponents. Of course, en-route there are some more obstacles that the player has to overcome. Go through these step-by-step instructions to get a better perspective on how to master this easy game.

## How to Run
```bash
git clone https://gitlab.com/mansiag/Ludo
cd Ludo
pip3 install -r requirement.txt
python3 main.py
```

## Instruction

- Each player gets a chance to roll the die. Game starts with one who has Green Coin. The other players start rolling the die in an **anticlockwise** direction.
- To enter a token/piece into play,or from its staging area to its starting square, a player must roll a 6. If the player does not roll a 6, the turn passes to the next player. Once a player has one or more tokens in play, he can choose any one of the tokens in play and move them forward. The number on the rolled die will determine the number of squares the chosen piece moves forward.
- If a player lands on a square he/she already occupies, the pair of tokens form a block. Opponents can pass or land on the block but would not able to kill. If the advance of a token ends on a square occupied by an opponent's token, the opponent's token is returned to its owner's starting position. The returned token may only be reentered into play when the owner again rolls a 6.
- When the player rolls a six, he/she can get a single pawn out off a pocket. Then you roll again and move that pawn the number of spaces corresponding to the second roll.
    -   If the player rolls a six on the second roll, then the player can choose to place another pawn out of a pocket or move the first pawn. If you moved a second pawn out of your pocket, roll a third time and proceed to move a pawn.
    -   If a player rolls a six on their third roll, they cannot place any pawns out of their pocket. The third six ends a player’s turn
- ***If there is two or more than two coins on a single block of path then player has to click on the visible part of that coin for moving the coin.***
- Now, once a token travels around the entire board and reaches his home stretch or home column, it has to be moved towards the home. For this, a player has to roll the exact number the token has to move in order to reach home. For example, if you roll a four, and your token requires to move only three squares, you have to move another token or pass. The first player to move all his tokens to the finishing square wins the game.

### Screenshots

![alt text](./assets/main.png?raw=true)

![alt text](./assets/name.png?raw=true)

![alt text](./assets/midphase.png?raw=true)

![alt text](./assets/kill.png?raw=true)

## Contributors

- [Mansi Agrawal (@mansiag)](https://github.com/mansiag)
- [Shivam Gupta (@shivg7706)](https://github.com/shivg7706)
