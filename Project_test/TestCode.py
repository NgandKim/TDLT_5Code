import sys
from PyQt6.QtWidgets import *
from giaodienbangdiemtennis import *  # file .ui chuyển sang .py bằng pyuic6

app = QApplication(sys.argv)
form = Ui_bangdiemtennis()
window = QMainWindow()
form.setupUi(window)

# --------------------------
# 🟢 Khởi tạo điểm ban đầu
# --------------------------
form.A = 0
form.B = 0
score_names = ["0", "15", "30", "40"]
form.kqua=''

# --------------------------
# 🟢 Liên kết nút
# --------------------------
def lienketnut():
    form.btn_p1.clicked.connect(cong_A)
    form.btn_p2.clicked.connect(cong_B)
    form.btn_reset.clicked.connect(reset_game)

# --------------------------
# 🟢 Các hàm xử lý
# --------------------------
def cong_A():
    update_score("A")

def cong_B():
    update_score("B")

def update_score(player):
    """Cập nhật điểm cho người chơi"""
    if player == "A":
        form.A += 1
    elif player == "B":
        form.B += 1

    A, B = form.A, form.B
    kqua = ""
    #Hiển thị LCD
    if A < 4:
        form.lcd_p1.display(score_names[A])
    else:
        form.lcd_p1.display("-")

    if B < 4:
        form.lcd_p2.display(score_names[B])
    else:
        form.lcd_p2.display("-")

    #Hiện tỉ số, kqua
    if A<3 and B<3:
        kqua = f"Tỉ số hiện tại: {score_names[A]} - {score_names[B]}"
    elif A==3 and B==3:
        kqua = "Deuce"
    elif A==3 or B==3:
        kqua = f"Tỉ số hiện tại: {score_names[A]} - {score_names[B]}"

    elif A>3 or B>3:
        if A == B + 1:
            kqua = "Advantage A"
        elif B == A + 1:
            kqua = "Advantage B"
        elif A >= B + 2:
            kqua = "Người chơi A thắng game!"
        elif B >= A + 2:
            kqua = "Người chơi B thắng game!"
        elif A - B == 2:
            kqua = "Người chơi 1 thắng game"
        elif B - A == 2:
            kqua = "Người chơi 2 thắng game"

        # Kiểm tra giai đoạn Deuce / Advantage / Winner

    # Cập nhật giao diện
    form.lne_kqua.setText(kqua)


def reset_game():
    """Đặt lại điểm game mới"""
    form.A = 0
    form.B = 0
    form.lcd_p1.display(0)
    form.lcd_p2.display(0)
    form.lne_kqua.setText("Bắt đầu game mới! Tỉ số: 0 - 0")

# --------------------------
# 🟢 Khởi động chương trình
# --------------------------
lienketnut()
window.show()
app.exec()
