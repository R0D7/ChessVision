import re
from opening_database import opening_data

path_pgn = input(r"Enter the path of the .pgn export from chess.com (format : C:\directory\files.png): ")

with open(path_pgn,"r") as f:
    data_analyzed = f.read().strip()

database_clean = re.sub(r'\[(.*?)\]', '', data_analyzed)
database_clean = database_clean.replace("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "/--/")
database_clean = database_clean.replace("\n", "")
list_of_game = database_clean.split("/--/")

opening_score_final = {}
opening_score_temp = {}
for opening_name in opening_data:
    opening_score_final[opening_name] = 0
    opening_score_temp[opening_name] = 0

print("---------------------------")
nb_game = 0  
for game in list_of_game:
    nb_game += 1
    game_compress = game.split()
    temp_score = {}
    for name, opening_moves in opening_data.items():
        opening_moves = opening_moves.split()
        matching_moves = 0
        for i in range(min(len(opening_moves), len(game_compress))):
            if opening_moves[i] == game_compress[i]:
                matching_moves += 1
            else : 
                temp_score[name] = matching_moves
                break
    game_opening = max(temp_score, key=lambda k: temp_score[k])
    print(f'{game_compress}: {game_opening} with {temp_score[game_opening]}')
    print("")
    opening_score_final[game_opening] += 1

opening_score_final = sorted(opening_score_final.items(), key=lambda x: x[1], reverse=True)
print("---------------------------")
for i in range(15):
    if i < len(opening_score_final):
        key, value = opening_score_final[i]
        if value != 0:
            print(f"{key} :  {value} ({round(value/nb_game*100, 2)}%) ")

print("---------------------------")
print(f"{nb_game} game have been analysed")
print("---------------------------")