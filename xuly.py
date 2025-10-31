# Biến toàn cục lưu điểm của 2 người chơi
player_A_score = 0
player_B_score = 0

# Quy tắc điểm hiển thị (0, 15, 30, 40)
score_names = ["0", "15", "30", "40"]


def reset_game():
    global player_A_score, player_B_score
    player_A_score = 0
    player_B_score = 0
    return "Bắt đầu game mới! Tỉ số: 0 - 0"


def get_display_score():
    if player_A_score >= 3 and player_B_score >= 3:
        if player_A_score == player_B_score:
            return "Deuce"
        elif player_A_score == player_B_score + 1:
            return "Advantage A"
        elif player_B_score == player_A_score + 1:
            return "Advantage B"

    # Nếu chưa tới giai đoạn Deuce
    score_A_display = score_names[player_A_score] if player_A_score < 4 else "40"
    score_B_display = score_names[player_B_score] if player_B_score < 4 else "40"
    return f"A: {score_A_display} - B: {score_B_display}"


def check_winner():
    if player_A_score >= 4 and player_A_score >= player_B_score + 2:
        return "Người chơi A thắng game!"
    elif player_B_score >= 4 and player_B_score >= player_A_score + 2:
        return "Người chơi B thắng game!"
    return None


def update_score(player):
    global player_A_score, player_B_score
    if player == "A":
        player_A_score += 1
    elif player == "B":
        player_B_score += 1

    # Kiểm tra có ai thắng chưa
    winner = check_winner()
    if winner:
        result = winner
        # Sau khi có người thắng, tự động reset để chơi ván mới
        reset_game()
        return result

    # Nếu chưa ai thắng, trả về điểm hiển thị
    return get_display_score()
