from tkinter import *

import tkinter.filedialog


root = Tk()
root.title("Larry")
root.geometry("600x400")

def getVideo():
    videoName = tkinter.filedialog.askopenfilename()#返回文件名
    print(videoName)
    return videoName

def cut():
	print(sTime)

def merge():
	pass

frame1 = Frame(root)
frame1.pack(pady = 20)
l1 = Label(frame1, text = "视频编辑器", bg = 'red', font = "50")
l1.pack()

frame2 = Frame(root)
frame2.pack(pady = 20)
l2 = Label(frame2, text = "视频文件 :", font ="20")
l2.pack(side = LEFT, fill = X, pady = 10)
e1 = Entry(frame2, bg = 'gray', font ="20")
e1.pack(side = LEFT)
b1 = Button(frame2, text = '选择视频文件', command = getVideo)
b1.pack(side = LEFT)


frame3 = Frame(root)
frame3.pack(pady = 20)
l3 = Label(frame3, text = '视频片段: From')
l3.pack(side = LEFT)
e2 = Entry(frame3, bg = 'gray', font ="20")
e2.pack(side = LEFT)
sTime = e2.get()
l4 = Label(frame3, text = 'To')
l4.pack(side = LEFT)
e3 = Entry(frame3, bg = 'gray', font ="20")
e3.pack(side = LEFT)

frame4 = Frame(root)
frame4.pack(pady = 20)
b2 = Button(frame4, text = '提取视频片段', command = cut)
b2.pack()

frame5 = Frame(root)
frame5.pack(pady = 20)
b3 = Button(frame5, text = '合并视频片段', command = merge)
b3.pack()

root.mainloop()
                       






                             