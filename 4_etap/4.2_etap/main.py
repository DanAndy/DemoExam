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
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem  # для работы с таблицами
)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidget, QLineEdit
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QPushButton


class Operator(QMainWindow):
    
    def __init__(self, table_widget):        
        super(Operator, self).__init__()
        print("Проверка открытия страницы Operator")
        self.tableVseZayavki = table_widget
        print(self.tableVseZayavki)
        print(table_widget)
        self.showdata()
        # self.BackButtonReq.clicked.connect(self.BackOperatorButfunction)
        # self.SaveButton.clicked.connect(self.SaveFunction)

    def showdata(self):
        conn1 = sqlite3.connect("newbd")
        cur1 = conn1.cursor()
        data = cur1.execute(f"""SELECT
                                r.IDrequest AS "Идентификатор заявки",
                                r.startDate AS "Дата начала заявки",
                                ot.orgTechType AS "ID типа техники",
                                r.orgTechModel AS "Модель техники",
                                r.problemDescryption AS "Описание проблемы",
                                rs.requestStatus AS "ID статуса заявки",
                                r.completionDate AS "Дата завершения",
                                r.repairParts AS "Замененные запчасти",
                                m.fio AS "ID мастера",
                                c.fio AS "ID клиента"
                                FROM 
                                    requests r
                                LEFT JOIN 
                                    orgTechTypes ot ON r.orgTechTypeID = ot.IDorgTechType
                                LEFT JOIN 
                                    requestStatuses rs ON r.requestStatusID = rs.IDrequestStatus
                                LEFT JOIN 
                                    users m ON r.masterID = m.IDuser
                                LEFT JOIN 
                                    users c ON r.clientID = c.IDuser;""")
            
        col_name = [i[0] for i in data.description]
        print(col_name)
        data_rows = data.fetchall()
        self.tableVseZayavki.setHorizontalHeaderLabels(col_name)
        self.tableVseZayavki.setRowCount(0)       
        for i, row in enumerate(data_rows):
            self.tableVseZayavki.setRowCount(self.tableVseZayavki.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableVseZayavki.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableVseZayavki.resizeColumnsToContents()
        
        self.tableVseZayavki.setColumnCount(len(col_name))
        print(len(col_name))
                
        self.tableVseZayavki.setHorizontalHeaderLabels(col_name)
        self.tableVseZayavki.setRowCount(0) 
        for i, row in enumerate(data_rows):
            self.tableVseZayavki.setRowCount(self.tableVseZayavki.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableVseZayavki.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableVseZayavki.resizeColumnsToContents()
        conn1.commit()
        conn1.close()

        self.vivod()
        
    def vivod(self):
        conn = sqlite3.connect("newbd")
        cur = conn.cursor()
        zayavki=cur.execute('SELECT * FROM requests') 
        name_stolba = [xz[0] for xz in zayavki.description] 
        print(name_stolba)
        conn.commit() 
        conn.close() 

class Zakazchik(QMainWindow):
    def __init__(self):        
        super(Zakazchik, self).__init__()
        print("Проверка открытия страницы Zakazchik")

class Master(QMainWindow):
    def __init__(self):        
        super(Master, self).__init__()
        print("Проверка открытия страницы Master" )

class AddRequest(QMainWindow):
    def __init__(self, BButton, Sbutton, lineIDrequest,
                 linestartDate,
                 lineorgTechTypeID,
                 lineorgTechModel,
                 lineproblemDescryption,
                 linerequestStatusID,
                 linecompletionDate,
                 linerepairParts,
                 linemasterID,
                 lineclientID):        
        super(AddRequest, self).__init__()

        print("Проверка открытия страницы AddRequest" )

        """
        Это конструктор класса
        """
        
        self.BackButtonReq = BButton
        print(self.BackButtonReq) 

        self.SaveButton = Sbutton
        print(self.SaveButton)

        self.IDrequestLine = lineIDrequest
        print(self.IDrequestLine)   
        
        self.startDateLine = linestartDate
        print(self.startDateLine)
        
        self.orgTechTypeIDLine = lineorgTechTypeID
        print(self.orgTechTypeIDLine)
        
        self.orgTechModelLine = lineorgTechModel
        print(self.orgTechModelLine)
        
        self.problemDescryptionLine = lineproblemDescryption
        print(self.problemDescryptionLine)
        
        self.requestStatusIDLine = linerequestStatusID
        print(self.requestStatusIDLine)
        
        self.completionDateLine = linecompletionDate
        print(self.completionDateLine)
        
        self.repairPartsLine = linerepairParts
        print(self.repairPartsLine)
        
        self.masterIDLine = linemasterID
        print(self.masterIDLine)
        
        self.clientIDLine = lineclientID
        print(self.clientIDLine)

        self.SaveButton.clicked.connect(self.SaveFunction)        

    def SaveFunction(self):        
        IDrequest = self.IDrequestLine.text() 
        print(IDrequest) 

        startDate = self.startDateLine.text() 
        print(startDate)

        orgTechTypeID = self.orgTechTypeIDLine.text() 
        print(orgTechTypeID)

        orgTechModel = self.orgTechModelLine.text() 
        print(orgTechModel)

        problemDescryption = self.problemDescryptionLine.text() 
        print(problemDescryption)

        requestStatusID = self.requestStatusIDLine.text() 
        print(requestStatusID)

        completionDate = self.completionDateLine.text() 
        print(completionDate)

        repairParts = self.repairPartsLine.text() 
        print(repairParts)

        masterID = self.masterIDLine.text() 
        print(masterID)

        clientID = self.clientIDLine.text() 
        print(clientID)

        conn1 = sqlite3.connect("newbd")
        cur1 = conn1.cursor()
               
        cur1.execute(f"""INSERT INTO requests (
                        IDrequest, 
                        startDate, 
                        orgTechTypeID, 
                        orgTechModel, 
                        problemDescryption, 
                        requestStatusID, 
                        completionDate, 
                        repairParts, 
                        masterID, 
                        clientID
                    ) VALUES (
                        {IDrequest},        -- IDrequest (INTEGER)
                        "{startDate}",        -- startDate (TEXT)
                        {orgTechTypeID},        -- orgTechTypeID (INTEGER)
                        "{orgTechModel}",        -- orgTechModel (TEXT)
                        "{problemDescryption}",        -- problemDescryption (TEXT)
                        {requestStatusID},        -- requestStatusID (INTEGER)
                        "{completionDate}",        -- completionDate (TEXT)
                        "{repairParts}",        -- repairParts (TEXT)
                        {masterID},        -- masterID (INTEGER)
                        {clientID}         -- clientID (INTEGER)
                    );
                    """)
        print("test")
        conn1.commit()
        conn1.close()
               

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
            elif typeUser[0] == 3:
                self.tableVseZayavki = self.findChild(QTableWidget, 'tableVseZayavki')              
                self.stackedWidget.setCurrentWidget(self.Operator)
                self.lybaya = Operator(self.tableVseZayavki) 


    def MasterButfunction(self):
        print("test2")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

    def ZakazchikButfunction(self):
        print("test4")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

    def OperatorsButfunction(self):
        print("test3")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()
    
    def AddRequestButfunction(self):
        print("testAddRequest")
        self.IDrequestLine = self.findChild(QLineEdit,'IDrequestLine')
        self.startDateLine = self.findChild(QLineEdit,'startDateLine')
        self.orgTechTypeIDLine = self.findChild(QLineEdit,'orgTechTypeIDLine')
        self.orgTechModelLine = self.findChild(QLineEdit,'orgTechModelLine')
        self.problemDescryptionLine = self.findChild(QLineEdit,'problemDescryptionLine')
        self.requestStatusIDLine = self.findChild(QLineEdit,'requestStatusIDLine')
        self.completionDateLine = self.findChild(QLineEdit,'completionDateLine')
        self.repairPartsLine = self.findChild(QLineEdit,'repairPartsLine')
        self.masterIDLine = self.findChild(QLineEdit,'masterIDLine')
        self.clientIDLine = self.findChild(QLineEdit,'clientIDLine')
        self.SaveButton = self.findChild(QPushButton, 'SaveButton')
        self.BackButtonReq = self.findChild(QPushButton, 'BackButtonReq')

        if not self.SaveButton or not self.BackButtonReq:
            print("Ошибка: кнопки SaveButton или BackButtonReq не найдены")
            return
        
        self.stackedWidget.setCurrentWidget(self.AddRequest)
        self.lybaya = AddRequest(self.IDrequestLine, self.startDateLine, self.orgTechModelLine, self.orgTechTypeIDLine, self.problemDescryptionLine,
                                 self.requestStatusIDLine,
                                 self.completionDateLine,
                                 self.repairPartsLine,
                                 self.masterIDLine,
                                 self.clientIDLine,
                                 self.SaveButton,
                                 self.BackButtonReq)
    
    def BackOperatorButfunction(self):
        print("test11")
        self.tableVseZayavki = self.findChild(QTableWidget, 'tableVseZayavki')              
        self.stackedWidget.setCurrentWidget(self.Operator)
        self.lybaya = Operator(self.tableVseZayavki) 

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
            elif typeUser[0] == 3:
                self.tableVseZayavki = self.findChild(QTableWidget, 'tableVseZayavki')              
                self.stackedWidget.setCurrentWidget(self.Operator)
                self.lybaya = Operator(self.tableVseZayavki) 

    def MasterButfunction(self):
        print("test2")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

    def ZakazchikButfunction(self):
        print("test4")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()

    def OperatorsButfunction(self):
        print("test3")
        self.stackedWidget.setCurrentWidget(self.Authorization)
        self.lybaya = Authorization()
    
    def AddRequestButfunction(self):
        print("testAddRequest")
        self.IDrequestLine = self.findChild(QLineEdit,'IDrequestLine')
        self.startDateLine = self.findChild(QLineEdit,'startDateLine')
        self.orgTechTypeIDLine = self.findChild(QLineEdit,'orgTechTypeIDLine')
        self.orgTechModelLine = self.findChild(QLineEdit,'orgTechModelLine')
        self.problemDescryptionLine = self.findChild(QLineEdit,'problemDescryptionLine')
        self.requestStatusIDLine = self.findChild(QLineEdit,'requestStatusIDLine')
        self.completionDateLine = self.findChild(QLineEdit,'completionDateLine')
        self.repairPartsLine = self.findChild(QLineEdit,'repairPartsLine')
        self.masterIDLine = self.findChild(QLineEdit,'masterIDLine')
        self.clientIDLine = self.findChild(QLineEdit,'clientIDLine')
        self.SaveButton = self.findChild(QPushButton, 'SaveButton')
        self.BackButtonReq = self.findChild(QPushButton, 'BackButtonReq')

        if not self.SaveButton or not self.BackButtonReq:
            print("Ошибка: кнопки SaveButton или BackButtonReq не найдены")
            return
        
        self.stackedWidget.setCurrentWidget(self.AddRequest)
        self.lybaya = AddRequest(self.BackButtonReq,
                                self.SaveButton,
                                self.IDrequestLine,
                                self.startDateLine,
                                self.orgTechTypeIDLine,
                                self.orgTechModelLine,
                                self.problemDescryptionLine,
                                self.requestStatusIDLine,
                                self.completionDateLine,
                                self.repairPartsLine,
                                self.masterIDLine,
                                self.clientIDLine)
    
    def BackOperatorButfunction(self):
        print("test11")
        self.tableVseZayavki = self.findChild(QTableWidget, 'tableVseZayavki')              
        self.stackedWidget.setCurrentWidget(self.Operator)
        self.lybaya = Operator(self.tableVseZayavki) 


    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignButton.clicked.connect(self.signupfunction)
        self.MasterBut.clicked.connect(self.MasterButfunction)
        self.ZakazchikBut.clicked.connect(self.ZakazchikButfunction)
        self.OperatorsBut.clicked.connect(self.OperatorsButfunction)
        self.AddButRequestBut.clicked.connect(self.AddRequestButfunction)

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