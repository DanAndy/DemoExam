#импорт

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

from PyQt5.uic import loadUi

import sys

from PyQt5.QtGui import QPixmap, QIcon

import sqlite3




class Zakazchik(QMainWindow):
    def __init__(self):        
        super(Zakazchik, self).__init__()
        print("Проверка открытия страницы Zakazchik")

class Master(QMainWindow):
    def __init__(self):        
        super(Master, self).__init__()
        print("Проверка открытия страницы Master" )

class Authorization(QMainWindow):
    def __init__(self):        
        super(Authorization, self).__init__()
        print("Проверка открытия страницы Authorization" )
    def signupfunction(self):
        print("test")
        user = self.LoginField.text()
        password = self.PasswordField.text()
        print(user, password)

        # првоерка введения данных
        if len(user)==0 or len(password)==0:
            self.ErrorField.setText("Заполните все поля")
        else:
            self.ErrorField.setText("Все ок")

            #покдл к бд
            conn = sqlite3.connect('newbd')
            cur = conn.cursor()

            cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?);', [user, password]) 
            typeUser = cur.fetchone()
            print(typeUser[0])                      

            conn.commit()
            conn.close()

            if typeUser[0] == 4:
                self.stackedWidget.setCurrentWidget(self.Zakazchik)
                self.lybaya = Zakazchik()
            elif typeUser[0] == 2:
                self.stackedWidget.setCurrentWidget(self.Master)
                self.lybaya = Master()

    def MasterButfunction(self):
        print("test2")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

    def ZakazchikButfunction(self):
        print("test3")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

#главный класс
class MainWindow(QMainWindow):
    #проверка работы кнопки
    def signupfunction(self):
        print("test")
        user = self.LoginField.text()
        password = self.PasswordField.text()
        print(user, password)

        # првоерка введения данных
        if len(user)==0 or len(password)==0:
            self.ErrorField.setText("Заполните все поля")
        else:
            self.ErrorField.setText("Все ок")

            #покдл к бд
            conn = sqlite3.connect('newbd')
            cur = conn.cursor()

            cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?);', [user, password]) 
            typeUser = cur.fetchone()
            print(typeUser[0])                      

            conn.commit()
            conn.close()

            if typeUser[0] == 4:
                self.stackedWidget.setCurrentWidget(self.Zakazchik)
                self.lybaya = Zakazchik()
            elif typeUser[0] == 2:
                self.stackedWidget.setCurrentWidget(self.Master)
                self.lybaya = Master()

    def MasterButfunction(self):
        print("test2")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

    def ZakazchikButfunction(self):
        print("test3")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignButton.clicked.connect(self.signupfunction)
        self.MasterBut.clicked.connect(self.MasterButfunction)
        self.ZakazchikBut.clicked.connect(self.ZakazchikButfunction)








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