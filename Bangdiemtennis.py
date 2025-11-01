import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodienbangdiemtennis import Ui_bangdiemtennis
import xuly

app = QApplication(sys.argv)
window = QWidget(windowTitle = 'Quy doi he')
form =Ui_bangdiemtennis()
form.setupUi(window)



def player_A():
    xuly.player_A_score+=1
    form.INdiem1.setText(str(xuly.score_names[(xuly.player_A_score)]))

def player_B():
    xuly.player_B_score+=1
    form.INdiem1.setText(str(xuly.score_names[(xuly.player_B_score)]))


def reset():
    form.INdiem1.setText("0")
    form.INdiem1_2.setText("0")
    form.linEketqua.setText(xuly.reset_game())

form.bt1.clicked.connect(player_A)
form.bt2.clicked.connect(player_B)
form.btreset.clicked.connect(reset)


window.show()
app.exec()