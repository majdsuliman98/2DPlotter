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


from plotter_main import Ui_MainWindow
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
        self.ui.stackedWidget1.setCurrentIndex(0)
        self.ui.Choose_img_btn.clicked.connect(self.BrowseImage)
        self.ui.Take_pic_btn.clicked.connect(self.openPicture)
        self.ui.capture_btn.clicked.connect(self.takePicture)
        self.ui.label_5.hide()
        self.ui.Draw_btn.clicked.connect(self.Draw)
        self.ui.Cancel_btn.clicked.connect(self.Cancel)
        self.ui.label_3.setStyleSheet("border: 1px solid black;")
        self.ui.label_4.setStyleSheet("border: 1px solid black;")

        self.ui.horizontalSlider.setMinimum(1)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.setValue(50)
        self.ui.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.ui.label_thresh.setText(str(float(self.ui.horizontalSlider.value())/100))


        self.Main.show()
        self.ui.horizontalSlider.valueChanged.connect(self.valuechanged)

        self.camera = QCamera()
        self.capture = QCameraImageCapture(self.camera)

        self.movie = QMovie('loading.gif')
        self.ui.label_5.setMovie(self.movie)

    
    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        
        self.displayImage(self.imgpth,self.img_name)
        self.ui.label_5.hide()
        self.ui.stackedWidget1.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget.setGeometry(QRect(0, 320, 671, 191))
        self.ui.stackedWidget1.setGeometry(QRect(-1, 0, 671, 311))

    def displayImage(self,imagepth,filename):
        threshold = float(self.ui.label_thresh.text())
        pixmap = QtGui.QPixmap(imagepth)
        self.ui.label_3.setPixmap(QtGui.QPixmap(imagepth))
        img2bmp(imagepth,filename)
        CovertToPBM(threshold,filename)
    
        pixmap1 = QtGui.QPixmap('./PBM images/'+filename+'.pbm')
        self.ui.label_4.setPixmap(pixmap1)

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
        
        if self.ui.label_3.pixmap()== None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Choose image first')
            msg.setWindowTitle("Error")
    
            x= msg.exec_()
        else:
            
            print(self.Filename)
            ConvertToSVG(self.Filename)
            FixSvgHeader(self.Filename)
            ConvertToGCode(self.Filename)
    
    def openPicture(self):
        self.ui.viewfinder.show()
        self.ui.capture_btn.show()
        self.ui.stackedWidget1.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.stackedWidget.setGeometry(QRect(0, 440, 671, 151))
        self.ui.stackedWidget1.setGeometry(QRect(-1, 0, 671, 441))
        self.available_cameras = QCameraInfo.availableCameras()

		# if no camera found
        if not self.available_cameras:
        
			# exit the code
            sys.exit()   
            # creating a QCameraViewfinder object

        
        
		# showing this viewfinder
        
        self.camera.setViewfinder(self.ui.viewfinder)
        self.camera.start()
    
    def takePicture(self):

        
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
        self.imgpth = "/home/pi/Desktop/2d printer/images_taken/{}.jpg".format(timestamp)
        self.capture.capture(self.imgpth)
        self.img_name = timestamp
        self.ui.viewfinder.hide()
        self.ui.capture_btn.hide()
        self.ui.label_5.show()
        self.Filename = self.img_name
        
        self.startAnimation()
        timer = QTimer()
        timer.singleShot(3000,self.stopAnimation)
        
        
        

        
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    UImain = UI()
    sys.exit(app.exec_())