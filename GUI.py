from pathlib import Path
from tkinter import *
import plc_comunication as plc
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def byte_to_bit_dict(byte):
    index = 1
    values={}
    for b in str(byte)[::-1]:
        values[index] = b
        index +=1
    return values

def update():
    t = time.time()
    adc_lowstate=853
    adc_highstate=686
    phys_lowstate=190
    phys_highstate=210
    try:
        input = plc.communication()

        values_input = byte_to_bit_dict(input["input_byte"])
        values_output = byte_to_bit_dict(input["output_byte"])
        values_nwoutput = byte_to_bit_dict(input["network_output_byte"])


        I1=values_input[1]
        I2=values_input[2]
        I3=values_input[3]
        I4=values_input[4]
        I5=values_input[5]
        I6=values_input[6]
        Q1=values_output[1]
        Q2=values_output[2]
        Q3=values_output[3]
        Q4=values_output[4]
        Q5=values_output[5]
        NQ1=values_nwoutput[1]
        NQ2=values_nwoutput[2]
        NQ3=values_nwoutput[3]

        wasserstand = str(plc.scaling(int(input["AI1"]), adc_lowstate, adc_highstate, phys_lowstate, phys_highstate))

        canvas.itemconfig(text_stand, text=wasserstand+ " mm")
        canvas.itemconfig(text_jahr, text=input["wv_jahr"] + " liter")
        canvas.itemconfig(text_gesamt, text=input["wv_gesamt"] + " liter")


        if NQ1 == "1":
            canvas.itemconfig(text_monat, text=input["wv_monat"] + " liter")
            canvas.itemconfig(text_vormonat, text=input["wv_monat2"] + " liter")
        else:
            canvas.itemconfig(text_monat, text=input["wv_monat2"] + " liter")
            canvas.itemconfig(text_vormonat, text=input["wv_monat"] + " liter")

        if I1 == "1":
            canvas.itemconfig(signal_I1, fill="green")
        else:
            canvas.itemconfig(signal_I1, fill="red")

        if I2 == "1":
            canvas.itemconfig(signal_I2, fill="green")
        else:
            canvas.itemconfig(signal_I2, fill="red")

        if I3 == "1":
            canvas.itemconfig(signal_I3, fill="green")
        else:
            canvas.itemconfig(signal_I3, fill="red")

        if I4 == "1":
            canvas.itemconfig(signal_I4, fill="green")
        else:
            canvas.itemconfig(signal_I4, fill="red")

        if I5 == "1":
            canvas.itemconfig(signal_I5, fill="green")
        else:
            canvas.itemconfig(signal_I5, fill="red")

        if I6 == "1":
            canvas.itemconfig(signal_I6, fill="green")
        else:
            canvas.itemconfig(signal_I6, fill="red")

        if Q1 == "1":
            canvas.itemconfig(signal_Q1, fill="green")
        else:
            canvas.itemconfig(signal_Q1, fill="red")


        if Q2 == "1":
            canvas.itemconfig(signal_Q2, fill="green")
        else:
            canvas.itemconfig(signal_Q2, fill="red")

        if Q3 == "1":
            canvas.itemconfig(signal_Q3, fill="green")
        else:
            canvas.itemconfig(signal_Q3, fill="red")

        if Q4 == "1":
            canvas.itemconfig(signal_Q4, fill="green")
        else:
            canvas.itemconfig(signal_Q4, fill="red")

        if Q5 == "1":
            canvas.itemconfig(signal_Q5, fill="green")
        else:
            canvas.itemconfig(signal_Q5, fill="red")

        if NQ2 == "1":
            canvas.itemconfig(signal_osmose, fill="green")
        else:
            canvas.itemconfig(signal_osmose, fill="red")

        if NQ3 == "1":
            canvas.itemconfig(signal_wasserwechsel, fill="green")
        else:
            canvas.itemconfig(signal_wasserwechsel, fill="red")

        refreshrate = str((time.time() - t))[:5]
        canvas.itemconfig(text_rate, text=refreshrate)

    except Exception as e:
        print("hier",type(e), e)

    #print(input)
    window.after(1000, update)

def connection_status():
    connected = plc.connection_status()
    if connected == 1:
        canvas.itemconfig(signal_conn, fill="green")
    else:
        canvas.itemconfig(signal_conn, fill="red")

    window.after(1000, connection_status)



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



window = Tk()

window.geometry("723x491")
window.configure(bg = "#C4D1F4")
window.iconbitmap(relative_to_assets("fisch.ico"))

def change_oval():
    canvas.itemconfig(text_gesamt, text="1234")

#--------Init

var_AI1=StringVar()
var_wvmonat=StringVar()
var_wvvormonat=StringVar()
var_wvjahr=StringVar()
var_wvgesamt=StringVar()
var_aktualisierung = StringVar()


#----------- create Elements


