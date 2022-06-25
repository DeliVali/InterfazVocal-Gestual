# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlVWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from threading import Thread
from _VoiceCommandList import Ui_InformationVoice

sys.path.append('C:/Users/jeffr/OneDrive/Documentos/UV/7mo semestre/INTERFACES DE USUARIO AVANZADAS/Proyecto Python')
import VoiceRecognition

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
            VoiceRecognition.run() 
              
    


class voiceWindow(object):
        #Main Window
    def abrirlistaComandos(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_InformationVoice()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Clicked")  
          
    def labelChange(self,command,response):
        self.indicationLabel.setText(command)
        self.ResponseLabel.setText(response)
           
    def executeCommand(self):
            command=self.inputText.toPlainText()
            VoiceRecognition.run_ai_Command(command)
            voiceWindow.labelChange(self,command,VoiceRecognition.Responses.response_get(VoiceRecognition.Responses))
            self.inputText.clear()
        
                
    def setupUi(self, MainWindow):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 398)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 50, 721, 291))
        self.frame.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.indicationLabel = QtWidgets.QLabel(self.frame)
        self.indicationLabel.setGeometry(QtCore.QRect(190, 30, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Astralaga Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.indicationLabel.setFont(font)
        self.indicationLabel.setStyleSheet("background-color: rgb(98, 101, 173);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:20px;")
        #indication label
        self.indicationLabel.setScaledContents(True)
        self.indicationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.indicationLabel.setWordWrap(False)
        self.indicationLabel.setObjectName("indicationLabel")
        self.ResponseLabel = QtWidgets.QLabel(self.frame)
        self.ResponseLabel.setGeometry(QtCore.QRect(0, 110, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Astralaga Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ResponseLabel.setFont(font)
        self.ResponseLabel.setStyleSheet("background-color: rgb(113, 173, 143);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"")
        #Response label
        self.ResponseLabel.setScaledContents(True)
        self.ResponseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ResponseLabel.setWordWrap(False)
        self.ResponseLabel.setObjectName("ResponseLabel")
        
        
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, -50, 611, 101))
        self.frame_2.setStyleSheet("background-color: rgb(159, 168, 218);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Astralaga")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"\n"
"color: rgb(255, 255, 255);")
        
        
        #Information button
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.InformationButton = QtWidgets.QPushButton(self.frame_2)
        self.InformationButton.setGeometry(QtCore.QRect(514, 60, 81, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui\icons\information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InformationButton.setIcon(icon)
        self.InformationButton.setFlat(True)
        self.InformationButton.clicked.connect(self.abrirlistaComandos)
        
        
     
        self.inputText = QtWidgets.QTextEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(0, 340, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputText.setFont(font)
        self.inputText.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(98, 101, 173);\n"
"color: rgb(255, 255, 255);\n"
"")
        #Input text box
        self.inputText.setObjectName("inputText")
        self.commandButton = QtWidgets.QPushButton(self.centralwidget)
        self.commandButton.setGeometry(QtCore.QRect(540, 340, 61, 31))
        self.commandButton.setStyleSheet("background-color: rgb(104, 80, 153);")
        self.commandButton.setText("")
        
        #Command Button
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Gui\icons\Bnext.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandButton.setIcon(icon2)
        self.commandButton.setIconSize(QtCore.QSize(21, 27))
        self.commandButton.setFlat(False)
        self.commandButton.setObjectName("commandButton")
        self.frame_2.raise_()
        self.frame.raise_()
        self.inputText.raise_()
        self.commandButton.raise_()
        #Funcion del boton para ejecutar los comandos
        self.commandButton.clicked.connect(self.executeCommand)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.indicationLabel.setText(_translate("MainWindow", "Su indicación aparecera aqui"))
        self.ResponseLabel.setText(_translate("MainWindow", "Su respuesta aparecera aqui"))
        self.label.setText(_translate("MainWindow", "Interfaz Vocal"))
        self.InformationButton.setText(_translate("MainWindow", "Información"))
        self.inputText.setPlaceholderText(_translate("MainWindow", "Escriba un comando..."))

    
        



if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = voiceWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()       
        sys.exit(app.exec_())
