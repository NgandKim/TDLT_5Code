import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodienbangdiemtennis import Ui_bangdiemtennis
from xuly import reset_game, get_display_score, check_winner, update_score



app = QApplication(sys.argv)
window = QWidget(windowTitle = 'Quy doi he')
form =Ui_bangdiemtennis()
form.setupUi(window)



window.show()
app.exec()