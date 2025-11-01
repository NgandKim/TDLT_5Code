import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodien import Ui_bangdiemtennis
import xuly

app = QApplication(sys.argv)
window = QWidget(windowTitle = 'Tennis')
form =Ui_bangdiemtennis()
form.setupUi(window)



#Quy tắc hiện điểm
def more():
    if xuly.player_A_score<4 and xuly.player_B_score<4:
        form.INdiem1.display(xuly.score_names[(xuly.player_A_score)])
        form.INdiem1_2.display(xuly.score_names[(xuly.player_B_score)])
    else:
        form.INdiem1.display(" ")
        form.INdiem1_2.display(" ")


def player_A():
    n=xuly.update_score("A") #cập nhật điểm
    more()
    form.lneWord.setText(n)

def player_B():
    n=xuly.update_score("B")
    more()
    form.lneWord.setText(n)

#Chơi ván mới
def reset():
    xuly.reset_game()
    #Hiện 0-0
    form.INdiem1.display(xuly.score_names[0])
    form.INdiem1_2.display(xuly.score_names[0])
    form.lneWord.setText(xuly.reset_game())

form.bt1.clicked.connect(player_A)
form.bt2.clicked.connect(player_B)
form.btreset.clicked.connect(reset)


window.show()
app.exec()