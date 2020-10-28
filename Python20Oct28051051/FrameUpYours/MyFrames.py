from tkinter import *

print("start of driver")



base = Tk()
screen_width = int(base.winfo_screenwidth())
screen_height = int(base.winfo_screenheight())
base.config(background="white")
base.state('zoomed')
base.title("Base Window - Your max resolution is (width x height): " + str(screen_width) + " x " + str(screen_height))
base.geometry(str(screen_width) + "x" + str(screen_height))
base.grid()
colnum=0
rownum=0
while (colnum < screen_width):
    base.grid_columnconfigure(colnum, weight=1)
    colnum = colnum+1
while (rownum < screen_height):
    base.grid_rowconfigure(rownum, weight=1)
    rownum = rownum+1


# #This will point out each pixel...
# colnum=0
# while (colnum < screen_width):
#     if (colnum % 2 == 0):
#         Label(base, bg="yellow", height=1, width=1).grid(row=5, column=colnum)
#     else:
#         Label(base, bg="green", height=1, width=1).grid(row=5, column=colnum)
#     colnum = colnum + 1
#
# rownum=0
# while (rownum < screen_height):
#     if (rownum % 2 == 0):
#         Label(base, bg="blue",height=1, width=1).grid(row=rownum, column=5)
#     else:
#         Label(base, bg="red",height=1, width=1).grid(row=rownum, column=5)
#     rownum = rownum + 1


# tellsize=Text(base, bg="white", bd=2,width=30)
# tellsize.tag_configure("bold", font="Bazooka 12 bold",justify=CENTER)
# tellsize.tag_configure("highlight", font="Bazooka 12 bold", background="yellow",justify=CENTER)
# tellsize.grid(row=20,column=40)
# tellsize.insert(END,"  This is the main window, defaulted to open at fullscreen, which is based on your resolution.\n","bold")
# tellsize.insert(END,"  Your resolution is set to ","bold")
# tellsize.insert(END,str(screen_width) + " x " + str(screen_height) +" ","highlight")
# tellsize.insert(END,"(width x height).","bold")

# #http://effbot.org/zone/tkinter-window-size.htm
# def myconfigure(event):
#     mycanvas.delete("all")
#     w = event.width
#     h = event.height
#     print(w)
#     print(h)
#
# mycanvas = Canvas(bd=3, relief=SOLID, bg="blue", height=100, width=100)
# mycanvas.grid()
# mycanvas.resizable(True, True)
# mycanvas.bind("<Configure>", myconfigure)

#
# winsize = Text(base, bg="white", bd=0)
# winsize.grid()
# winsize.insert(END, " This window:\n")
# winsize.insert(END, "   Width: wwww\n")
# winsize.insert(END, "   Height: hhhh")


testframe = Toplevel(bg="white", bd=1)
testframe.grid()
testframe.title("Test Frame")
testframe.lift(aboveThis=base)

mainsize=Text(testframe,bd=0)
mainsize.grid()
mainsize.insert(END," Your max resolution is: ")
mainsize.insert(END,str(screen_width) + " x " + str(screen_height))

def myconfigure(event):
    w = event.width
    h = event.height
    print(w)
    print(h)

testframe.bind("<Configure>", myconfigure)

base.mainloop()
