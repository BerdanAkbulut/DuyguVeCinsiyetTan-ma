# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from secondwindow import SecondWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainwindow()

    def mainwindow(self):
        # Anasayfa yapısı
        self.second_window = QtWidgets.QStackedWidget()
        self.setStyleSheet("background: cyan;")
        self.setWindowTitle("Trakya Üniversitesi Bitirme Projesi")
        self.setWindowIcon(QtGui.QIcon('iimages/kapak.jpg'))
        self.setMinimumSize(1200, 900)
        self.setMaximumSize(1200, 900)

        # logo
        self.logo = QtWidgets.QLabel(self)
        self.logo.setPixmap(QtGui.QPixmap("iimages/kapak.jpg"))
        self.logo.setScaledContents(True)
        self.logo.resize(1000, 600)
        self.logo.move(100, 0)

        # tez konusu
        self.tez_konusu = QtWidgets.QLabel(self)
        self.tez_konusu.setText("PROJE KONUSU: \nDERİN ÖĞRENME \nİLE\nYÜZ VE MİMİK TANIMA")
        self.tez_konusu.setFont(QtGui.QFont("MS Shell Dlg 2", 25))
        self.tez_konusu.setAlignment(QtCore.Qt.AlignCenter)
        self.tez_konusu.resize(750, 191)
        self.tez_konusu.move(230, 600)

        # Programa geçiş butonu
        self.prog_gecis_buton = QtWidgets.QPushButton(self)
        self.prog_gecis_buton.setText("MİMİK TANIMLAMAYA\nBAŞLA")
        self.prog_gecis_buton.setStyleSheet(
            "background-color:#c39435;color:#ffffff;border-radius:20px;border-style: solid;")
        self.prog_gecis_buton.setFont(QtGui.QFont("MS Shell Dlg 2", 12, QtGui.QFont.Bold))
        self.prog_gecis_buton.resize(191, 51)
        self.prog_gecis_buton.move(510, 800)

        self.prog_gecis_buton.clicked.connect(self.openWindow)

    def openWindow(self):
        self.hide()
        self.second = SecondWindow()
        self.second.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