canvas = Canvas(
    window,
    bg = "#C4D1F4",
    height = 491,
    width = 723,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    280.0,
    23.999999999999943,
    anchor="nw",
    text="Aquarium",
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    14.0,
    87.99999999999994,
    anchor="nw",
    text="Wasserstand:",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

canvas.create_text(
    14.0,
    124.99999999999994,
    anchor="nw",
    text="Wasserverbrauch Monat:",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

canvas.create_text(
    14.0,
    161.99999999999994,
    anchor="nw",
    text="Wasserverbrauch Vormonat:",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

canvas.create_text(
    14.0,
    235.99999999999994,
    anchor="nw",
    text="Wasserverbrauch Gesamt:",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

canvas.create_text(
    14.0,
    198.99999999999994,
    anchor="nw",
    text="Wasserverbrauch Jahr:",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

#===== Input Signale
signal_I1 = canvas.create_oval(
    464.0,
    84.99999999999994,
    479.0,
    99.99999999999994,
    fill="#C4C4C4")

signal_I2 = canvas.create_oval(
    464.0,
    111.99999999999994,
    479.0,
    126.99999999999994,
    fill="#C4C4C4")

signal_I3 = canvas.create_oval(
    464.0,
    138.99999999999994,
    479.0,
    153.99999999999994,
    fill="#C4C4C4")

signal_I4 = canvas.create_oval(
    464.0,
    165.99999999999994,
    479.0,
    180.99999999999994,
    fill="#C4C4C4")

signal_I5 = canvas.create_oval(
    464.0,
    192.99999999999994,
    479.0,
    207.99999999999994,
    fill="#C4C4C4")

signal_I6 = canvas.create_oval(
    464.0,
    219.99999999999994,
    479.0,
    234.99999999999994,
    fill="#C4C4C4")

#======Output signale

signal_Q1 = canvas.create_oval(
    464.0,
    261.99999999999994,
    479.0,
    276.99999999999994,
    fill="#C4C4C4")

signal_Q2 = canvas.create_oval(
    464.0,
    288.99999999999994,
    479.0,
    303.99999999999994,
    fill="#C4C4C4",)

signal_Q3 = canvas.create_oval(
    464.0,
    315.99999999999994,
    479.0,
    330.99999999999994,
    fill="#C4C4C4")

signal_Q4 = canvas.create_oval(
    464.0,
    342.99999999999994,
    479.0,
    357.99999999999994,
    fill="#C4C4C4",)

signal_Q5 = canvas.create_oval(
    464.0,
    369.99999999999994,
    479.0,
    384.99999999999994,
    fill="#C4C4C4")
 #========Signale divers
signal_osmose = canvas.create_oval(
    177.0,
    424.99999999999994,
    192.0,
    439.99999999999994,
    fill="#C4C4C4")

signal_wasserwechsel = canvas.create_oval(
    71.0,
    424.99999999999994,
    86.0,
    439.99999999999994,
    fill="#C4C4C4")

signal_conn = canvas.create_oval(
    699.0,
    465.99999999999994,
    714.0,
    480.99999999999994,
    fill="#C4C4C4")

text_stand = canvas.create_text(
    260.0,
    89.99999999999994,
    anchor="nw",
    text="0",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

text_gesamt = canvas.create_text(
    260.0,
    238.99999999999994,
    anchor="nw",
    text="0 Liter",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

text_jahr = canvas.create_text(
    260.0,
    199.99999999999994,
    anchor="nw",
    text="0 Liter",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

text_vormonat = canvas.create_text(
    260.0,
    162.99999999999994,
    anchor="nw",
    text="0 Liter",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

text_monat = canvas.create_text(
    260.0,
    125.99999999999994,
    anchor="nw",
    text="0 Liter",
    fill="#000000",
    font=("Inter Bold", 18 * -1)
)

canvas.create_text(
    35,
    368.99999999999994,
    anchor="nw",
    text="Wasserwechsel",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    132.0,
    368.99999999999994,
    anchor="nw",
    text="Osmoseaufbereitung",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    494.0,
    83.99999999999994,
    anchor="nw",
    text="Schwimmer Osmose Unten",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    218.99999999999994,
    anchor="nw",
    text="Notueberwachung",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    191.99999999999994,
    anchor="nw",
    text="Schalter Osmose",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    164.99999999999994,
    anchor="nw",
    text="Schalter Wasserwechsel",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    137.99999999999994,
    anchor="nw",
    text="Wasserzaehler",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    110.99999999999994,
    anchor="nw",
    text="Schwimmer Osmose Oben",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    260.99999999999994,
    anchor="nw",
    text="Magnetventil Wasser",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    368.99999999999994,
    anchor="nw",
    text="Lampe",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    341.99999999999994,
    anchor="nw",
    text="Pumpe Abwasser",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    314.99999999999994,
    anchor="nw",
    text="Pumpe Osmose => Becken",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    494.0,
    287.99999999999994,
    anchor="nw",
    text="Magnetventil Osmose",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

text_rate = canvas.create_text(
    661.0,
    466.99999999999994,
    anchor="nw",
    text="0.000",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    592.0,
    466.99999999999994,
    anchor="nw",
    text="Refreshrate:",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_osmose,
    relief="flat"
)
button_1.place(
    x=140.0,
    y=390.99999999999994,
    width=88.0,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_wasserwechsel,
    relief="flat"
)
button_2.place(
    x=34.0,
    y=390.99999999999994,
    width=88.0,
    height=28.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=btn_osmose_stop,
    relief="flat"
)
button_3.place(
    x=140.0,
    y=444.99999999999994,
    width=88.0,
    height=28.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=btn_wasserwechsel_stop,
    relief="flat"
)
button_4.place(
    x=34.0,
    y=444.99999999999994,
    width=88.0,
    height=28.0
)
window.resizable(False, False)
update()
connection_status()
window.mainloop()
