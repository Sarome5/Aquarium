import tkinter as tk
from tkinter import *
import plc_comunication as plc
import multiprocessing
import time

try:
    dict = plc.communication()
except Exception as e:
    print(type(e), e)

def show_frame(frame):
    frame.tkraise()

def comunication():
    t = time.time()
    try:
        dict = plc.communication()
    except Exception as e:
        print(type(e), e)

    try:

        I1=dict["I1"]
        I2=dict["I2"]
        I3=dict["I3"]
        I4=dict["I4"]
        I5=dict["I5"]
        I6=dict["I6"]
        Q1=dict["Q1"]
        Q2=dict["Q2"]
        Q3=dict["Q3"]
        Q4=dict["Q4"]
        Q5=dict["Q5"]
        NQ1=dict["NQ1"]
        NQ2=dict["NQ1"]
        NQ3=dict["NQ1"]
        var_AI1.set(dict["AI1"])
        var_wvjahr.set(dict["wv_jahr"] + " liter")
        var_wvgesamt.set(dict["wv_gesamt"] + " liter")


        if dict["NQ1"] == "1":
            var_wvmonat.set(dict["wv_monat"] + " liter")
            var_wvvormonat.set(dict["wv_monat2"] + " liter")

        else:
            var_wvmonat.set(dict["wv_monat2"] + " liter")
            var_wvvormonat.set(dict["wv_monat"] + " liter")

        if dict["I1"] == "1":
            signal_I1.itemconfig(oval_I1, fill="green")
        else:
            signal_I1.itemconfig(oval_I1, fill="red")

        if dict["I2"] == "1":
            signal_I2.itemconfig(oval_I2, fill="green")
        else:
            signal_I2.itemconfig(oval_I2, fill="red")

        if dict["I3"] == "1":
            signal_I3.itemconfig(oval_I3, fill="green")
        else:
            signal_I3.itemconfig(oval_I3, fill="red")

        if dict["I4"] == "1":
            signal_I4.itemconfig(oval_I4, fill="green")
        else:
            signal_I4.itemconfig(oval_I4, fill="red")

        if dict["I5"] == "1":
            signal_I5.itemconfig(oval_I5, fill="green")
        else:
            signal_I5.itemconfig(oval_I5, fill="red")

        if dict["I6"] == "1":
            signal_I6.itemconfig(oval_I6, fill="green")
        else:
            signal_I6.itemconfig(oval_I6, fill="red")

        if dict["Q1"] == "1":
            signal_Q1.itemconfig(oval_Q1, fill="green")
        else:
            signal_Q1.itemconfig(oval_Q1, fill="red")

        if dict["Q2"] == "1":
            signal_Q2.itemconfig(oval_Q2, fill="green")
        else:
            signal_Q2.itemconfig(oval_Q2, fill="red")

        if dict["Q3"] == "1":
            signal_Q3.itemconfig(oval_Q3, fill="green")
        else:
            signal_Q3.itemconfig(oval_Q3, fill="red")

        if dict["Q4"] == "1":
            signal_Q4.itemconfig(oval_Q4, fill="green")
        else:
            signal_Q4.itemconfig(oval_Q4, fill="red")

        if dict["Q5"] == "1":
            signal_Q5.itemconfig(oval_Q5, fill="green")
        else:
            signal_Q5.itemconfig(oval_Q5, fill="red")

        if dict["NQ2"] == "1":
            signal_NQ2.itemconfig(oval_NQ2, fill="green")
        else:
            signal_NQ2.itemconfig(oval_NQ2, fill="red")

        if dict["NQ3"] == "1":
            signal_NQ3.itemconfig(oval_NQ3, fill="green")
        else:
            signal_NQ3.itemconfig(oval_NQ3, fill="red")

        refreshrate = str((time.time() - t))[:5]
        var_aktualisierung.set(refreshrate)

    except Exception as e:
        print(type(e), e)
    #print(dict)
    window.after(1000, comunication)



def btn_wasserwechsel():
    plc.set_bool("1105.2", 1)
    plc.set_bool("1105.2", 0)

