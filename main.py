from PyQt5.QtWidgets import QApplication, QWidget,QStackedWidget, QPushButton, QVBoxLayout,QGraphicsView, QWizard, QMainWindow, QLabel,QDialog, QFileDialog,QMessageBox, QGraphicsOpacityEffect, QSlider
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys
import os
import sys
import time
from PyQt5 import QtGui
from PyQt5 import uic
import sys
import qdarkstyle
from Functions import *
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from read_gcode import *
from main_screen import Ui_MainWindow
Filename = ''
class UI:
    def __init__(self):
        self.Main = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Main)
        self.Filename = ''
        self.imgpth = ''
        # Initialize 
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.upload_btn.clicked.connect(self.BrowseImage)
        self.ui.picture_btn.clicked.connect(self.openPicture)
        self.ui.capture_btn.clicked.connect(self.takePicture)
        # self.ui.label_5.hide()
        
        self.ui.draw_btn.clicked.connect(self.Draw)
        self.ui.back_btn.clicked.connect(self.Cancel)
        self.ui.back_btn1.clicked.connect(self.Cancel)
        self.ui.quit_button.clicked.connect(self.Quit)

        self.ui.horizontalSlider.setMinimum(1)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.setValue(50)
        self.ui.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.ui.label_thresh.setText(str(float(self.ui.horizontalSlider.value())/100))


        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.img_loading = QLabel(self.page_4)
        self.img_loading.setGeometry(QRect(250, 40, 201, 221))
        self.gif = QtGui.QPixmap('loading.gif')
        self.img_loading.setPixmap(self.gif)
        self.ui.stackedWidget.addWidget(self.page_4)

        self.Main.setWindowFlags(Qt.FramelessWindowHint)
        self.Main.show()
        self.ui.horizontalSlider.valueChanged.connect(self.valuechanged)

        self.camera = QCamera()
        self.capture = QCameraImageCapture(self.camera)

        self.movie = QMovie('loading.gif')
        self.img_loading.setMovie(self.movie)

    def Quit(self):
        sys.exit()
    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        
        self.displayImage(self.imgpth,self.img_name)
        # self.ui.label_5.hide()
        self.ui.stackedWidget.setCurrentIndex(1)
        

    def displayImage(self,imagepth,filename):
        threshold = float(self.ui.label_thresh.text())
        
        img2bmp(imagepth,filename)
        CovertToPBM(threshold,filename)

        pixmap = QtGui.QPixmap('./PBM images/'+filename+'.bmp')
        self.ui.img_choosen.setPixmap(pixmap)
    
        pixmap1 = QtGui.QPixmap('./PBM images/'+filename+'.pbm')
        self.ui.filtered_image.setPixmap(pixmap1)

    def valuechanged(self):
        val = self.ui.horizontalSlider.value()
        self.ui.label_thresh.setText(str(float(val)/100))

        if self.imgpth:
            self.displayImage(self.imgpth,self.Filename)

    def BrowseImage(self):
        fname = QFileDialog.getOpenFileName(None,'Open File', 'c:\\', 'Image files (*.jpg *png *.jpeg)')
        

        imagepth = fname[0]
        if(imagepth == ""):
            return

        else:
            self.ui.stackedWidget.setCurrentIndex(1)
            head ,tail = os.path.split(imagepth)    
            filename = tail.split('.')[0]
            print(filename)
            self.displayImage(imagepth,filename)
            
            self.imgpth = imagepth
            self.Filename = filename
          
    
            
            
            
    def Cancel(self):
        self.ui.stackedWidget.setCurrentIndex(0)
       

    def Draw(self):
        
        if self.ui.img_choosen.pixmap()== None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Choose image first')
            msg.setWindowTitle("Error")
            msg.setStyleSheet("border: 1px solid black;border-color:white;border-radius:10px")
            x= msg.exec_()
        else:
            
            print(self.Filename)
            ConvertToSVG(self.Filename)
            FixSvgHeader(self.Filename)
            ConvertToGCode(self.Filename)

            parser = Gcode()
            parser.read_gcode(self.Filename)
            parser.startDrawing()
    
    def openPicture(self):
        
        self.available_cameras = QCameraInfo.availableCameras()
       
        # if no camera found
        if not self.available_cameras:
        
            # exit the code
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please connect a camera first!')
            msg.setWindowTitle("Error")  
            msg.setWindowFlags(Qt.FramelessWindowHint)
            msg.setStyleSheet("border-radius:10px")
            x= msg.exec_()
            return
            # creating a QCameraViewfinder object

        
        self.ui.viewfinder.show()
        self.ui.capture_btn.show()
        self.ui.stackedWidget.setCurrentIndex(2)
      
        
        self.camera.setViewfinder(self.ui.viewfinder)
        self.camera.start()
    
    def takePicture(self):

        
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
        self.imgpth = "/home/pi/Desktop/New interface/2d plotter/images_taken/{}.jpg".format(timestamp)
        self.capture.capture(self.imgpth)
        self.img_name = timestamp
        # self.ui.viewfinder.hide()
        # self.ui.capture_btn.hide()
        
        # self.ui.label_5.show()
        self.Filename = self.img_name
        self.ui.stackedWidget.setCurrentIndex(3)
        self.startAnimation()
        
        timer = QTimer()
        timer.singleShot(3000,self.stopAnimation)
        
        
        

        
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    UImain = UI()
    sys.exit(app.exec_())