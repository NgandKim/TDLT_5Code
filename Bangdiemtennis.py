import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodienbangdiemtennis import Ui_bangdiemtennis
from xuly import reset_game, get_display_score, check_winner, update_score, player_A_score

app = QApplication(sys.argv)
window = QWidget(windowTitle = 'Quy doi he')
form =Ui_bangdiemtennis()
form.setupUi(window)


INdiem1=["0","15","30","40"]
INdiem2=["0","15","30","40"]
def player_A():
    global player_A_score
    player_A_score+=1
    form.INdiem1.setText(INdiem1[(player_A_score)])

def reset():
    reset_game()
    form.linEketqua.setText(reset_game())

form.bt1.clicked.connect(player_A)
form.bt2.clicked.connect(player_A)
form.btreset.clicked.connect(reset)


window.show()
app.exec()