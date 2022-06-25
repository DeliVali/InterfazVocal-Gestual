
import sys
sys.path.append('../Proyecto Python')

from ControlVWindow import voiceWindow
import HandTrackingModule
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def run(self):
            HandTrackingModule.mainConfiguration()
              



class Ui_MainWindow(object):
        
        #Se le tiene que pasar el self al metodo al momento de unirlo con el boton
    def abrirVentanaVoz(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=voiceWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Clicked")    

    def abrirVentanaGestos(self):
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
        
        
        #Ventana Primcipal
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 474)
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(209, 217, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 190, 531, 201))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gestureWindowBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.gestureWindowBtn.setStyleSheet("QPushButton{\n"
"border: .1px solid #900;\n"
"border-bottom: none;\n"
"border-radius:8px;\n"
"padding:0px;\n"
"transition: 2s;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(126, 129, 180);\n"
"padding:2px\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(77, 90, 173);}")
        #Boton ventana de gestos
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui\icons\hand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gestureWindowBtn.setIcon(icon)
        self.gestureWindowBtn.setIconSize(QtCore.QSize(41, 84))
        self.gestureWindowBtn.setFlat(True)
        self.gestureWindowBtn.setObjectName("gestureWindowBtn")
        #Evento del boton
        self.gestureWindowBtn.clicked.connect(self.abrirVentanaGestos)
        self.horizontalLayout_2.addWidget(self.gestureWindowBtn)
        spacerItem = QtWidgets.QSpacerItem(156, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.voiceWindowBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.voiceWindowBtn.setStyleSheet("QPushButton{\n"
"border: .1px solid #900;\n"
"border-bottom: none;\n"
"border-radius:8px;\n"
"padding:0px;\n"
"transition: 2s;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(126, 129, 180);\n"
"padding:2px\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(77, 90, 173);}")
        #Boton Ventana de voz
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Gui\icons\controlvoz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.voiceWindowBtn.setIcon(icon1)
        self.voiceWindowBtn.setIconSize(QtCore.QSize(41, 84))
        self.voiceWindowBtn.setFlat(True)
        #Evento del boton
        self.voiceWindowBtn.clicked.connect(self.abrirVentanaVoz)
        #id del boton
        self.voiceWindowBtn.setObjectName("voiceWindowBtn")
        self.horizontalLayout_2.addWidget(self.voiceWindowBtn)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("  background: rgba(76, 175, 80, 0.000001) /* Green background with 30% opacity */")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 30, 91, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border: .1px solid #900;\n"
"border-bottom: none;\n"
"border-radius:8px;\n"
"padding:0px;\n"
"transition: 2s;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(126, 129, 180);\n"
"padding:2px\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(77, 90, 173);}")
        #Boton de información
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Gui\icons\information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gestureWindowBtn.setText(_translate("MainWindow", "Control de gestos"))
        self.voiceWindowBtn.setText(_translate("MainWindow", "Control de Voz"))
        #Label name
        self.label.setText(_translate("MainWindow", "Asistente Virtual"))
        self.pushButton.setText(_translate("MainWindow", "Information"))
        
        


#Función main ,muestra la ventana
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
