# Biến toàn cục lưu điểm của 2 người chơi
player_A_score = 0
player_B_score = 0

# Quy tắc điểm hiển thị (0, 15, 30, 40)
score_names = ["0", "15", "30", "40",None]


def reset_game():
    global player_A_score, player_B_score
    player_A_score = 0
    player_B_score = 0
    return "Start"


def get_display_score():
    #Trường hợp Deuce,Advantage,Win
    if player_A_score == 4 and player_A_score-player_B_score >=2 :
        return "Player 1 wins"
    elif player_B_score == 4 and player_B_score-player_A_score >=2:
        return "Player 2 wins"
    elif player_A_score >= 3 and player_B_score >= 3:
        if player_A_score == player_B_score:
            return "Deuce"
        elif player_A_score == player_B_score + 1:
            return "Advantage A"
        elif player_B_score == player_A_score + 1:
            return "Advantage B"
        elif player_A_score >= player_B_score + 2:
            return "Player 1 wins!"
        elif player_B_score >= player_A_score + 2:
            return "Player 2 wins!"
    #Trường hợp bình thường
    else:
        return f"{score_names[player_A_score]} - {score_names[player_B_score]}"

#cập nhật điểm
def update_score(player):
    global player_A_score, player_B_score
    if player == "A":
        player_A_score += 1
    elif player == "B":
        player_B_score += 1
    return (get_display_score())

