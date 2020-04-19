import git, os, datetime, shutil, time
from tkinter import *

base = Tk()
base.config(background="white",height=200,width=200)
base.title("VSCodePython Backup")
base.grid()
w = 300 # width for the Tk root
h = 350 # height for the Tk root
ws = base.winfo_screenwidth() # width of the screen
hs = base.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
base.geometry('%dx%d+%d+%d' % (w, h, x, y))

def fixreadfile(func, path, exc_info):
    import stat
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def driver(base):
        time.sleep(1)
        git_url = "https://smadabob:Slickgit1@github.com/smadabob/python"
        updatetext=Text(base,bd=0)
        updatetext.grid()
        #make a copy of VSCodePython with timestamp in name
        updatetext.insert(END," Saving files...\n")
        base.update()
        stamp = datetime.datetime.now()
        Y=stamp.strftime("%y")
        M=stamp.strftime("%b")
        D=stamp.strftime("%d")
        h=stamp.strftime("%I")
        m=stamp.strftime("%M")
        s=stamp.strftime("%S")
        src = "C:/My Apps/VSCodePython"
        newsrc = "C:/My Apps/python"+Y+M+D+h+m+s
        shutil.copytree(src,newsrc)
        #repo the github
        updatetext.insert(END," Repo remote repository...\n")
        base.update()
        repodir = "C:/My Apps/gitrepo"
        if os.path.isdir(repodir):
            shutil.rmtree(repodir,onerror=fixreadfile)
        myrepo = git.Repo.clone_from(git_url, repodir)
        #move folder to repo, add, commit and push
        updatetext.insert(END," Move, Add, Commit, Push...\n")
        base.update();
        shutil.move(newsrc,repodir)
        myrepo.git.add(A=True)
        myrepo.index.commit("commit - "+Y+M+D+h+m+s)
        myrepo.git.push()
        updatetext.insert(END," FINISHED!")
        base.update();

base.wait_visibility()
doit = driver(base)
base.mainloop()