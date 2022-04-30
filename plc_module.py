import snap7
import time

Logo_7 = False

def connect(plc, ip):
    while True:
        if plc.get_connected():
            break
        try:
            #attempt connection
            plc.connect(ip, 0x0200, 0x0300)
        except:
            pass
        time.sleep(2)

plc = snap7.logo.Logo()
connect(plc,"10.0.0.201")

def get_bool(adresse):
    try:
        a = (f"V{adresse}")
        return(str(plc.read(a)))
    except Exception as e:
        connect(plc,"10.0.0.201")

def get_word(adresse):
    try:
        a = (f"VW{adresse}")
        return(str(plc.read(a)))
    except Exception as e:
        connect(plc,"10.0.0.201")

def get_doubleword(adresse):
    try:
        a = (f"VD{adresse}")
        return(str(plc.read(a)))
    except Exception as e:
        connect(plc,"10.0.0.201")

def set_bool(adresse, value):
    try:
        a = (f"V{adresse}")
        plc.write(a, value)
    except Exception as e:
        connect(plc,"10.0.0.201")

def set_doubleword(adresse, value):
    try:
        a = (f"VD{adresse}")
        plc.write(a, value)
    except Exception as e:
        connect(plc,"10.0.0.201")

def connection_status():
    if plc.get_connected():
        return(1)
    else:
        return(0)



plc.disconnect
plc.destroy
