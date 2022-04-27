import plc_module
import time
import socket
import pickle


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 1234))

i1 = ("1024.0")
ai1 = ("1032")
wv_monat = ("0")
wv_vormonat = ("4")
wv_jahr = ("8")
wv_gesamt = ("12")


while True:
    t = time.time()
    values=[]

    values.append({"I1": plc_module.get_bool(i1)})
    values.append({"AI1": plc_module.get_word(ai1)})
    values.append({"wv_monat": plc_module.get_doubleword(wv_monat)})
    values.append({"wv_vormonat": plc_module.get_doubleword(wv_vormonat)})
    values.append({"wv_jahr": plc_module.get_doubleword(wv_jahr)})
    values.append({"wv_gesamt": plc_module.get_doubleword(wv_gesamt)})

    # for dict_items in values:
    #     for key, value in dict_items.items():
    #         print(key, value)
    data=pickle.dumps(values)

    conn.send(data)
    #bytes_of_values=bytearray(values)
    #print(bytes(values))
    #for key, value in dict_items.items():
    #    print(key, value)

    print(time.time() - t)


    time.sleep(2)
