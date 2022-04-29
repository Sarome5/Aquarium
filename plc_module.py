import snap7

Logo_7 = False

plc = snap7.logo.Logo()
plc.connect("10.0.0.201", 0x0200, 0x0300)

def get_bool(adresse):
    a = (f"V{adresse}")
    return(str(plc.read(a)))

def get_word(adresse):
    a = (f"VW{adresse}")
    return(str(plc.read(a)))

def get_doubleword(adresse):
    a = (f"VD{adresse}")
    return(str(plc.read(a)))

def set_bool(adresse, value):
    a = (f"V{adresse}")
    plc.write(a, value)


'''if plc.get_connected():
    I1 = ("1024.0")
    print(f"I1 = {get_bool(I1)}")
    AI1 = ("1032")
    print(f"AI1 = {get_word(AI1)}")
    Counter1 = ("0")
    print(f"C1 = {get_doubleword(Counter1)}")
'''
plc.disconnect
plc.destroy
