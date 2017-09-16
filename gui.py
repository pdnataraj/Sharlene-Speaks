#!bin/python3
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QMainWindow,
                             QAction,qApp, QPushButton, QGridLayout)
from PyQt5.QtGui import QIcon


class App_Window(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.resize(800, 800)
        self.setWindowTitle('Sharlene Speaks')  
        
        # Add menu bar
        exitAct = QAction(QIcon('exit.png'), '&Exit', self) 
        exitAct.setToolTip("Exit Application")
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)   
        menubar.setNativeMenuBar(False)   
        
        self.center()     
        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)
        self.show()
    
    def center(self):
            
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())  
        
class MainWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)
        left = [1,3,5,7,9]
        right = [2,4,6,8,10]               
        for i in range(5):
           
            self.buttonLeft = QPushButton(str(left[i]))
            self.buttonLeft.setToolTip("Upload .wav file...")
            self.buttonLeft.clicked.connect(self.upload_wav)
            self.layout.addWidget(self.buttonLeft,i+1,0)
            
            self.buttonRight = QPushButton(str(right[i]))
            self.buttonRight.setToolTip("Upload .wav file...")
            self.buttonRight.clicked.connect(self.upload_wav)
            self.layout.addWidget(self.buttonRight,i+1,1)

        self.setLayout(self.layout)
    
    def upload_wav(self):
        print("success")
         
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))
    ex = App_Window()
    sys.exit(app.exec_())