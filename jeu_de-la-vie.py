#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from tkinter import *

def finir(): #ferme la fenetre et enregistre les saisie dans les variables
    global nlignes,ncol,taille
    global Entreel,Entreec,Entreet,fen1
    nlignes = int(Entreel.get())
    ncol =int(Entreec.get())
    taille =int(Entreet.get())
    fen1.destroy()

def debut(): #ouvre la premiere fenetre
    global Entreel,Entreec,Entreet,fen1
    fen1=Tk()
    tex1=Label(fen1, text='nombre de lignes')
    tex1.pack()
    tex1.grid(row =0,column = 0)
    
    tex2=Label(fen1,text='nombre de collones')
    tex2.pack()
    tex2.grid(row=1,column = 0)
    
    tex3=Label(fen1,text="taille d'une cellule")
    tex3.pack()
    tex3.grid(row=2,column = 0)
    
    bou1=Button(fen1, text='OK', command=finir)
    bou1.pack()
    bou1.grid(row =3, column=3)
    
    entrl =StringVar()
    Entreel = Entry(fen1, textvariable=entrl, width = 7, justify = 'center')
    Entreel.pack()
    Entreel.grid(row=0,column=1) 
    entrl.set("100")
    
    entrc =StringVar()
    Entreec = Entry(fen1, textvariable=entrc, width = 7, justify = 'center')
    Entreec.pack()
    Entreec.grid(row=1,column=1) 
    entrc.set("100")
    
    entrt=StringVar()
    Entreet = Entry(fen1, textvariable=entrt,  width = 7, justify = 'center')
    Entreet.pack()
    Entreet.grid(row=2,column=1) 
    entrt.set("5")
    
    fen1.mainloop()

class Tableau(object): #classe permetant de creer les tables
    def __init__(self,nr,nc) :#constructeur
        self.nr=nr
        self.nc=nc
        self.table=[[" " for i in range(nc)] for j in range(nr)]
    def remplir(self,rang,col) : #permet de creer un point dans le tableau ne genere pas d'erreur si en dehors tu tableau
        if rang < self.nr and col < self.nc :
            self.table[rang][col]="#"            
    def nombre_de_voisins(self,rang,col) : #renvoi le nombre de voisins d'une cellule
        v=0
        if rang >= self.nr or col >= self.nc:
            return 0
        if rang != self.nr-1 and col != self.nc-1 and rang !=0 and col != 0 : #cas general pas au bord
            if self.table[rang][col-1]=="#" :
                v+=1
            if self.table[rang][col+1]=="#" :
                v+=1
            if self.table[rang-1][col]=="#" :
                v+=1
            if self.table[rang+1][col]=="#" :
                v+=1
            if self.table[rang+1][col+1]=="#" :
                v+=1
            if self.table[rang-1][col+1]=="#" :
                v+=1
            if self.table[rang+1][col-1]=="#" :
                v+=1
            if self.table[rang-1][col-1]=="#" :
                v+=1
        elif col != self.nc-1 and rang ==0 and col != 0 : #si dans le bord superieur
            if self.table[rang][col-1]=="#" :
                v+=1
            if self.table[rang][col+1]=="#" :
                v+=1
            if self.table[rang+1][col]=="#" :
                v+=1
            if self.table[rang+1][col+1]=="#" :
                v+=1
            if self.table[rang+1][col-1]=="#" :
                v+=1
        elif rang != self.nr-1 and rang !=0 and col == 0 : # si dans le bord de gauche
            if self.table[rang][col+1]=="#" :
                v+=1
            if self.table[rang-1][col]=="#" :
                v+=1
            if self.table[rang+1][col]=="#" :
                v+=1
            if self.table[rang+1][col+1]=="#" :
                v+=1
            if self.table[rang-1][col+1]=="#" :
                v+=1
        elif rang == self.nr-1 and col != self.nc-1  and col != 0 : #si derniere ligne
            if self.table[rang][col-1]=="#" :
                v+=1
            if self.table[rang][col+1]=="#" :
                v+=1
            if self.table[rang-1][col]=="#" :
                v+=1
            if self.table[rang-1][col+1]=="#" :
                v+=1
            if self.table[rang-1][col-1]=="#" :
                v+=1
        elif rang != self.nr-1 and col == self.nc-1 and rang !=0: #si derniere collone
            if self.table[rang][col-1]=="#" :
                v+=1
            if self.table[rang-1][col]=="#" :
                v+=1
            if self.table[rang+1][col]=="#" :
                v+=1
            if self.table[rang+1][col-1]=="#" :
                v+=1
            if self.table[rang-1][col-1]=="#" :
                v+=1
        elif  rang ==0 and col == 0 : # coin haut gauche
            if self.table[rang][col+1]=="#" :
                v+=1
            if self.table[rang+1][col]=="#" :
                v+=1
            if self.table[rang+1][col+1]=="#" :
                v+=1
        elif col == self.nc-1 and rang ==0 : #coin haut droit
            if self.table[rang][col-1]=="#" :
                v+=1
            if self.table[rang+1][col]=="#" :
                v+=1
            if self.table[rang+1][col-1]=="#" :
                v+=1
        elif rang == self.nr-1  and col == 0 : #coin bas gauche
            if self.table[rang][col+1]=="#" :
                v+=1
            if self.table[rang-1][col]=="#" :
                v+=1
            if self.table[rang-1][col+1]=="#" :
                v+=1
        elif rang == self.nr-1 and col == self.nc-1 : #coin bas droite
            if self.table[rang][col-1]=="#" :
                v+=1
            if self.table[rang-1][col]=="#" :
                v+=1
            if self.table[rang-1][col-1]=="#" :
                v+=1
        return v
    def affiche(self):
        global nlignes,ncol,taille,canv
        canv.delete('all')
        canv.create_rectangle( 0, 0, nlignes*taille, ncol*taille, fill="white")
        for i in range(nlignes) :
            for j in range(ncol) :
                if self.table[i][j]=="#":
                    canv.create_rectangle((taille*j,taille*i,taille*(j+1),taille*(i+1)),fill="black",outline="black") 
    def sauvegarde(self,nomf):
        global nlignes,ncol,taille
        myFile=open(nomf,'w')
        for i in range(nlignes) :
            for j in range(ncol) :
                if self.table[i][j]=="#" :
                    print(str(i)+","+str(j),file=myFile)
                    #myFile.write(str(i)+","+str(j)+" ")
        myFile.close()
         