def btn_wasserwechsel_stop():
    plc.set_bool("1105.4", 1)
    plc.set_bool("1105.4", 0)

def btn_osmose():
    plc.set_bool("1105.1", 1)
    plc.set_bool("1105.1", 0)

def btn_osmose_stop():
    plc.set_bool("1105.3", 1)
    plc.set_bool("1105.3", 0)



window = tk.Tk()
window.title("Aquarium")
window.iconbitmap("fisch.ico")
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

I1=dict["I1"]
I2=dict["I2"]
I3=dict["I3"]
I4=dict["I4"]
I5=dict["I5"]
I6=dict["I6"]
Q1=dict["Q1"]
Q2=dict["Q2"]
Q3=dict["Q3"]
Q4=dict["Q4"]
Q5=dict["Q5"]
NQ1=dict["NQ1"]
NQ2=dict["NQ1"]
NQ3=dict["NQ1"]

var_AI1=StringVar()
var_wvmonat=StringVar()
var_wvvormonat=StringVar()
var_wvjahr=StringVar()
var_wvgesamt=StringVar()
var_aktualisierung = StringVar()


#============Frame 1 code



frame1_title= tk.Label(frame1,
                        text="Aquarium",
                        font="Times 22 bold")

frame1_title.place(relx=0.5, rely=0.05, anchor=CENTER)


#=====================Anzeige der Aktualwerte

frame1_label_AI1_name= tk.Label(frame1,
                        text="Wasserstand:",
                        font="Arial 16 bold")
frame1_label_AI1_name.place(relx=0, rely=0.15, anchor=W)

frame1_label_AI1= tk.Label(frame1,
                        textvariable=var_AI1,
                        font="Arial 16 bold")
frame1_label_AI1.place(relx=0.50, rely=0.15, anchor=CENTER)

frame1_label_akt_name= tk.Label(frame1,
                        text="Refreshrate:",
                        font="Arial 10")
frame1_label_akt_name.place(relx=0.92, rely=0.95, anchor=E)

frame1_label_akt= tk.Label(frame1,
                        textvariable=var_aktualisierung,
                        font="Arial 10")
frame1_label_akt.place(relx=0.95, rely=0.95, anchor=CENTER)


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

#==============Button für Wasserwechsel und Osmose

f1_btnww = tk.Button(frame1, text="Wasserwechsel START", command=btn_wasserwechsel)
f1_btnww.place(relx=0.10, rely=0.90, anchor=CENTER)

f1_btnwws = tk.Button(frame1, text="Wasserwechsel STOP", command=btn_wasserwechsel_stop)
f1_btnwws.place(relx=0.10, rely=0.75, anchor=CENTER)

f1_btno = tk.Button(frame1, text="Osmose START", command=btn_osmose)
f1_btno.place(relx=0.25, rely=0.90, anchor=CENTER)

f1_btnos = tk.Button(frame1, text="Osmose STOP", command=btn_osmose_stop)
f1_btnos.place(relx=0.25, rely=0.75, anchor=CENTER)

#============= Indikatoren für Ein/Ausgänge bzw Status Wasserwechsel/Osmose

#-----Signalüberwachung I1
signal_I1 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_I1.place(relx=0.6, rely=0.10)

oval_I1 = signal_I1.create_oval(5, 5, 20, 20)
frame1_label_ovalI1_name= tk.Label(frame1,
                        text="Schwimmer Osmose unten",
                        font="Arial 12")

frame1_label_ovalI1_name.place(relx=0.64, rely=0.13, anchor=W)

#-----Signalüberwachung I2
signal_I2 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_I2.place(relx=0.6, rely=0.16)

oval_I2 = signal_I2.create_oval(5, 5, 20, 20)
frame1_label_ovalI2_name= tk.Label(frame1,
                        text="Schwimmer Osmose oben",
                        font="Arial 12")

frame1_label_ovalI2_name.place(relx=0.64, rely=0.19, anchor=W)

#-----Signalüberwachung I3
signal_I3 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_I3.place(relx=0.6, rely=0.22)

