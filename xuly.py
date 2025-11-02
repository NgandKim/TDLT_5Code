# 0 điểm tương ứng với 0, 1 điểm tương ứng với 15, 2 điểm tương ứng với 30, 3 điểm tương ứng với 40
# Từ 3 điểm trở lên:
# Ai đạt >3 điểm và hơn đối thủ 2 điểm thì sẽ thắng
# Cả hai cùng bằng 3 thì gọi là Deuce, sau đó ai ăn thêm một điểm thì gọi là Advantage. Nếu gỡ hòa thì quay lại Deuce còn nếu ăn thêm 1 trái thì thắng game

# Danh sách điểm trong game Tennis
ds_diem= ["0", "15", "30", "40"]

#Hàm trả về 0 từ đầu khi reset
def reset_game():
    p1=0
    p2=0
    kqua="Start"
    return p1, p2, kqua # Trả về p1, p2 bằng 0 và thông báo start

#Hàm hiện tỉ số, kết quả game
def get_display_score(p1, p2):
    if p1 == 4 and p1 - p2 >= 2: #TH: P1 đạt 4 điểm trước và hơn P2 2 điểm thì thắng
        return "Player 1 wins"
    elif p2 == 4 and p2 - p1 >= 2: #TH: P2 đạt 4 điểm trước và hơn P1 2 điểm thì thắng
        return "Player 2 wins"
    elif p1 >= 3 and p2 >= 3: #Khi 2 player đạt mức điểm 3 trở lên
        if p1 == p2: # 2 người bằng điểm
            return "Deuce"
        elif p1 == p2 + 1: # P1 hơn P2 1 điểm
            return "Advantage A"
        elif p2 == p1 + 1: # P2 hơn P1 1 điểm
            return "Advantage B"
        elif p1 >= p2 + 2: # P1 hơn P2 2 điểm
            return "Player 1 wins!"
        elif p2 >= p1 + 2: # P2 hơn P1 2 điểm
            return "Player 2 wins!"
    # Trường hợp còn lại: cả 2 player đều dưới mức điểm 3
    else:
        return str(ds_diem[p1] + " - " + ds_diem[p2]) # Trả về tỉ số p1-p2

# Hàm cập nhật điểm (khi nhận tín hiệu click)
def update_score(p1, p2, player): # Đầu vào là điểm hiện tại p1, p2 và người thắng bóng
    if player == "P1": # Nếu người thắng bóng là P1
        p1 += 1
    else: # Người thắng bóng là P2
        p2 += 1
    kqua = get_display_score(p1, p2) # Sau khi cộng 1 điểm cho người thắng, đưa p1, p2 vào hàm get_display_score để xét trường hợp và hiện kết quả
    return p1, p2, kqua  # Trả về điểm số hiện tại, tỉ số/kết quả
