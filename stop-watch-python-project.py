# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'J.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtGui, QtCore, QtWidgets, Qt
 
s = 0
m = 0
h = 0

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Seconds = QtWidgets.QLCDNumber(self.centralwidget)
        self.Seconds.setGeometry(QtCore.QRect(180, 130, 391, 151))
        self.Seconds.setObjectName("Seconds")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 80, 101, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 80, 101, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 70, 91, 51))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(200, 310, 81, 23))
        self.Start.setObjectName("Start")

        self.Lap = QtWidgets.QPushButton(self.centralwidget)
        self.Lap.setGeometry(QtCore.QRect(290, 310, 81, 23))
        self.Lap.setObjectName("Lap")

        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(380, 310, 81, 23))
        self.Stop.setObjectName("Stop")

        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(470, 310, 81, 23))
        self.Reset.setObjectName("Reset")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 350, 256, 192))
        self.textBrowser.setObjectName("textBrowser")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Time)

        self.Start.clicked.connect(self.Starto)
        self.Lap.clicked.connect(self.Laps)
        self.Stop.clicked.connect(self.Stops)
        self.Reset.clicked.connect(self.Resets)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Hour"))
        self.label_2.setText(_translate("MainWindow", "Minute"))
        self.label_3.setText(_translate("MainWindow", "Second"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.Lap.setText(_translate("MainWindow", "Lap"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.Reset.setText(_translate("MainWindows", "Reset"))

    def Starto(self):
        global s
        self.timer.start(1000)
        
    def Time(self):
        global s,m,h
        if s < 59:
            s += 1
        else:
            if m < 59:
                s = 0
                m += 1
            elif m == 59 and h < 24:
                h += 1
                m = 0
                s = 0
            else:
                self.timer.stop()
 
        time = "{0}:{1}:{2}".format(h,m,s)
        self.Seconds.setDigitCount(len(time))
        self.Seconds.display(time)

    def Laps(self):
        time = "{0}:{1}:{2}".format(h,m,s)
        self.textBrowser.setText(time)

    def Stops(self):
        self.timer.stop()
        
    def do_pause(self):
        self.timer.stop()
        self.start.clicked.disconnect()

    def Resets(self):
        global s,m,h
        self.timer.stop()
        s = 0
        m = 0
        h = 0
        time = "{0}:{1}:{2}".format(h,m,s)
        self.Seconds.setDigitCount(len(time))
        self.Seconds.display(time)
            
    def main():
        app = Qt.QApplication(sys.argv)
        main= Main()
        main.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    main()

