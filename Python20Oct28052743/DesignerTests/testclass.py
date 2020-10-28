import os, datetime, shutil, time, git, sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class car(QWidget): 
      
    # init method or constructor 
    def __init__(self, gobuttonact): 
        super().__init__()
        self.initui()

    def initui(self):
    
    #mmain window    
        mainlayout = QGridLayout()
        self.setLayout(mainlayout)
        self.setWindowTitle("smadagitbackup")
        w=596
        h=380
        self.setGeometry(0,0,w,h)
        centerpoint = QDesktopWidget().screenGeometry().center()
        newpos = self.frameGeometry()
        newpos.moveCenter(centerpoint)
        self.move(newpos.topLeft())   
    
    #set the GO button to the function passed in
        gobutton = QPushButton()
        mainlayout.addWidget(gobutton,2,2,1,1)
        gobutton.setText(textin)
        gobutton.setMinimumSize(101,23)
        gobutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gobutton.setStyleSheet("border: 1px solid black;background-color: aqua;")
        gobutton.clicked.connect(lambda: buttonact(gobutton, printtest))

        
def dobutton(parm1, parm2):
    print("testing")
    print(parm2)
    parm1.setStyleSheet("border: 1px solid black;background-color: green;")
    

app = QApplication(sys.argv)
model=""
color=""
textin = "OH"
buttonact=dobutton
doit = car(model, color, textin, buttonact)
doit.show()
sys.exit(app.exec_())

#audi = car("audi a4", "blue") 
#ferrari = car("ferrari 488", "green") 
#audi.writeit()     # same output as car.show(audi) 
#ferrari.writeit()  # same output as car.show(ferrari) 
  