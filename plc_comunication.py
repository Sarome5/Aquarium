import plc_module
import time



i1 = ("1024.0")
i2 = ("1024.1")
i3 = ("1024.2")
i4 = ("1024.3")
i5 = ("1024.4")
i6 = ("1024.5")
q1 = ("1064.0")
q2 = ("1064.1")
q3 = ("1064.2")
q4 = ("1064.3")
q5 = ("1064.4")
nq1 = ("1390.0")
nq2 = ("1390.2")
nq3 = ("1390.3")
ai1 = ("1032")
wv_monat = ("0")
wv_vormonat = ("4")
wv_jahr = ("8")
wv_gesamt = ("12")

def communication():
    t = time.time()
    values={}

    values["I1"] = plc_module.get_bool(i1)
    values["I2"] = plc_module.get_bool(i2)
    values["I3"] = plc_module.get_bool(i3)
    values["I4"] = plc_module.get_bool(i4)
    values["I5"] = plc_module.get_bool(i5)
    values["I6"] = plc_module.get_bool(i6)
    values["Q1"] = plc_module.get_bool(q1)
    values["Q2"] = plc_module.get_bool(q2)
    values["Q3"] = plc_module.get_bool(q3)
    values["Q4"] = plc_module.get_bool(q4)
    values["Q5"] = plc_module.get_bool(q5)
    values["NQ1"] = plc_module.get_bool(nq1)
    values["NQ2"] = plc_module.get_bool(nq2)
    values["NQ3"] = plc_module.get_bool(nq3)
    values["AI1"] = plc_module.get_word(ai1)
    values["wv_monat"] = plc_module.get_doubleword(wv_monat)
    values["wv_monat2"] = plc_module.get_doubleword(wv_vormonat)
    values["wv_jahr"] = plc_module.get_doubleword(wv_jahr)
    values["wv_gesamt"] = plc_module.get_doubleword(wv_gesamt)

    return(values)
    print(time.time() - t)

def set_bool(adresse, value):
    plc_module.set_bool(adresse, value)
