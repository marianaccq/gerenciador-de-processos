# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gerenciador-processos2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets

class Second(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.label = QtWidgets.QLabel(Ui_GroupBox.print_prioridade)

class Ui_GroupBox(object):

    def atualizar_processos(self):
        self.filtro = self.textEdit_4.toPlainText()

        if self.filtro != None:
            self.listagem_processos()
        else:
            self.filtrar_processo()

    def botao_kill(self):
        self.pid = self.textEdit.toPlainText()
        self.textEdit.update()
        os.system("kill " + self.pid + " > kill.txt")
        kill = open("kill.txt").read()
        self.plainTextEdit.setPlainText(self.listagem_processos())
        self.textEdit.setText("")
        print("matou: " + self.pid)
        return kill

    def botao_stop(self):
        self.pid = self.textEdit.toPlainText()
        self.textEdit.update()
        os.system("kill -STOP" + self.pid + " > stop.txt")
        stop = open("stop.txt").read()
        self.plainTextEdit.setPlainText(self.listagem_processos())
        self.textEdit.setText("")
        print("stop: " + self.pid)
        return stop

    def botao_cont(self):
        self.pid = self.textEdit.toPlainText()
        self.textEdit.update()
        os.system("kill -CONT" + self.pid + " > cont.txt")
        cont = open("cont.txt").read()
        self.plainTextEdit.setPlainText(self.listagem_processos())
        self.textEdit.setText("")
        print("cont: " + self.pid)
        return cont

    def listagem_processos(self):
        os.system("ps -aux > listagem.txt")
        listagem = open("listagem.txt").read()
        return listagem

    def filtrar_processo(self):
        self.filtro = self.textEdit_4.toPlainText()
        self.textEdit_4.update()
        os.system("ps -A | grep " + self.filtro + " > filtro.txt")
        filtro_resultado = open("filtro.txt").read()
        self.plainTextEdit.setPlainText(filtro_resultado)

    def limpar_filtro(self):
        self.plainTextEdit.setPlainText(self.listagem_processos())
        self.textEdit_4.setText("")

    def definindo_prioridade(self):
        self.prioridade = self.textEdit_2.toPlainText()
        self.textEdit_2.update()
        self.pid = self.textEdit.toPlainText()
        self.textEdit.update()
        os.system("renice " + self.prioridade + " -p " + self.pid +" > prioridade.txt")
        prioridade_resultado = open("prioridade.txt").read()
        print("prioridade " + self.prioridade + "definida ao processo " + self.pid)
        #self.label = QtWidgets.QLabel("Prioridade " + self.textEdit_2.toPlainText() + " definida ao processo com PID " + self.textEdit.toPlainText())
        #self.label_20.setGeometry(QtCore.QRect(10, 320, 100, 17))
        #self.label_20.setText("Prioridade " + self.textEdit_2.toPlainText() + " definida ao processo com PID " + self.textEdit.toPlainText())
        #self.label_20.show()
        #self.dialog = Second()
        #self.dialog.show()

        return prioridade_resultado

    def print_prioridade(self):
        texto = "Prioridade " + self.textEdit_2.toPlainText() + " definida ao processo com PID " + self.textEdit.toPlainText()
        self.textEdit_2.setText("")
        self.textEdit.setText("")
        return texto




    def setupUi(self, GroupBox):

        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_processos)
        self.timer.start(1000)

        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(625, 450)

        #kill
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setGeometry(QtCore.QRect(220, 240, 51, 31))
        self.pushButton.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.pushButton.setObjectName("pushButton")
        #stop
        self.pushButton_2 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 240, 51, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(233, 185, 110);\n"
"background-color: rgb(239, 41, 41);")
        self.pushButton_2.setObjectName("pushButton_2")
        #cont
        self.pushButton_3 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 240, 51, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton_3.setObjectName("pushButton_3")

        #ok filtro

        self.pushButton_4 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 180, 51, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(114, 159, 207);\n"            
