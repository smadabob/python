import os, datetime, shutil, time, tkinter, git
import sqlite3
from tkinter import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#set up main window
base = Tk()
base.config(background="white")
base.title("VSCodePython Backup")
w=600
h=600
ws = base.winfo_screenwidth() # width of the screen
hs = base.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
base.geometry('%dx%d+%d+%d' % (w, h, x, y))


#this is needed in case the file being copied is read-only
def fixreadonlyfile(func, path, exc_info):
    import stat
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    
def allsteps():

#-------------------------------------------------------
# make a copy of source directory with timestamp
    try:
        dbpointer = sqlite3.connect('gitbackup.db')
        dbcursor = dbpointer.cursor()
        dbcursor.execute('''CREATE TABLE IF NOT EXISTS folders (folder text, location text)''')
        dbpointer.commit()
        dbpointer.close()
        sys.exit()
    except Exception as e:
        progresstext.insert(END,"exception = "+str(e))
        raise

#-------------------------------------------------------
# make a copy of source directory with timestamp
    #progresstext.insert(END," Saving files...\n")
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
        progresstext.insert(END,"exception = "+str(e))
        raise
#-------------------------------------------------------
    
    git_url = "https://smadabob:Slickgit1@github.com/smadabob/python"
    #progresstext.insert(END," Repo remote repository...\n")
    repodir = "C:/Users/samad/Desktop/repodir2"
    if os.path.isdir(repodir):
        shutil.rmtree(repodir,onerror=fixreadonlyfile)
    myrepo = git.Repo.clone_from(git_url, repodir)
    #progresstext.insert(END," Repo remote repository...\n")

    #progresstext.insert(END," Move, Add, Commit, Push...\n")
    shutil.move(newsrc,repodir)
    myrepo.git.add(A=True)
    myrepo.index.commit("commit - "+Y+M+D+h+m+s)
    myrepo.git.push()
    
    #progresstext.insert(END," FINISHED!")
 
#time.sleep(1)
#base.wait_visibility()


#progresstext=Text(base, bd=0, bg="old lace",height=13, width=30)
#progresstext.grid()
rows = 0
cols = 0
while rows < 20:
    base.grid_rowconfigure(rows, weight=1)
    rows = rows + 1
while cols < 20:
    base.grid_columnconfigure(cols, weight=1)
    cols = cols + 1
#empty1=Label(base)
#empty1.grid()
gobutton=Button(base, text = "GO!", bg="green", command = allsteps)
gobutton.grid(row=10, column=2, columnspan=7)

base.mainloop()