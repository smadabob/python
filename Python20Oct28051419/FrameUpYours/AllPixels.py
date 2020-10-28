from tkinter import *
#from tkinter.ttk import *

base = Tk()
screen_width = int(base.winfo_screenwidth())
screen_height = int(base.winfo_screenheight())
base.config(background="white")
base.state('zoomed')
base.geometry(str(screen_width) + "x" + str(screen_height))
base.grid()

c = Canvas(base, width=screen_width, height=screen_height, bg="grey85")
c.grid()

f = Toplevel(c, width=20, height=20, bg="blue")
f.grid()
f.lift(aboveThis=c)



# progress = Progressbar(base, orient=HORIZONTAL, length=100, mode='determinate')
# progress.grid()

# initialize each cell (pixel)
# colnum=0
# rownum=0
# while (colnum <= screen_width):
#     base.grid_columnconfigure(colnum, weight=1)
#     colnum = colnum+1
# while (rownum <= screen_height):
#     base.grid_rowconfigure(rownum, weight=1)
#     rownum = rownum+1

# # This will point out each pixelm, alternating colors...
# colnum=0
# while (colnum < screen_width):
#     if (colnum % 10 == 0):
#         Label(base, bg="yellow", height=1, width=1).grid(row=20, column=colnum)
#     else:
#         Label(base, bg="black", height=1, width=1).grid(row=20, column=colnum)
#     colnum = colnum + 1
# rownum=0
# while (rownum < screen_height):
#     if (rownum % 10 == 0):
#         Label(base, bg="yellow", height=1, width=1).grid(row=rownum, column=20)
#     else:
#         Label(base, bg="black", height=1, width=1).grid(row=rownum, column=20)
#     rownum = rownum + 1

# This will point out each pixel at x% increments
# count = 0
# fillcell = 0
# colnum = 0
# while (colnum < screen_width):
#     if (colnum == fillcell):
#         print("fillcol = " + str(fillcell))
#         Label(base, bg="black").grid(row=20, column=colnum)
#         Label(base, bg="black").grid(row=21, column=colnum)
#         Label(base, bg="black").grid(row=22, column=colnum)
#         Label(base, bg="black").grid(row=23, column=colnum)
#         Label(base, bg="black").grid(row=24, column=colnum)
#         fillcell = fillcell + int(screen_width*.05)
#         count = count + 1
#     else:
#         Label(base, bg="white").grid(row=20, column=colnum)
#     colnum = colnum + 1
# print("cols = " + str(count))
# rownum=0
# fillcell = 0
# count=0
# while (rownum < screen_height):
#     if (rownum == fillcell):
#         print("fillrow = " + str(fillcell))
#         Label(base, bg="black").grid(row=rownum, column=20)
#         Label(base, bg="black").grid(row=rownum, column=21)
#         Label(base, bg="black").grid(row=rownum, column=22)
#         Label(base, bg="black").grid(row=rownum, column=23)
#         Label(base, bg="black").grid(row=rownum, column=24)
#         fillcell = fillcell + int(screen_height * .05)
#         count = count + 1
#     else:
#         Label(base, bg="white").grid(row=rownum, column=20)
#     rownum = rownum + 1
# print("rows = " + str(count))

base.mainloop()