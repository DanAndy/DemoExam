#импорт

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

from PyQt5.uic import loadUi

import sys

from PyQt5.QtGui import QPixmap, QIcon

#главный класс
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)


#запуск приложения

app = QApplication(sys.argv)

welcome = MainWindow() #обьект на основе нашего класса
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

#загружаем лого
logo = QIcon()
logo.addPixmap(QPixmap("logo.ong"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(logo)
widget.show()

#запуск
try:
    sys.exit(app.exec_())
except:
    print("except")


#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