# Hàm chuyển điểm số sang cách gọi trong tennis
def point_to_name(point):
    tennis_score = ["0", "15", "30", "40"]
    if point < 4:
        return tennis_score[point]
    return "Error"  # Chỉ để tránh lỗi nếu vượt quá

# Hàm kiểm tra xem có ai thắng chưa
def check_winner(a, b):
    if (a >= 4 or b >= 4) and abs(a - b) >= 2:
        return "A" if a > b else "B"
    return None

# Hàm hiển thị điểm hiện tại
def get_score(a, b):
    # Trường hợp Deuce
    if a >= 3 and b >= 3 and a == b:
        return "Deuce"
    # Trường hợp Advantage
    if a >= 4 and a == b + 1:
        return "Advantage A"
    if b >= 4 and b == a + 1:
        return "Advantage B"
    # Trường hợp bình thường
    return f"A: {point_to_name(a)} – B: {point_to_name(b)}"

# Chương trình chính mô phỏng nhập điểm
def play_game():
    a = b = 0
    while True:
        player = input("Nhập A hoặc B ghi điểm: ").strip().upper()
        if player == "A":
            a += 1
        elif player == "B":
            b += 1
        else:
            print("Chỉ nhập A hoặc B thôi nha.")
            continue

        winner = check_winner(a, b)
        if winner:
            print(f"Người chơi {winner} thắng game!")
            break
        else:
            print(get_score(a, b))


play_game()
