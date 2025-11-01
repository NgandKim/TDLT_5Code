import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodien import Ui_bangdiemtennis
import xuly

app = QApplication(sys.argv)
window = QWidget(windowTitle = 'Tennis')
form =Ui_bangdiemtennis()
form.setupUi(window)



def player_A():
    n=xuly.update_score("A")

    form.INdiem1.display(xuly.score_names[(xuly.player_A_score)])

def player_B():
    xuly.player_B_score+=1
    form.INdiem1_2.display(xuly.score_names[(xuly.player_B_score)])


def reset():
    xuly.reset_game()
    form.INdiem1.display(xuly.score_names[(xuly.player_B_score)])
    form.INdiem1_2.display(xuly.score_names[(xuly.player_B_score)])
    form.lneWord.setText(xuly.reset_game())

form.bt1.clicked.connect(player_A)
form.bt2.clicked.connect(player_B)
form.btreset.clicked.connect(reset)


window.show()
app.exec()