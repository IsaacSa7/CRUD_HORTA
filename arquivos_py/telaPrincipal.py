# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName("TelaPrincipal")
        TelaPrincipal.resize(450, 423)
        TelaPrincipal.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(TelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCadastra = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastra.setGeometry(QtCore.QRect(160, 110, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnCadastra.setFont(font)
        self.btnCadastra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnCadastra.setObjectName("btnCadastra")
        self.btnPesquisa = QtWidgets.QPushButton(self.centralwidget)
        self.btnPesquisa.setGeometry(QtCore.QRect(160, 220, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnPesquisa.setFont(font)
        self.btnPesquisa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnPesquisa.setObjectName("btnPesquisa")
        TelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 20))
        self.menubar.setObjectName("menubar")
        TelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaPrincipal)
        self.statusbar.setObjectName("statusbar")
        TelaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(TelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

    def retranslateUi(self, TelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "TELA PRINCIPAL"))
        self.btnCadastra.setText(_translate("TelaPrincipal", "Cadastrar"))
        self.btnPesquisa.setText(_translate("TelaPrincipal", "Pesquisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_TelaPrincipal()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())