def jouer(E,S) :
    global tour,T
    for i in range(E.nr) :
        for j in range(E.nc) :
            if (E.nombre_de_voisins(i,j)==3):
                S.table[i][j]="#"    
            elif (E.nombre_de_voisins(i,j)==2):
                S.table[i][j]=E.table[i][j]
            else :
                S.table[i][j]=" "
    T = S   
    S.affiche()
    
    tour+=1
            
def play() :
    global tour
    if (tour%2==0) :
        jouer(A,B)
    else :
        jouer(B,A)
        
def playn() :
    global canv,Entree
    for i in range(int(Entree.get())) :
        play()
        canv.update_idletasks()

def sav():
    global fen,nomf
    #noms=StringVar()
    fen=Tk()
    tex1=Label(fen, text='nom du fichier a sauvegarder')
    tex1.pack()
    tex1.grid(row =0,column = 0)
    nomf = Entry(fen, width = 10, justify = 'center')
    nomf.pack()
    nomf.grid(row=1,column=0)
    
    b= Button(fen,text ='OK',command = savclose)
    b.pack()
    b.grid(row=10,column=10)
    fen.mainloop()

def savclose():
    global fen,T,nomf
    nom=nomf.get()
    T.sauvegarde(nom)
    fen.destroy()

def read(nomf) :
    try:
        file=open(nomf)
        li=file.readlines()
    except IOError:
        print("le fichier demander n'existe pas")
    for l in range(len(li)) :
        pair=li[l].split(',')
        T.remplir(int(pair[0]),int(pair[1]))
        
def reado():
    global fen2,nomr
    #noms=StringVar()
    fen2=Tk()
    tex1=Label(fen2, text='nom du fichier a ouvrir')
    tex1.pack()
    tex1.grid(row =0,column = 0)
    nomr = Entry(fen2, width = 10, justify = 'center')
    nomr.pack()
    nomr.grid(row=1,column=0)
    
    b= Button(fen2,text ='OK',command = readclose)
    b.pack()
    b.grid(row=10,column=10)
    fen2.mainloop()

def readclose() :
    global nomr,T,fen2
    nom=nomr.get()
    read(nom)
    fen2.destroy()
    T.affiche()

def createWidgets(root):
    global canv,Entree,ck
    global nlignes,ncol,taille
    f1 = Frame(root)
    b=Button(f1)
    b["text"]="jouer"
    b["command"]=play
    b.pack()
    b.grid(row=0, column=0)
    
    
    QUIT = Button(f1)
    QUIT["text"] = "QUIT"
    QUIT["fg"] = "red"
    QUIT["command"] = root.destroy
    QUIT.pack()
    QUIT.grid(row=0, column=15)
    
    b3=Button(f1)
    b3["text"]=" jouer ... coups"
    b3["command"]=playn
    b3.pack()
    b3.grid(row=0, column=1)
    
    b4=Button(f1,text="ouvrir",command = reado)
    b4.pack()
    b4.grid(row=2,column=2)
    
    b5=Button(f1,text="sauvegarder",command = sav)
    b5.pack()
    b5.grid(row=2,column=1)
    
    
    entr =StringVar()
    Entree = Entry(f1, textvariable=entr)     # On définit l'objet Entry qui porte le nom Entree
    Entree["width"]=7
    Entree["justify"]="center"
    Entree.pack()
    Entree.grid(row=1,column=1) 
    entr.set("200")
    
    ck=IntVar()
    chk = Checkbutton(f1, text='editer ?',variable=ck,)
    chk.pack()
    chk.grid(row=2,column=10)
    
    eff=Button(f1)
    eff["text"]="effacer"
    eff["command"]=effacer
    eff.pack()
    eff.grid(row=2,column=0)
    f1.pack()
    
    canv=Canvas(root,width=nlignes*taille,height=ncol*taille)
    canv.create_rectangle( 0, 0, nlignes*taille, ncol*taille, fill="white",outline="black")
    canv.pack()
    
    canv.bind("<Button-1>", crea)
    canv.bind("<B1-Motion>",crea)
    canv.bind("<Button-2>", dest)
    canv.bind("<B2-Motion>", dest)

def effacer():
    global canv,tour,T
    canv.delete("all")
    for i in range(nlignes):
        for j in range(ncol):
            T.table[i][j]=" "
    canv.create_rectangle( 0, 0, nlignes*taille, ncol*taille, fill="white",outline="black")
    canv.pack()
   
def crea(event):
    global taille,tour,ck,T
    r=event.y//taille
    c=event.x//taille
    if ck.get()==1:
       T.remplir(r, c)
       T.affiche()

def dest(event): 
    global taille,tour,ck,T
    r=event.y//taille
    c=event.x//taille
    if ck.get()==1 :
        T.table[r][c]=" "
        T.affiche()

debut()
global tour,T
tour=0
A = Tableau(nlignes,ncol)
B = Tableau(A.nr,A.nc)
T=A
root=Tk()
createWidgets(root)
T.affiche()
root.mainloop()