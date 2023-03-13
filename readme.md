# ChessVision

## Description
This Python program analyzes a PGN file (containing one or more chess games) exported from chess.com and returns the openings ranked by the most played during the games in the PGN file. The program returns the number of times the opening was played and expresses the percentage of times it was played.

## Getting Started
To use this program, you will need to install Python 3 on your computer.

## Usage
1. Download your history of chess game in https://www.chess.com/games/archive/YOUR_PSEUDONYM
2. Clone this repository onto your local machine.
3. Open a terminal window and navigate to the project directory.
4. Run the following command :
```
python chess_vision.py
```

5. Enter the path of the .pgn file when prompted.
```
Enter the path of the .pgn export from chess.com (format : C:\directory\files.png): C:\directory\chesscom_games.pgn
```
Exemple of output : 
```
---------------------------
[White "Caro-Kann defense"] :  214 (22.96%)
[White "Caro-Kann"][Black "Advance, Short Variation "] :  60 (6.44%)
[White "Scotch"][Black "Lolli Variation "] :  50 (5.36%)
[White "Scotch"][Black "Ghulam Kassim Variation "] :  50 (5.36%)
[White "Scandinavian defense, Lasker Variation "] :  46 (4.94%)
[White "Blackmar-Diemer gambit"] :  44 (4.72%)
[White "Petrov"][Black "French attack"] :  33 (3.54%)
[White "King's pawn game"] :  27 (2.9%)
[White "French"][Black "Wing gambit"] :  23 (2.47%)
[White "QGD Slav defense, Alekhine Variation "] :  22 (2.36%)
[White "Pirc defense"] :  21 (2.25%) 
[White "Caro-Kann"][Black "Exchange, Rubinstein Variation "] :  21 (2.25%)
[White "Caro-Kann"][Black "GOldman (Spielmann) Variation "] :  19 (2.04%)
[White "Philidor"][Black "Philidor counter-gambit"] :  18 (1.93%)
[White "Guatemala defense"] :  16 (1.72%)
---------------------------
932 game have been analysed
---------------------------
```
