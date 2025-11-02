import sys
from PyQt6.QtWidgets import QApplication, QWidget
from giaodien import *
from xuly import *

app = QApplication(sys.argv)
window = QWidget()
form = Ui_bangdiemtennis()
form.setupUi(window)

# Tạo p1, p2 như thuộc tính của form vì thế có thể gọi ra và cập nhật
form.p1 = 0
form.p2 = 0

def lienketnut():
    form.btn_p1.clicked.connect(player_1) # Gọi hàm player_1 khi bấm nút Player 1
    form.btn_p2.clicked.connect(player_2) # Gọi hàm player_2 khi bấm nút Player 2
    form.btn_reset.clicked.connect(reset) # Gọi hàm reset trả lại từ đầu khi bấm Reset

 # Hàm cập nhật điểm khi người ghi điểm là P1
def player_1():
    form.p1, form.p2, kqua = update_score(form.p1, form.p2, "P1") # Đưa điểm hiện tại và người ghi bóng P1 vào update_score, sau đó gán lại kết quả
    hiendiem(form.p1, form.p2) # Đưa dữ liệu điểm sau update_score để hiện lên LCDnumber
    form.lne_kqua.setText(kqua) # Trả tỉ số/kết quả ra lineEdit

# Hàm cập nhật điểm khi người ghi bóng là P2
def player_2():
    form.p1, form.p2, kqua = update_score(form.p1, form.p2, "P2") # Đưa điểm hiện tại và người ghi bóng P2 vào update_score, sau đó gán lại kết quả
    hiendiem(form.p1, form.p2) # Đưa dữ liệu điểm sau update_score để hiện lên LCDnumber
    form.lne_kqua.setText(kqua) # Trả tỉ số/kết quả ra lineEdit

# Hàm hiển thị điểm 2 player ra LCDNumber
def hiendiem(p1, p2):
    if p1 <= 3 and p2 <= 3: # Khi điểm của cả hai dưới mức 4
        form.lcd_p1.display(ds_diem[p1])
        form.lcd_p2.display(ds_diem[p2])
    else: # Khi điểm của 1 trong 2 hoặc cả hai trên mức 4
        form.lcd_p1.display("-")
        form.lcd_p2.display("-")

# Hàm reset game
def reset():
    form.p1, form.p2, kqua = reset_game() # Gán kết quả của reset_game p1,p2=0 vào điểm hiện tại và hiển thị Start
    form.lcd_p1.display(form.p1) # Điểm P1=0 trên LCDnumber
    form.lcd_p2.display(form.p2) # Điểm P2=0 trên LCDnumber
    form.lne_kqua.setText(kqua) # Hiển thị thông báo Start


lienketnut() #Gọi hàm lienketnut chạy
window.show()
app.exec()
