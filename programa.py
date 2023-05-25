from tkinter import *

# Variable

base = 480
altura = 480

# Ventana principal

ventana_Principal = Tk()
ventana_Principal.title("Gráficas 2d")
ventana_Principal.resizable(False, False)
ventana_Principal.geometry("520x520")
ventana_Principal.config(bg="black")
# Creación canvas

c= Canvas(ventana_Principal, width=base, height=altura)
c.config(bg="white")
c.place(x=20,y=20)

arribajaja =  c.create_polygon(base/2,0,base-20,0,base-20,altura-460,base/2,altura-460   ,fill="gray39")
abajodearribajaja = c.create_polygon(base/2-20,altura-460,base-10,altura-460,base-10,altura-430,base/2-20,altura-430,fill="gray39")
rectangulomasomenos  =  c.create_polygon(base/2,altura-430,base-30,altura-430,base-30,altura/2-10,base/2,altura/2-10, fill="gray50")
rectangulodentroderectangulo = c.create_polygon(base/2+20,altura-410,base-50,altura-410,base-50,altura/2-30,base/2+20,altura/2-30,fill="gray80")
caradentroderectangulo = c.create_oval(base/2+30,altura-420,base-60,altura/2-20,fill="OliveDrab1")
bocadecara = c.create_oval(325,165,365,200,fill="firebrick3",outline="firebrick3")
ojo1 = c.create_oval(360,100,395,130,fill="white",outline="OliveDrab1")
ojo2 = c.create_oval(300,100,335,130,fill="white",outline="OliveDrab1")
iris1 = c.create_oval(310,108,325,120,fill="SteelBlue1", outline="white")
iris2 = c.create_oval(370,108,385,120,fill="SteelBlue1", outline="white")
enojado1 = c.create_line(355,105,375,90, width=3)
enojado2 = c.create_line(340,105,320,90, width=3)
nosecirculo = c.create_oval(base/4-90,altura/2,base/4,altura-65,fill="gray39",outline="gray50")
rectangulogrande = c.create_polygon(base/2,altura/2-10,base-10,altura/2-10,base-10,altura-50,base/4,altura-50,base/4,altura/2-10,fill="gray86")
rectangulonosé = c.create_polygon(base/4,altura/2+10,base/4,altura-65,base/4-15,altura-65,base/4-15,altura-40,base/4-60,altura-40,base/4-60,altura/2-20,base/4-60,altura/2-20,base/4-15,altura/2-20,base/4-15,altura/2+10,fill="gray50")
chuchu = c.create_polygon(base/4+15,altura/2-10,base/4+70,altura/2-10,base/4+70,altura/2-60,base/4+90,altura/2-60,base/4+90,altura/2-110,base/4-5,altura/2-110,base/4-5,altura/2-60,base/4+15,altura/2-60,fill="gray50")
rueda1 = c.create_oval(base-110,altura-120,base-5,altura-15,fill="gray39",outline="gray39")
rueda2 = c.create_oval(base-230,altura-120,base-125,altura-15,fill="gray39",outline="gray39")
rueda3 = c.create_oval(base-350,altura-120,base-245,altura-15,fill="gray39",outline="gray39")
coso1 = c.create_rectangle(base-150,400,395,430,fill="black")
coso2 = c.create_rectangle(base-270,400,275,430,fill="black")
hola = c.create_text(base/2+50,altura/2+50,text="Andrés García", anchor="center",font=("Arial", 20 ,"bold"), fill="black",activefill="blue")

# Frame de contro

ventana_Principal.mainloop()