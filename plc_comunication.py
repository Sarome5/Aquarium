import plc_module
import time

ai1 = ("1032")
wv_monat = ("0")
wv_vormonat = ("4")
wv_jahr = ("8")
wv_gesamt = ("12")
I00_17 = ("1024")
Q00_17 = ("1064")
NQ00_17 = ("1390")



def scaling(adc, adc_l, adc_h, phys_l, phys_h):
    steigung = ((phys_l-phys_h)/(adc_l-adc_h))
    offset = phys_l-(steigung*adc_l)
    scaled_value = adc * steigung + offset
    return(int(scaled_value))

def communication():
    values={}
    values["input_byte"] = bin(int(plc_module.get_word(I00_17)))[2:-8].zfill(8)
    values["output_byte"] = bin(int(plc_module.get_word(Q00_17)))[2:-8].zfill(8)
    values["network_output_byte"] = bin(int(plc_module.get_word(NQ00_17)))[2:-8].zfill(8)
    values["AI1"] = plc_module.get_word(ai1)
    values["wv_monat"] = plc_module.get_doubleword(wv_monat)
    values["wv_monat2"] = plc_module.get_doubleword(wv_vormonat)
    values["wv_jahr"] = plc_module.get_doubleword(wv_jahr)
    values["wv_gesamt"] = plc_module.get_doubleword(wv_gesamt)
    return(values)

def connection_status():
    connection_status=plc_module.connection_status()
    return(connection_status)


def set_bool(adresse, value):
    plc_module.set_bool(adresse, value)
