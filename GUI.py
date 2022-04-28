import tkinter as tk
from tkinter import *
import plc_comunication as plc
import multiprocessing
import time


list = plc.communication()

def show_frame(frame):
    frame.tkraise()

def comunication():
    global var_1
    list = plc.communication()
    var_I1.set(list["I1"])
    var_AI1.set(list["AI1"])
    var_wvmonat.set(list["wv_monat"] + " liter")
    var_wvvormonat.set(list["wv_vormonat"] + " liter")
    var_wvjahr.set(list["wv_jahr"] + " liter")
    var_wvgesamt.set(list["wv_gesamt"] + " liter")

    window.after(1000, comunication)




window = tk.Tk()
window.title("Aquarium")
window.geometry("800x400")
window.minsize(width=250, height=250)


#Frames
#___________
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0,sticky="nsew")
show_frame(frame1)

frame1.grid(row=0,column=0,sticky="nsew")


#=============init

var_I1=StringVar()
var_AI1=StringVar()
var_wvmonat=StringVar()
var_wvvormonat=StringVar()
var_wvjahr=StringVar()
var_wvgesamt=StringVar()


#============Frame 1 code



frame1_title= tk.Label(frame1,
                        text="Aktuelle Werte",
                        font="Times 22 bold")

frame1_title.place(relx=0.5, rely=0.05, anchor=CENTER)




frame1_label_AI1_name= tk.Label(frame1,
                        text="Wasserstand:",
                        font="Arial 16 bold")
frame1_label_AI1_name.place(relx=0, rely=0.15, anchor=W)

frame1_label_AI1= tk.Label(frame1,
                        textvariable=var_AI1,
                        font="Arial 16 bold")
frame1_label_AI1.place(relx=0.50, rely=0.15, anchor=CENTER)


#----------

frame1_label_wvm_name= tk.Label(frame1,
                        text="Wasserverbrauch Monat:",
                        font="Arial 16 bold")
frame1_label_wvm_name.place(relx=0, rely=0.25, anchor=W)

frame1_label_wvm= tk.Label(frame1,
                        textvariable=var_wvmonat,
                        font="Arial 16 bold")
frame1_label_wvm.place(relx=0.50, rely=0.25, anchor=CENTER)

#------------------


frame1_label_wvv_name= tk.Label(frame1,
                        text="Wasserverbrauch Vormonat:",
                        font="Arial 16 bold")
frame1_label_wvv_name.place(relx=0, rely=0.35, anchor=W)

frame1_label_wvv= tk.Label(frame1,
                        textvariable=var_wvvormonat,
                        font="Arial 16 bold")
frame1_label_wvv.place(relx=0.50, rely=0.35, anchor=CENTER)

#------------------

frame1_label_wvj_name= tk.Label(frame1,
                        text="Wasserverbrauch Jahr:",
                        font="Arial 16 bold")
frame1_label_wvj_name.place(relx=0, rely=0.45, anchor=W)

frame1_label_wvj= tk.Label(frame1,
                        textvariable=var_wvjahr,
                        font="Arial 16 bold")
frame1_label_wvj.place(relx=0.50, rely=0.45, anchor=CENTER)

#-----------------


frame1_label_wvg_name= tk.Label(frame1,
                        text="Wasserverbrauch Gesamt:",
                        font="Arial 16 bold")
frame1_label_wvg_name.place(relx=0, rely=0.55, anchor=W)

frame1_label_wvg= tk.Label(frame1,
                        textvariable=var_wvgesamt,
                        font="Arial 16 bold")
frame1_label_wvg.place(relx=0.50, rely=0.55, anchor=CENTER)

#----------------

'''
f1_btnf2 = tk.Button(frame1, text="frame2", command=lambda:show_frame(frame2))
f1_btnf2.grid(row=1, column=0, ipadx=50, ipady=50)


f1_btnf3 = tk.Button(frame1, text="frame3", command=lambda:show_frame(frame3))
f1_btnf3.grid(row=2, column=0, ipadx=50, ipady=50)
'''

#============Frame 2 code
frame2_title= tk.Label(frame2, text="This is frame2", bg="yellow")
frame2_title.grid(row=0, column=0)

f2_btnf1 = tk.Button(frame2, text="frame1", command=lambda:show_frame(frame1))
f2_btnf1.grid(row=1, column=0, ipadx=50, ipady=50)


f2_btnf3 = tk.Button(frame2, text="frame3", command=lambda:show_frame(frame3))
f2_btnf3.grid(row=2, column=0, ipadx=50, ipady=50)

#============Frame 3 code
frame1_title= tk.Label(frame3, text="This is frame3", bg="green")
frame1_title.grid(row=0, column=0)

f3_btnf1 = tk.Button(frame3, text="frame1", command=lambda:show_frame(frame1))
f3_btnf1.grid(row=1, column=0, ipadx=50, ipady=50)


f3_btnf2 = tk.Button(frame3, text="frame2", command=lambda:show_frame(frame2))
f3_btnf2.grid(row=2, column=0, ipadx=50, ipady=50)


comunication()



window.mainloop()