"background-color: rgb(233, 185, 110);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("ok")

        #ok prioridade
        self.pushButton_5 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 310, 51, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(114, 159, 207);\n"
                                        "background-color: rgb(233, 185, 110);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("ok")
        self.pushButton_5.clicked.connect(self.definindo_prioridade)

        #ok cpu
        self.pushButton_6 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 370, 51, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(114, 159, 207);\n"
                                        "background-color: rgb(233, 185, 110);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText("ok")

        #limpar filtro
        self.pushButton_7 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 220, 51, 31))
        self.pushButton_7.setStyleSheet("background-color: rgb(114, 159, 207);\n"
                                        "background-color: rgb(235, 185, 110);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText("limpar")
        self.pushButton_7.clicked.connect(self.limpar_filtro)





        #labels
        self.label = QtWidgets.QLabel(GroupBox)
        self.label.setGeometry(QtCore.QRect(10, 250, 51, 17))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(GroupBox)
        self.label_2.setGeometry(QtCore.QRect(310, 190, 111, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(GroupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 81, 17))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(GroupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 51, 17))
        self.label_4.setObjectName("label_4")
        #cpu 1
        self.progressBar_2 = QtWidgets.QProgressBar(GroupBox)
        self.progressBar_2.setGeometry(QtCore.QRect(390, 350, 201, 16))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        # cpu 0
        self.progressBar_3 = QtWidgets.QProgressBar(GroupBox)
        self.progressBar_3.setGeometry(QtCore.QRect(390, 330, 201, 16))
        self.progressBar_3.setStyleSheet("")
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        #cpu 2
        self.progressBar_4 = QtWidgets.QProgressBar(GroupBox)
        self.progressBar_4.setGeometry(QtCore.QRect(390, 370, 201, 16))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        #cpu 3
        self.progressBar_5 = QtWidgets.QProgressBar(GroupBox)
        self.progressBar_5.setGeometry(QtCore.QRect(390, 390, 201, 16))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")

        self.label_5 = QtWidgets.QLabel(GroupBox)
        self.label_5.setGeometry(QtCore.QRect(400, 300, 101, 17))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(GroupBox)
        self.label_6.setGeometry(QtCore.QRect(330, 330, 51, 17))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(GroupBox)
        self.label_7.setGeometry(QtCore.QRect(330, 350, 51, 17))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(GroupBox)
        self.label_8.setGeometry(QtCore.QRect(330, 370, 51, 17))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(GroupBox)
        self.label_9.setGeometry(QtCore.QRect(330, 390, 51, 17))
        self.label_9.setObjectName("label_9")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(GroupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 611, 141))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlainText(self.listagem_processos())
        self.plainTextEdit.update()

        #pid
        self.textEdit = QtWidgets.QTextEdit(GroupBox)
        self.textEdit.setGeometry(QtCore.QRect(130, 240, 81, 31))
        self.textEdit.setObjectName("textEdit")
        #self.pid = self.textEdit.toPlainText()
        print("oi")
        self.pushButton.clicked.connect(self.botao_kill)
        self.pushButton_2.clicked.connect(self.botao_stop)
        self.pushButton_3.clicked.connect(self.botao_cont)




        #prioridade
        self.textEdit_2 = QtWidgets.QTextEdit(GroupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 310, 161, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        #cpu
        self.textEdit_3 = QtWidgets.QTextEdit(GroupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(50, 370, 121, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        #filtro
        self.textEdit_4 = QtWidgets.QTextEdit(GroupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(370, 180, 191, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_4.clicked.connect(self.filtrar_processo)

        #filtro = self.textEdit_4.toPlainText()
        #os.system("ps –auf | grep" + filtro + " > filtro.txt")
        #filtro_texto = open("filtro.txt").read()
        #self.textBrowser_2.setPlainText(filtro_texto)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        GroupBox.setTitle(_translate("GroupBox", "Gerenciador de processos"))
        self.pushButton.setText(_translate("GroupBox", "Kill"))
        self.pushButton_2.setText(_translate("GroupBox", "Stop"))
        self.pushButton_3.setText(_translate("GroupBox", "Cont"))
        self.label.setText(_translate("GroupBox", "PID do processo:"))
        self.label_2.setText(_translate("GroupBox", "Filtro:"))
        self.label_3.setText(_translate("GroupBox", "Prioridade:"))
        self.label_4.setText(_translate("GroupBox", "CPU:"))
        self.label_5.setText(_translate("GroupBox", "Carga de CPU"))
        self.label_6.setText(_translate("GroupBox", "CPU 0"))
        self.label_7.setText(_translate("GroupBox", "CPU 1"))
        self.label_8.setText(_translate("GroupBox", "CPU 2"))
        self.label_9.setText(_translate("GroupBox", "CPU 3"))
        GroupBox.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GroupBox = QtWidgets.QGroupBox()
    ui = Ui_GroupBox()
    ui.setupUi(GroupBox)
    GroupBox.show()

    sys.exit(app.exec_())