oval_I3 = signal_I3.create_oval(5, 5, 20, 20)
frame1_label_ovalI3_name= tk.Label(frame1,
                        text="Wasserzähler",
                        font="Arial 12")

frame1_label_ovalI3_name.place(relx=0.64, rely=0.25, anchor=W)

#-----Signalüberwachung I4
signal_I4 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_I4.place(relx=0.6, rely=0.28)

oval_I4 = signal_I4.create_oval(5, 5, 20, 20)
frame1_label_ovalI4_name= tk.Label(frame1,
                        text="Schalter WW",
                        font="Arial 12")

frame1_label_ovalI4_name.place(relx=0.64, rely=0.31, anchor=W)

#-----Signalüberwachung I5
signal_I5 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_I5.place(relx=0.6, rely=0.34)

oval_I5 = signal_I5.create_oval(5, 5, 20, 20)
frame1_label_ovalI5_name= tk.Label(frame1,
                        text="Schalter Osmose",
                        font="Arial 12")

frame1_label_ovalI5_name.place(relx=0.64, rely=0.37, anchor=W)

#-----Signalüberwachung I6
signal_I6 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_I6.place(relx=0.6, rely=0.41)

oval_I6 = signal_I6.create_oval(5, 5, 20, 20)
frame1_label_ovalI6_name= tk.Label(frame1,
                        text="Notüberwachung",
                        font="Arial 12")

frame1_label_ovalI6_name.place(relx=0.64, rely=0.43, anchor=W)

#-----Signalüberwachung Q1
signal_Q1 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_Q1.place(relx=0.6, rely=0.50)

oval_Q1 = signal_Q1.create_oval(5, 5, 20, 20)
frame1_label_ovalQ1_name= tk.Label(frame1,
                        text="Magnetventil Wasser",
                        font="Arial 12")

frame1_label_ovalQ1_name.place(relx=0.64, rely=0.53, anchor=W)

#-----Signalüberwachung Q2
signal_Q2 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_Q2.place(relx=0.6, rely=0.56)

oval_Q2 = signal_Q2.create_oval(5, 5, 20, 20)
frame1_label_ovalQ2_name= tk.Label(frame1,
                        text="Magnetventil Osmose",
                        font="Arial 12")

frame1_label_ovalQ2_name.place(relx=0.64, rely=0.59, anchor=W)

#-----Signalüberwachung Q3
signal_Q3 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_Q3.place(relx=0.6, rely=0.62)

oval_Q3 = signal_Q3.create_oval(5, 5, 20, 20)
frame1_label_ovalQ3_name= tk.Label(frame1,
                        text="Pumpe Osmose => Becken",
                        font="Arial 12")

frame1_label_ovalQ3_name.place(relx=0.64, rely=0.65, anchor=W)

#-----Signalüberwachung Q4
signal_Q4 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_Q4.place(relx=0.6, rely=0.68)

oval_Q4 = signal_Q4.create_oval(5, 5, 20, 20)
frame1_label_ovalQ4_name= tk.Label(frame1,
                        text="Pumpe Abwasser",
                        font="Arial 12")

frame1_label_ovalQ4_name.place(relx=0.64, rely=0.71, anchor=W)

#-----Signalüberwachung Q5
signal_Q5 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_Q5.place(relx=0.6, rely=0.74)

oval_Q5 = signal_Q5.create_oval(5, 5, 20, 20)
frame1_label_ovalQ5_name= tk.Label(frame1,
                        text="Lampe",
                        font="Arial 12")

frame1_label_ovalQ5_name.place(relx=0.64, rely=0.77, anchor=W)


#------Überwachung Wasserwechsel aktiv

signal_NQ3 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_NQ3.place(relx=0.085, rely=0.79)

oval_NQ3 = signal_NQ3.create_oval(5, 5, 20, 20)


#------Überwachung Osmoseaufbereitung aktiv

signal_NQ2 = tk.Canvas(window, width=20, height=20)  # Create 200x200 Canvas widget
signal_NQ2.place(relx=0.234, rely=0.79)

oval_NQ2 = signal_NQ2.create_oval(5, 5, 20, 20)

#------------------


comunication()



window.mainloop()
