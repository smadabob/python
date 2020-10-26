import os, datetime, shutil, time, git, sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class gitbackup(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainlayout = QGridLayout()
        #---------------------------------------------------------------------
        githublabel = QLabel("Github Location:")
        mainlayout.addWidget(githublabel,0,0,1,1)
        #lastfolder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        githublabel.setMinimumSize(60,20)
        githublabel.setStyleSheet("border: 1px solid black;background-color: aqua;")
        #---------------------------------------------------------------------
        githubloc = QLabel()
        mainlayout.addWidget(githubloc,0,1,1,3)
        #lastfolder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        githubloc.setMinimumSize(450,20)
        githubloc.setStyleSheet("border: 1px solid black;background-color: aqua;")
        #---------------------------------------------------------------------
        folderlabel = QLabel("Folder to Zip:")
        mainlayout.addWidget(folderlabel,1,0,1,1)
        #lastfolder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        folderlabel.setMinimumSize(60,20)
        folderlabel.setStyleSheet("border: 1px solid black;background-color: aqua;")
        #---------------------------------------------------------------------
        folderloc = QLabel()
        mainlayout.addWidget(folderloc,1,1,1,3)
        #lastfolder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        folderloc.setMinimumSize(450,20)
        folderloc.setStyleSheet("border: 1px solid black;background-color: aqua;")
        #---------------------------------------------------------------------
        mainlayout.addItem(QSpacerItem(210, 20), 2, 0, 1, 2)
        #---------------------------------------------------------------------
        self.gobutton = QPushButton("GO!")
        #self.gobutton.clicked.connect(self.dobutton)
        mainlayout.addWidget(self.gobutton,2,2,1,1)
        self.gobutton.setMinimumSize(101,23)
        #gobutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gobutton.setStyleSheet("border: 1px solid black;background-color: aqua;")
        
        #---------------------------------------------------------------------
        mainlayout.addItem(QSpacerItem(228, 20), 2, 3, 1, 1)
        #---------------------------------------------------------------------
        mainlayout.addItem(QSpacerItem(20, 21), 3, 2, 1, 1)
        #---------------------------------------------------------------------
        progresstext = QLabel()
        mainlayout.addWidget(progresstext,4,0,1,4)
        #lastfolder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        progresstext.setMinimumSize(571,221)
        progresstext.setStyleSheet("border: 1px solid black;background-color: aqua;")
        self.setLayout(mainlayout)
        self.setWindowTitle("smadagitbackup")
        w=596
        h=380
        self.setGeometry(0,0,w,h)
        centerpoint = QDesktopWidget().screenGeometry().center()
        newpos = self.frameGeometry()
        newpos.moveCenter(centerpoint)
        self.move(newpos.topLeft())
        self.show()
        
#this is needed in case the file being copied is read-only
def fixreadonlyfile(func, path, exc_info):
    import stat
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)

def dobutton():
    print(os.getcwd())
    doit.gobutton.setStyleSheet("background-color: red")
    doit.gobutton.setText("Working...")
    doit.gobutton.repaint()
    
    try:
        dbpointer = sqlite3.connect('gitbackup.db')
        dbcursor = dbpointer.cursor()
        dbcursor.execute('''CREATE TABLE IF NOT EXISTS folders (folder text, location text)''')
        dbpointer.commit()
        dbpointer.close()
    except Exception as e:
        raise
    
    # make a copy of source directory with timestamp
    stamp = datetime.datetime.now()
    Y=stamp.strftime("%y")
    M=stamp.strftime("%b")
    D=stamp.strftime("%d")
    h=stamp.strftime("%I")
    m=stamp.strftime("%M")
    s=stamp.strftime("%S")
    src = "C:/Users/samad/Desktop/Python"
    newsrc = "C:/Users/samad/Desktop/Python"+Y+M+D+h+m+s
    try:
        shutil.copytree(src,newsrc)
    except Exception as e:
        raise
        
    git_url = "https://smadabob:Slickgit1@github.com/smadabob/python"
    repodir = "C:/Users/samad/Desktop/repodir2"
    if os.path.isdir(repodir):
        shutil.rmtree(repodir,onerror=fixreadonlyfile)
    myrepo = git.Repo.clone_from(git_url, repodir)
    shutil.move(newsrc,repodir)
    myrepo.git.add(A=True)
    myrepo.index.commit("commit - "+Y+M+D+h+m+s)
    myrepo.git.push() 
    doit.gobutton.setStyleSheet("background-color: green")
    doit.gobutton.setText("Done!")
    doit.gobutton.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    os.chdir(os.path.dirname(os.path.abspath(__file__))) #sets working directory to where the executable is
    doit = gitbackup()
    doit.gobutton.clicked.connect(dobutton)
    sys.exit(app.exec_())

