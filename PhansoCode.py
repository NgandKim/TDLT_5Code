import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from GdPhanso import Ui_MainWindow

class MainWindow():
    def __init__(self):
        self.main=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.main)
        self.nut()
    def show(self):
        self.main.show()
    def nut(self):
        self.ui.btn_cong.clicked.connect(self.tinh_cong)
        self.ui.btn_tru.clicked.connect(self.tinh_tru)
        self.ui.btn_nhan.clicked.connect(self.tinh_nhan)
        self.ui.btn_chia.clicked.connect(self.tinh_chia)
        self.ui.btn_tg.clicked.connect(self.tinh_toigian)
        self.ui.btn_nd.clicked.connect(self.tinh_nghichdao)

    def giatri(self):
        ts1 = int(self.ui.lne_ts1.text())
        ms1 = int(self.ui.lne_ms1.text())
        ts2 = int(self.ui.lne_ts2.text())
        ms2 = int(self.ui.lne_ms2.text())
        return ts1, ms1, ts2, ms2

    def tinh_toigian(self):
        ts1, ms1,_,_= self.giatri()
        kqua=uocchung(ts1,ms1)
        self.ui.lne_kqua.setText(kqua)

    def tinh_nghichdao(self):
        ts1, ms1,_,_= self.giatri()
        kqua=str(ms1)+'/'+str(ts1)
        self.ui.lne_kqua.setText(kqua)

    def tinh_cong(self):
        ts1, ms1, ts2, ms2 = self.giatri()
        kqua = cong(ts1, ms1, ts2, ms2)
        self.ui.lne_kqua.setText(kqua)

    def tinh_tru(self):
        ts1, ms1, ts2, ms2 = self.giatri()
        kqua = tru(ts1, ms1, ts2, ms2)
        self.ui.lne_kqua.setText(kqua)

    def tinh_nhan(self):
        ts1, ms1, ts2, ms2 = self.giatri()
        kqua = nhan(ts1, ms1, ts2, ms2)
        self.ui.lne_kqua.setText(kqua)

    def tinh_chia(self):
        ts1, ms1, ts2, ms2 = self.giatri()
        kqua = chia(ts1, ms1, ts2, ms2)
        self.ui.lne_kqua.setText(kqua)

def cong(ts1,ms1,ts2,ms2):
    ts=ts1*ms2 + ts2*ms1
    ms=ms1*ms2
    kqua=str(ts)+'/'+str(ms)
    return kqua

def tru(ts1,ms1,ts2,ms2):
    ts=ts1*ms2 - ts2*ms1
    ms=ms1*ms2
    kqua=str(ts)+'/'+str(ms)
    return kqua

def nhan(ts1,ms1,ts2,ms2):
    ts=ts1*ts2
    ms=ms1*ms2
    kqua=str(ts)+'/'+str(ms)
    return kqua

def chia(ts1,ms1,ts2,ms2):
    ts=ts1*ms2
    ms=ts2*ms1
    kqua=str(ts)+'/'+str(ms)
    return kqua

def uocchung(ts1, ms1):
    uoc = 1
    for i in range(1, min(ts1, ms1) + 1):
        if ts1 % i == 0 and ms1 % i == 0:
            uoc = i
    ts1=ts1//uoc
    ms1=ms1//uoc
    kqua=str(ts1)+'/'+str(ms1)
    return kqua

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    #ui = Ui_MainWindow()
    window.show()
    app.exec()



