# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Wed Oct 30 16:37:43 2019

@author: Anthony
"""

import tkinter as tk
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import threading
import queue
import time
import subprocess

E=tk.E
W=tk.W
N=tk.N
S=tk.S

delay = 1

home = os.path.expanduser('~')

class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.left_frame = tk.Frame(master, bg='black')
        self.left_frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.left_frame.grid_columnconfigure(1, weight=1)
        
        for row in range(0,19):
            self.left_frame.grid_rowconfigure(row,weight=1)
        
        self.frame = tk.Frame(master, bg='dodgerblue2')
        self.frame.grid(row=1, column=0, sticky=N+S+E+W)

        for col in range(0,9):
            self.frame.grid_columnconfigure(col,weight=1)

        self.grid()
        self.master.title('VIS: Visualizador de Imágenes Satelitales')
        self.createImage()

        self.CH1()
        self.CH2()
        self.CH3()
        self.CH4()
        self.CH5()
        self.CH6()
        self.CH7()
        self.CH8()
        self.CH9()
        self.CH10()
        self.CH11()
        self.CH12()
        self.CH13()
        self.CH14()
        self.CH15()
        self.CH16()
        self.AirMass()
        self.Save()

        self.createRadio()
        self.grid(sticky=N+S+E+W)



    #### Se crea la imagen de fondo negro al iniciar el programa ####

    def createImage(self):
        self.v0 = tk.IntVar()
        self.v0.set(1)
        self.img = None
        self.paises= {1:'Centroamerica', 2:'CostaRica', 3:'Nicaragua', 4:'Panama', 5:'Honduras', 6:'ElSalvador', 7:'Guatemala', 8: 'Belice',
                      9:'Caribe', 10:'Cuba', 11:'HaitiRepDom', 12:'Jamaica', 13:'PuertoRico', 14:'Bahamas', 15:'AntillasMenores',
                      16:'AntillasHolandesas'}
        self.canales={1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'11', 12:'12', 13:'13', 14:'14', 15:'15', 16:'16', 17:'Airmass'}

        tk.Label(self.frame, text='Visible (VIS)', font=('Arial', 10, "bold"), relief=tk.SUNKEN, background="black", foreground="white", height=2).grid(row=3, column=0, columnspan=2, padx=2, pady=(2,0), sticky=W+N+E+S)

        tk.Label(self.frame, text='Infrarrojo Cercano (nIR)', font=('Arial', 10, "bold"), relief=tk.SUNKEN, background="black", foreground="white", height=2).grid(row=3, column=2, columnspan=4, padx=2, pady=(2,0), sticky=W+N+E+S)

        tk.Label(self.frame, text='Vapor de Agua (WV)', font=('Arial', 10, "bold"), relief=tk.SUNKEN, background="black", foreground="white", height=2).grid(row=3, column=6, columnspan=3, padx=2, pady=(2,0), sticky=W+N+E+S)

        tk.Label(self.frame, text='Infrarrojo (IR)', font=('Arial', 10, "bold"), relief=tk.SUNKEN, background="black", foreground="white", height=2).grid(row=5, column=0, columnspan=7, padx=2, pady=(2,0), sticky=W+N+E+S)

        tk.Label(self.frame, text='RGB\'s', font=('Arial', 10, "bold"), relief=tk.SUNKEN, background="black", foreground="white", height=2).grid(row=5, column=7, padx=2, pady=(2,0), sticky=W+N+E+S)

        tk.Label(self.frame, text='Guardar', font=('Arial', 10, "bold"), relief=tk.SUNKEN, background="black", foreground="white", height=2).grid(row=5, column=8, padx=2, pady=(2,0), sticky=W+N+E+S)

    #### Se crean los diferentes botones para los 16 canales del GOES ####
    #### Canal 01
            
    def CH1(self):
        self.button = tk.Button(self.frame)
        self.button["text"] = "Canal 01: "u"0.47 \u03bcm"
        self.button["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[1])
        self.button.grid(row=4, column=0, padx=(2, 0), sticky=N+E+W+S)
    
    #### Canal 02
    
    def CH2(self):
        self.button2 = tk.Button(self.frame)
        self.button2["text"] = "Canal 02: "u"0.64 \u03bcm"
        self.button2["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[2])
        self.button2.grid(row=4, column=1, padx=(0, 2), sticky=W+E+N+S)
    
    #### Canal 03
    
    def CH3(self):
        self.button3 = tk.Button(self.frame)
        self.button3["text"] = "Canal 03: "u"0.86 \u03bcm"
        self.button3["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[3])
        self.button3.grid(row=4, column=2, padx=(2, 0), sticky=W+E+N+S)
        
    #### Canal 04
    
    def CH4(self):
        self.button4 = tk.Button(self.frame)
        self.button4["text"] = "Canal 04: "u"1.37 \u03bcm"
        self.button4["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[4])
        self.button4.grid(row=4, column=3, sticky=W+E+N+S)
        
    #### Canal 05
    
    def CH5(self):
        self.button5 = tk.Button(self.frame)
        self.button5["text"] = "Canal 05: "u"1.6 \u03bcm"
        self.button5["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[5])
        self.button5.grid(row=4, column=4, sticky=W+E+N+S)
        
    #### Canal 06
    
    def CH6(self):
        self.button6 = tk.Button(self.frame)
        self.button6["text"] = "Canal 06: "u"2.24 \u03bcm"
        self.button6["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[6])
        self.button6.grid(row=4, column=5, padx=(0, 2), sticky=W+E+N+S)
        
    #### Canal 07
    
    def CH7(self):
        self.button7 = tk.Button(self.frame)
        self.button7["text"] = "Canal 07: "u"3.9 \u03bcm"
        self.button7["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[7])
        self.button7.grid(row=6, column=0, padx=(2, 0), sticky=W+E+N+S)
        
    #### Canal 08
    
    def CH8(self):
        self.button8 = tk.Button(self.frame)
        self.button8["text"] = "Canal 08: "u"6.2 \u03bcm"
        self.button8["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[8])
        self.button8.grid(row=4, column=6, padx=(2, 0), sticky=W+E+N+S)
        
    #### Canal 09
    
    def CH9(self):
        self.button9 = tk.Button(self.frame)
        self.button9["text"] = "Canal 09: "u"6.9 \u03bcm"
        self.button9["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[9])
        self.button9.grid(row=4, column=7, sticky=W+E+N+S)
        
    #### Canal 10
    
    def CH10(self):
        self.button10 = tk.Button(self.frame)
        self.button10["text"] = "Canal 10: "u"7.3 \u03bcm"
        self.button10["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[10])
        self.button10.grid(row=4, column=8, padx=(0, 2), sticky=W+E+N+S)
        self.button10.wait_visibility()
        
    #### Canal 11
    
    def CH11(self):
        self.button11 = tk.Button(self.frame)
        self.button11["text"] = "Canal 11: "u"8.4 \u03bcm"
        self.button11["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[11])
        self.button11.grid(row=6, column=1, sticky=W+E+N+S)
        
    #### Canal 12
    
    def CH12(self):
        self.button12 = tk.Button(self.frame)
        self.button12["text"] = "Canal 12: "u"9.6 \u03bcm"
        self.button12["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[12])
        self.button12.grid(row=6, column=2, sticky=W+E+N+S)
        
    #### Canal 13
    
    def CH13(self):
        self.button13 = tk.Button(self.frame)
        self.button13["text"] = "Canal 13: "u"10.3 \u03bcm"
        self.button13["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[13])
        self.button13.grid(row=6, column=3, sticky=W+E+N+S)
        
    #### Canal 14
    
    def CH14(self):
        self.button14 = tk.Button(self.frame)
        self.button14["text"] = "Canal 14: "u"11.2 \u03bcm"
        self.button14["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[14])
        self.button14.grid(row=6, column=4, sticky=W+E+N+S)
        
    #### Canal 15
    
    def CH15(self):
        self.button15 = tk.Button(self.frame)
        self.button15["text"] = "Canal 15: "u"12.3 \u03bcm"
        self.button15["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[15])
        self.button15.grid(row=6, column=5, sticky=W+E+N+S)
        
    #### Canal 16
    
    def CH16(self):
        self.button16 = tk.Button(self.frame)
        self.button16["text"] = "Canal 16: "u"13.3 \u03bcm"
        self.button16["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[16])
        self.button16.grid(row=6, column=6, padx=(0,2), sticky=W+E+N+S)
    
    #### RGB's
    
    def AirMass(self):
        self.button17 = tk.Button(self.frame)
        self.button17["text"] = 'RGB Masas de Aire'
        self.button17["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[17])
        self.button17.grid(row=6, column=7, padx=2, sticky=W+E+N+S)

    #### Guardar
    
    def Save(self):
        self.button18 = tk.Button(self.frame)
        self.button18["text"] = 'Guardar Imagen'
        self.button18["command"] = lambda: self.saveimage(self.country, self.channel)
        self.button18.grid(row=6, column=8, padx=2, sticky=W+E+N+S)

    #### Se crean los diferentes botones para los diferentes paises ####
                
    def createRadio(self):
        tk.Label(self.left_frame, text='PAISES Y REGIONES', font=('Arial', 10, "bold"), relief=tk.SUNKEN, width=20, height=5, background="black", foreground="white").grid(row=0, column=0, padx=5, pady=5, ipadx=10, sticky=W+N+E+S)

        tk.Label(self.left_frame, text='Centroamérica', font=('Arial', 10, 'italic'), relief=tk.RAISED, width=20, height=2, background="dodgerblue2", foreground="white").grid(row=1, column=0, padx=0, pady=2, sticky=W+E+N+S)
   
        tk.Label(self.left_frame, text='Caribe', font=('Arial', 10, 'italic'), relief=tk.RAISED, width=20, height=2, background="dodgerblue2", foreground="white").grid(row=10, column=0, padx=0, pady=2, sticky=W+E+N+S)

        #### Centroamerica
        self.r1=tk.Radiobutton(self.left_frame)
        self.r1["text"] ="Centroamérica"
        self.r1["variable"] =self.v0 
        self.r1["value"]=1
        self.r1["bg"]='white'
        self.r1["width"] = 20
        self.r1["command"] = lambda: self.Image_Generation(self.paises[1], self.canales[1])
        self.r1.grid(row=3, column=0, padx=0, pady=0, sticky=N+S+E+W)
        
        #### Costa Rica
        self.r2=tk.Radiobutton(self.left_frame)
        self.r2["text"] ="Costa Rica"
        self.r2["variable"] =self.v0 
        self.r2["value"]=2
        self.r2["bg"]='white'
        self.r2["width"]=20
        self.r2["command"] = lambda: self.Image_Generation(self.paises[2], self.canales[1])
        self.r2.grid(row=4, column = 0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Nicaragua
        self.r3=tk.Radiobutton(self.left_frame)
        self.r3["text"] ="Nicaragua"
        self.r3["variable"] =self.v0 
        self.r3["value"]=3
        self.r3["bg"]='white'
        self.r3["width"]=20
        self.r3["command"] = lambda: self.Image_Generation(self.paises[3], self.canales[1])
        self.r3.grid(row=8, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Panama
        self.r4=tk.Radiobutton(self.left_frame)
        self.r4["text"] ="Panamá"
        self.r4["variable"] =self.v0 
        self.r4["value"]=4
        self.r4["bg"]='white'
        self.r4["width"]=20
        self.r4["command"] = lambda: self.Image_Generation(self.paises[4], self.canales[1])
        self.r4.grid(row=9, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Honduras
        self.r5=tk.Radiobutton(self.left_frame)
        self.r5["text"] ="Honduras"
        self.r5["variable"] =self.v0 
        self.r5["value"]=5
        self.r5["bg"]='white'
        self.r5["width"]=20
        self.r5["command"] = lambda: self.Image_Generation(self.paises[5], self.canales[1])
        self.r5.grid(row=7, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### El Salvador
        self.r6=tk.Radiobutton(self.left_frame)
        self.r6["text"] ="El Salvador"
        self.r6["variable"] =self.v0 
        self.r6["value"]=6
        self.r6["bg"]='white'
        self.r6["width"]=20
        self.r6["command"] = lambda: self.Image_Generation(self.paises[6], self.canales[1])
        self.r6.grid(row=5, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Guatemala
        self.r7=tk.Radiobutton(self.left_frame)
        self.r7["text"] ="Guatemala"
        self.r7["variable"] =self.v0 
        self.r7["value"]=7
        self.r7["bg"]='white'
        self.r7["width"]=20
        self.r7["command"] = lambda: self.Image_Generation(self.paises[7], self.canales[1])
        self.r7.grid(row=6, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Belice
        self.r8=tk.Radiobutton(self.left_frame)
        self.r8["text"] ="Belice"
        self.r8["variable"] =self.v0 
        self.r8["value"]=8
        self.r8["bg"]='white'
        self.r8["width"]=20
        self.r8["command"] = lambda: self.Image_Generation(self.paises[8], self.canales[1])
        self.r8.grid(row=2, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Caribe
        self.r9=tk.Radiobutton(self.left_frame)
        self.r9["text"] ="Caribe"
        self.r9["variable"] =self.v0 
        self.r9["value"]=9
        self.r9["bg"]='white'
        self.r9["width"]=20
        self.r9["command"] = lambda: self.Image_Generation(self.paises[9], self.canales[1])
        self.r9.grid(row=14, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Cuba
        self.r10=tk.Radiobutton(self.left_frame)
        self.r10["text"] ="Cuba"
        self.r10["variable"] =self.v0 
        self.r10["value"]=10
        self.r10["bg"]='white'
        self.r10["width"]=20
        self.r10["command"] = lambda: self.Image_Generation(self.paises[10], self.canales[1])
        self.r10.grid(row=15, column = 0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Haiti - Rep Dominicana
        self.r11=tk.Radiobutton(self.left_frame)
        self.r11["text"] ="Haití y Rep. Dominicana"
        self.r11["variable"] =self.v0 
        self.r11["value"]=11
        self.r11["bg"]='white'
        self.r11["width"]=20
        self.r11["command"] = lambda: self.Image_Generation(self.paises[11], self.canales[1])
        self.r11.grid(row=16, column=0,  padx=0, pady=0, sticky=W+N+S+E)
        
        #### Jamaica
        self.r12=tk.Radiobutton(self.left_frame)
        self.r12["text"] ="Jamaica"
        self.r12["variable"] =self.v0 
        self.r12["value"]=12
        self.r12["bg"]='white'
        self.r12["width"]=20
        self.r12["command"] = lambda: self.Image_Generation(self.paises[12], self.canales[1])
        self.r12.grid(row=17, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Puerto Rico
        self.r13=tk.Radiobutton(self.left_frame)
        self.r13["text"] ="Puerto Rico"
        self.r13["variable"] =self.v0 
        self.r13["value"]=13
        self.r13["bg"]='white'
        self.r13["width"]=20
        self.r13["command"] = lambda: self.Image_Generation(self.paises[13], self.canales[1])
        self.r13.grid(row=18, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Bahamas
        self.r14=tk.Radiobutton(self.left_frame)
        self.r14["text"] ="Bahamas"
        self.r14["variable"] =self.v0 
        self.r14["value"]=14
        self.r14["bg"]='white'
        self.r14["width"]=20
        self.r14["command"] = lambda: self.Image_Generation(self.paises[14], self.canales[1])
        self.r14.grid(row=13, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Antillas Menores
        self.r15=tk.Radiobutton(self.left_frame)
        self.r15["text"] ="Antillas Menores"
        self.r15["variable"] =self.v0 
        self.r15["value"]=15
        self.r15["bg"]='white'
        self.r15["width"]=20
        self.r15["command"] = lambda: self.Image_Generation(self.paises[15], self.canales[1])
        self.r15.grid(row=12, column=0, padx=0, pady=0, sticky=W+N+S+E)
        
        #### Antillas de Sotavento
        self.r16=tk.Radiobutton(self.left_frame)
        self.r16["text"] ="Antillas Holandesas"
        self.r16["variable"] =self.v0 
        self.r16["value"]=16
        self.r16["bg"]='white'
        self.r16["width"]=20
        self.r16["command"] = lambda: self.Image_Generation(self.paises[16], self.canales[1])
        self.r16.grid(row=11, column=0, padx=0, pady=0, sticky=W+N+S+E)
    
    #### Se crea una funcion para la generacion de las diferentes imagenes para los diferentes canales y paises ####
    def Image_Generation(self, pais, canal):
        #os.system(home+"/IDV_5.7/runIDV "+home+"/Desktop/Paises/"+pais+"/" +pais+"CH"+canal+".isl")
        subprocess.run(["runIDV",home+"\Desktop\VIS\Paises\\"+pais+"\\"+pais+"CH"+canal+".isl"], cwd="C:\Program Files\IDV_5.7\\", shell=True)
        self.img = Image.open(home+'\Desktop\VIS\Paises\\'+pais+'\Imagenes\\'+pais+'CH'+canal+'.png')
        self.img = self.img.resize((1020,607), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label=tk.Label(self.left_frame, image=self.img , bg='black').grid(row=0, column=1, rowspan=20, sticky=W+N+E+S)
        self.image = self.img

        self.button["command"]= lambda: self.Image_Generation(pais, self.canales[1])
        self.button2["command"]= lambda: self.Image_Generation(pais, self.canales[2])
        self.button3["command"]= lambda: self.Image_Generation(pais, self.canales[3])
        self.button4["command"]= lambda: self.Image_Generation(pais, self.canales[4])
        self.button5["command"]= lambda: self.Image_Generation(pais, self.canales[5])
        self.button6["command"]= lambda: self.Image_Generation(pais, self.canales[6])
        self.button7["command"]= lambda: self.Image_Generation(pais, self.canales[7])
        self.button8["command"]= lambda: self.Image_Generation(pais, self.canales[8])
        self.button9["command"]= lambda: self.Image_Generation(pais, self.canales[9])
        self.button10["command"]= lambda: self.Image_Generation(pais, self.canales[10])
        self.button11["command"]= lambda: self.Image_Generation(pais, self.canales[11])
        self.button12["command"]= lambda: self.Image_Generation(pais, self.canales[12])
        self.button13["command"]= lambda: self.Image_Generation(pais, self.canales[13])
        self.button14["command"]= lambda: self.Image_Generation(pais, self.canales[14])
        self.button15["command"]= lambda: self.Image_Generation(pais, self.canales[15])
        self.button16["command"]= lambda: self.Image_Generation(pais, self.canales[16])
        self.button17["command"]= lambda: self.Image_Generation(pais, self.canales[17])
        self.button18["command"]= lambda: self.saveimage(pais, canal)

        self.r1["command"] = lambda: self.Image_Generation(self.paises[1], canal)
        self.r2["command"] = lambda: self.Image_Generation(self.paises[2], canal)
        self.r3["command"] = lambda: self.Image_Generation(self.paises[3], canal)
        self.r4["command"] = lambda: self.Image_Generation(self.paises[4], canal)
        self.r5["command"] = lambda: self.Image_Generation(self.paises[5], canal)
        self.r6["command"] = lambda: self.Image_Generation(self.paises[6], canal)
        self.r7["command"] = lambda: self.Image_Generation(self.paises[7], canal)
        self.r8["command"] = lambda: self.Image_Generation(self.paises[8], canal)
        self.r9["command"] = lambda: self.Image_Generation(self.paises[9], canal)
        self.r10["command"] = lambda: self.Image_Generation(self.paises[10], canal)
        self.r11["command"] = lambda: self.Image_Generation(self.paises[11], canal)
        self.r12["command"] = lambda: self.Image_Generation(self.paises[12], canal)
        self.r13["command"] = lambda: self.Image_Generation(self.paises[13], canal)
        self.r14["command"] = lambda: self.Image_Generation(self.paises[14], canal)
        self.r15["command"] = lambda: self.Image_Generation(self.paises[15], canal)
        self.r16["command"] = lambda: self.Image_Generation(self.paises[16], canal)
        self.country = pais
        self.channel = canal
        self.queue = queue.Queue()
        ThreadedTask(self.queue).start()
        self.master.after(delay, self.process_queue)
    
    def saveimage(self, pais, canal):
        self.img2 = None
        self.img2 = Image.open(home+'\Desktop\VIS\Paises\\'+pais+'\Imagenes\\'+pais+'CH'+canal+'.png')
        self.filename = filedialog.asksaveasfile(mode='wb', initialdir="~", defaultextension=".png", filetypes=[("Png file","*.png"),("All files","*.*")])
        if not self.filename:
            return
        self.img2.save(self.filename)

    #### Se crea una funcion para que una vez presionado un boton, se corra automaticamente cada 10 min, hasta que se presione otro boton ####
    
    def process_queue(self):
        try:
            self.queue.get(0)
            self.Image_Generation(self.country, self.channel)
        except queue.Empty:
            self.master.after(delay,self.process_queue)

#### Se crea una clase para que las funciones se llamen automaticamente ####    
        
class ThreadedTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        root.update_idletasks()
        time.sleep(600)
        self.queue.put("Click another button")

root = tk.Tk()
root.geometry("1200x690")
root.minsize(1200,690)
root.config(bg='white')
ST = App(master=root)
ST.mainloop()
