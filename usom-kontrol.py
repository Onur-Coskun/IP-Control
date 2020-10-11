from tkinter import *
import  datetime
def kontrol_et():
    dosya=open("usom.txt","r")
    icerik=dosya.read()
    dosya.close()
    ip=entry1.get()
    bugun=datatime.datatime.now()
    if str(ip) in icerik:
        dosya=open("log.txt","a")
        yazi=str(ip)+ "zararli\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("ip zararli")
    else:
        dosya = open("log.txt", "a")
        yazi = str(ip) + "zararli degil\nTarih:" + str(bugun) + "\n"
        dosya.write(yazi)
        dosya.close()
        v.set("ip zararli degil")

top=Tk()
top.title("usom ıp kontrol")
B=Button(top,text="kontrol et",command=kontrol_et)
B.place(x=50,y=50)
B.pack()
label1=Label(top,text="Kontrol edilecek ipler adreslerini giriniz:")
label1.place(x=50,y=70)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=80)
entry1.pack()
v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.pack()
top.mainloop()