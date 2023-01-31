# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, 60, 701, 341))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.upload_btn = QtWidgets.QToolButton(self.page)
        self.upload_btn.setGeometry(QtCore.QRect(110, 60, 184, 151))
        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.upload_btn.setFont(font)
        self.upload_btn.setStyleSheet("background-color:transparent;\n"
"border-style: outset;\n"
"   border-width: 2px;\n"
"    border-color: white;\n"
"border-radius:10px\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/AddImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_btn.setIcon(icon)
        self.upload_btn.setIconSize(QtCore.QSize(90, 90))
        self.upload_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.upload_btn.setObjectName("upload_btn")
        self.picture_btn = QtWidgets.QToolButton(self.page)
        self.picture_btn.setGeometry(QtCore.QRect(404, 60, 184, 151))
        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.picture_btn.setFont(font)
        self.picture_btn.setStyleSheet("background-color:transparent;\n"
"border-style: outset;\n"
"   border-width: 2px;\n"
"    border-color: white;\n"
"border-radius:10px\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resources/Camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.picture_btn.setIcon(icon1)
        self.picture_btn.setIconSize(QtCore.QSize(90, 90))
        self.picture_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.picture_btn.setObjectName("picture_btn")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.img_choosen = QtWidgets.QLabel(self.page_2)
        self.img_choosen.setGeometry(QtCore.QRect(38, 40, 291, 221))
        self.img_choosen.setStyleSheet("border: 1px solid black;border-color:white;border-radius:10px")
        self.img_choosen.setText("")
        self.img_choosen.setScaledContents(True)
        self.img_choosen.setObjectName("img_choosen")
        self.filtered_image = QtWidgets.QLabel(self.page_2)
        self.filtered_image.setGeometry(QtCore.QRect(368, 40, 291, 221))
        self.filtered_image.setStyleSheet("border: 1px solid ;border-color:white;border-radius:10px")
        self.filtered_image.setText("")
        self.filtered_image.setScaledContents(True)
        self.filtered_image.setObjectName("filtered_image")
        self.draw_btn = QtWidgets.QToolButton(self.page_2)
        self.draw_btn.setGeometry(QtCore.QRect(510, 280, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.draw_btn.setFont(font)
        self.draw_btn.setStyleSheet("border: 1px solid black;border-color:white;border-radius:10px;background-color:transparent")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./resources/Pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.draw_btn.setIcon(icon2)
        self.draw_btn.setIconSize(QtCore.QSize(24, 24))
        self.draw_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.draw_btn.setObjectName("draw_btn")
        self.horizontalSlider = QtWidgets.QSlider(self.page_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 290, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_thresh = QtWidgets.QLabel(self.page_2)
        self.label_thresh.setGeometry(QtCore.QRect(360, 291, 40, 16))
        self.label_thresh.setObjectName("label_thresh")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(40, 290, 141, 16))
        self.label_6.setObjectName("label_6")
        self.back_btn1 = QtWidgets.QToolButton(self.page_2)
        self.back_btn1.setGeometry(QtCore.QRect(10, 10, 80, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn1.setFont(font)
        self.back_btn1.setStyleSheet("border-radius:10px;background-color:transparent")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./resources/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn1.setIcon(icon3)
        self.back_btn1.setIconSize(QtCore.QSize(28, 28))
        self.back_btn1.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.back_btn1.setObjectName("back_btn1")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.viewfinder = QCameraViewfinder(self.page_3)
        self.viewfinder.setGeometry(QtCore.QRect(290, 10, 401, 321))
        self.viewfinder.setStyleSheet("border:1px solid;\n"
"border-color:white;\n"
"border-radius:10px;\n"
"\n"
"")
        self.viewfinder.setObjectName("viewfinder")
        self.back_btn = QtWidgets.QToolButton(self.page_3)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 80, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("border-radius:10px;background-color:transparent")
        self.back_btn.setIcon(icon3)
        self.back_btn.setIconSize(QtCore.QSize(28, 28))
        self.back_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.back_btn.setObjectName("back_btn")
        self.capture_btn = QtWidgets.QPushButton(self.page_3)
        self.capture_btn.setGeometry(QtCore.QRect(70, 100, 150, 150))
        self.capture_btn.setStyleSheet("background-color:transparent;\n"
"border-style: outset;\n"
"   border-width: 2px;\n"
"    border-color: white;\n"
"border-radius:10px\n"
"")
        self.capture_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./resources/Unsplash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.capture_btn.setIcon(icon4)
        self.capture_btn.setIconSize(QtCore.QSize(100, 100))
        self.capture_btn.setObjectName("capture_btn")
        self.stackedWidget.addWidget(self.page_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(640, 5, 61, 51))
        self.quit_button.setStyleSheet("background-color:transparent;\n"
"\n"
"")
        self.quit_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./resources/Shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_button.setIcon(icon5)
        self.quit_button.setIconSize(QtCore.QSize(42, 42))
        self.quit_button.setObjectName("quit_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.upload_btn.setText(_translate("MainWindow", "Upload"))
        self.picture_btn.setText(_translate("MainWindow", "picture"))
        self.draw_btn.setText(_translate("MainWindow", "DRAW"))
        self.label_thresh.setText(_translate("MainWindow", "1.0"))
        self.label_6.setText(_translate("MainWindow", "ADJUST THRESHOLD:"))
        self.back_btn1.setText(_translate("MainWindow", "BACK"))
        self.back_btn.setText(_translate("MainWindow", "BACK"))
        self.label.setText(_translate("MainWindow", "PLOTTER"))

from PyQt5.QtMultimediaWidgets import QCameraViewfinder

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

