import plc_module as plc

zähler = plc.get_doubleword("4")
print(zähler)
plc.set_doubleword("4", 200)
plc.set_doubleword("8", 200)
plc.set_doubleword("12", 200)
