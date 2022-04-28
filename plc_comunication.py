import plc_module
import time
import pickle


i1 = ("1024.0")
ai1 = ("1032")
wv_monat = ("0")
wv_vormonat = ("4")
wv_jahr = ("8")
wv_gesamt = ("12")

def communication():
    while True:
        t = time.time()
        values={}

        values["I1"] = plc_module.get_bool(i1)
        values["AI1"] = plc_module.get_word(ai1)
        values["wv_monat"] = plc_module.get_doubleword(wv_monat)
        values["wv_vormonat"] = plc_module.get_doubleword(wv_vormonat)
        values["wv_jahr"] = plc_module.get_doubleword(wv_jahr)
        values["wv_gesamt"] = plc_module.get_doubleword(wv_gesamt)

        return(values)
        print(time.time() - t)
