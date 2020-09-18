import os, datetime, shutil, time, tkinter, git
from tkinter import *

#set up main window
base = Tk()
base.config(background="white")
base.title("VSCodePython Backup")
w=300
h=300
ws = base.winfo_screenwidth() # width of the screen
hs = base.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
base.geometry('%dx%d+%d+%d' % (w, h, x, y))

#global variables
src = ""
newsrc = ""
repodir = ""
myrepo = ""


#this is needed in case the file being copied is read-only
def fixreadonlyfile(func, path, exc_info):
    import stat
    print("repodir in fix = "+repodir)
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

#make a copy of the library and add a timestamp to the name
#repo the github
#move folder to repo, add, commit and push

def allsteps():
    
    progresstext.insert(END," Saving files...\n")
    stamp = datetime.datetime.now()
    Y=stamp.strftime("%y")
    M=stamp.strftime("%b")
    D=stamp.strftime("%d")
    h=stamp.strftime("%I")
    m=stamp.strftime("%M")
    s=stamp.strftime("%S")
    src = "C:/Users/samad/Desktop/Python"
    newsrc = "C:/Users/samad/Desktop/Python"+Y+M+D+h+m+s
    shutil.copytree(src,newsrc)

    git_url = "https://smadabob:Slickgit1@github.com/smadabob/python"
    progresstext.insert(END," Repo remote repository...\n")
    repodir = "C:/Users/samad/Desktop/repodir"
    if os.path.isdir(repodir):
        shutil.rmtree(repodir,onerror=fixreadonlyfile)
    myrepo = git.Repo.clone_from(git_url, repodir)

    progresstext.insert(END," Move, Add, Commit, Push...\n")
    shutil.move(newsrc,repodir)
    myrepo.git.add(A=True)
    myrepo.index.commit("commit - "+Y+M+D+h+m+s)
    myrepo.git.push()
    
    progresstext.insert(END," FINISHED!")
 
#time.sleep(1)
#base.wait_visibility()

progresstext=Text(base, bd=0, bg="old lace",height=13, width=30)
progresstext.pack()
empty1=Label(base)
empty1.pack()
gobutton=Button(base, text = "GO!", bg="green", command = allsteps)
gobutton.pack()

base.mainloop()