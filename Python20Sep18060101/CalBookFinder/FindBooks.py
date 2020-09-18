import subprocess
import sqlite3
import datetime
import json
from tkinter import *

#https://www.mobileread.com/forums/showthread.php?t=262132
print("start of driver")

dbpointer = sqlite3.connect('calibrebooks.db')
dbcursor = dbpointer.cursor()
dbcursor.execute('''CREATE TABLE IF NOT EXISTS books (title text, authors text)''')
dbcursor.execute('''CREATE TABLE IF NOT EXISTS urls (title text, authors text)''')

##################
mainwindow = Tk()
mainwindow.minsize(width=600, height=400)
#mainwindow.resizable(width="false",height="false")
mainwindow.configure(background='#EBDAEF')
mainwindow.title("Calibre Book Search")

view_manual = Button(mainwindow, text="View Manual",borderwidth=5,relief=RIDGE)
add_url = Button(mainwindow, text="Add URL",borderwidth=5,relief=RIDGE)
add_url_list = Button(mainwindow, text="Add List of URLs",borderwidth=5,relief=RIDGE)
remove_url = Button(mainwindow, text="Remove URL",borderwidth=5,relief=RIDGE)
refresh_db = Button(mainwindow, text="Full DB Refresh",borderwidth=5,relief=RIDGE)
search_ip = Button(mainwindow, text="Search for IP",borderwidth=5,relief=RIDGE)
list_urls = Button(mainwindow, text="List URLs",borderwidth=5,relief=RIDGE)
configure = Button(mainwindow, text="Configure",borderwidth=5,relief=RIDGE)

view_manual.place(height=50, width=100,relx=.05, rely=.05)
configure.place(height=50, width=100,relx=.25, rely=.05)
add_url.place(height=50, width=100,relx=.05, rely=.40)
add_url_list.place(height=50, width=100,relx=.25, rely=.40)
remove_url.place(height=50, width=100,relx=.45, rely=.40)
refresh_db.place(height=50, width=100,relx=.05, rely=.60)
search_ip.place(height=50, width=100,relx=.25, rely=.60)
list_urls.place(height=50, width=100,relx=.45, rely=.60)



mainwindow.mainloop()
justatest = 7

###########################

#removeurl
#createdb
#maingui
#addurl
#searchip
#listallurls
#configure
#manual
#addurllist


def createdb():
    print("start of createdb")
# print(datetime.datetime.now())
# results = subprocess.run('C:\Program Files (x86)\Calibre2\calibredb list --for-machine --with-library http://92.108.65.53:8080',stdout=subprocess.PIPE,timeout=10)
# badresults = subprocess.run('C:\Program Files (x86)\Calibre2\calibredb list --for-machine --with-library http://69.47.181.212:8080',stdout=subprocess.PIPE)
# print(datetime.datetime.now())
# testjson = json.loads(results.stdout.decode())
# print(len(testjson))
# print(datetime.datetime.now())
#
# for item in testjson:
#     print(item['title'])
#     print(item['authors'])
#     dbtitle = item['title']
#     dbauthors = item['authors']
#     dbcursor.execute("INSERT INTO books(title, authors) VALUES ('%s', '%s')" % (dbtitle, dbauthors))
#     dbpointer.commit()
#
# dbpointer.close()


def readdb():
    print("start of readdb")
# dbpointer = sqlite3.connect('calibrebooks.db')
# dbcursor = dbpointer.cursor()
# dbcursor.execute("SELECT * from books")
# rows = dbcursor.fetchall()
# print(datetime.datetime.now())
# for row in rows:
#     print(row)
    print("done with readdb")

def cleardb():
    print("start of cleardb")
# dbpointer = sqlite3.connect('calibrebooks.db')
# dbcursor = dbpointer.cursor()
# dbcursor.execute("DELETE from books")
# dbpointer.commit()
# dbpointer.close()
    print("done with cleardb")