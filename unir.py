# Form implementation generated from reading ui file 'unir.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 191)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_nome = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_nome.setObjectName("label_nome")
        self.verticalLayout.addWidget(self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.verticalLayout.addWidget(self.lineEdit_nome)
        self.label_sobrenome = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_sobrenome.setObjectName("label_sobrenome")
        self.verticalLayout.addWidget(self.label_sobrenome)
        self.lineEdit_sobrenome = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_sobrenome.setObjectName("lineEdit_sobrenome")
        self.verticalLayout.addWidget(self.lineEdit_sobrenome)
        self.pushButton_unir = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_unir.setObjectName("pushButton_unir")
        
        self.pushButton_unir.clicked.connect(self.unir)
        
        self.verticalLayout.addWidget(self.pushButton_unir)
        self.label_completo = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_completo.setObjectName("label_completo")
        self.verticalLayout.addWidget(self.label_completo)
        self.lineEdit_completo = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_completo.setObjectName("lineEdit_completo")
        self.verticalLayout.addWidget(self.lineEdit_completo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_sobrenome.setText(_translate("MainWindow", "Sobrenome:"))
        self.pushButton_unir.setText(_translate("MainWindow", "UNIR"))
        self.label_completo.setText(_translate("MainWindow", "Completo:"))
        
        
    def unir(self):
        nome = self.lineEdit_nome.text()
        sobrenome = self.lineEdit_sobrenome.text()
        completo = nome + " " + sobrenome
        self.lineEdit_completo.setText(completo)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
