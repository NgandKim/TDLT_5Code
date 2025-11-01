import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodien import Ui_bangdiemtennis
import xuli

app = QApplication(sys.argv)
window = QWidget(windowTitle = 'Tennis')
form =Ui_bangdiemtennis()
form.setupUi(window)



def player_A():
    n=xuli.update_score("A")
    form.INdiem1.display(xuli.score_names[(xuli.player_A_score)])

def player_B():
    n=xuli.update_score("B")
    form.INdiem1_2.display(xuli.score_names[(xuli.player_B_score)])

def rule():
    form.lneWord.setText(xuli.get_display_score)

def reset():
    xuli.reset_game()
    form.INdiem1.display(xuli.score_names[(xuli.player_B_score)])
    form.INdiem1_2.display(xuli.score_names[(xuli.player_B_score)])
    form.lneWord.setText(xuli.reset_game())

form.bt1.clicked.connect(player_A)
form.bt2.clicked.connect(player_B)
form.btreset.clicked.connect(reset)


window.show()
app.exec()