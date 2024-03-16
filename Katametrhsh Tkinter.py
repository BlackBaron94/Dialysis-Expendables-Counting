# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:05:09 2024

@author: Equinox
"""

import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
item_list = [["25H", 0], 
            ["21H", 0], 
            ["19H", 0],
            ["21M", 0],
            ["19M", 0],
            ["17M", 0],
            ["FDY 210", 0],
            ["FDY 180", 0],
            ["FDY 150", 0],
            ["Γραμμές & Φύσιγγες", 0],
            ["Γραμμές Online", 0],
            ["293", 0],
            ["751", 0],
            ["296", 0],
            ["257", 0],
            ["1.75 Ca", 0],
            ["1.25 Ca", 0]]

def dbconnect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table():
    my_conn = dbconnect('katametrhsh.db') #Δημιουργεί ΔΒ αν δεν υπάρχει
    sql_query = '''CREATE TABLE IF NOT EXISTS "katametrhsh" (
	"AA"	INTEGER NOT NULL,
	"Αντικείμενο"	TEXT [30] NOT NULL,
	"Ποσότητα"	INTEGER,
	PRIMARY KEY("AA" AUTOINCREMENT)
);''' 
    c = my_conn.cursor()
    c.execute(sql_query) 
    my_conn.commit()
    my_conn.close()
    return

def addItem(string):
    global times
    # Μεταβλητή για έλεγχο φορών καταχώρησης
    for i in item_list:
        if i[0] == string:
            item_list[item_list.index(i)][1] += 1
            if "M" in i[0] or "F" in i[0] or "H" in i[0]:
                item_list[9][1] += 1
            if "H" in i[0] or "F" in i[0]:
                item_list[10][1] += 1
    # Έλεγχος αν το τρέχον αντικείμενο είναι αυτό που καταχωρήθηκε στην
    # προηγούμενη καταχώρηση
    if string in myStringVar.get(): 
        times += 1 
        text = string + " καταχωρήθηκε " + str(times) + " φορές επιτυχώς."
        myStringVar.set(text)
    
    else:
        # Αρχικοποίηση μεταβλητής times
        times = 1
        text = string + " καταχωρήθηκε επιτυχώς."
        myStringVar.set(text)
    return

def x25HPushed():
    addItem("25H")
    return
    
def x21HPushed():
    addItem("21H")
    return
    
def x19HPushed():
    addItem("19H")
    return

def x21MPushed():
    addItem("21M")
    return

def x19MPushed():
    addItem("19M")
    return

def x17MPushed():
    addItem("17M")
    return
    
def FDY210Pushed():
    addItem("FDY 210")
    return

def FDY180Pushed():
    addItem("FDY 180")
    return
    
def FDY150Pushed():
    addItem("FDY 150")
    return

def x293Pushed():
    addItem("293")
    return

def x751Pushed():
    addItem("751")
    return    
    
def x296Pushed():
    addItem("296")
    return

def x257Pushed():
    addItem("257")
    return

def x175CAPushed():
    addItem("1.75 Ca")
    return

def x125CAPushed():
    addItem("1.25 Ca")
    return
    
def enarkshKatametrhshs():
    global enarkshKatametrhshsWindow
    enarkshKatametrhshsWindow = tk.Toplevel(mainWindow)
    enarkshKatametrhshsWindow.geometry("425x400+770+220")
    enarkshKatametrhshsWindow.title("Καταμέτρηση")
    global myStringVar
    myStringVar = tk.StringVar()
    myStringVar.set("Καμία καταχώρηση")
    tk.Button(enarkshKatametrhshsWindow, 
              text = "25H", 
              font = 'Times 16', 
              command = x25HPushed).place(x=30, y=10)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "21H", 
              font = 'Times 16', 
              command = x21HPushed).place(x=30, y=60)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "19H", 
              font = 'Times 16', 
              command = x19HPushed).place(x=30, y=110)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "FDY 210", 
              font = 'Times 16', 
              command = FDY210Pushed).place(x=10, y=160)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "FDY 180", 
              font = 'Times 16', 
              command = FDY180Pushed).place(x=10, y=210)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "FDY 150", 
              font = 'Times 16', 
              command = FDY150Pushed).place(x=10, y=260)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "21M", 
              font = 'Times 16', 
              command = x21MPushed).place(x=185, y=10)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "19M", 
              font = 'Times 16', 
              command = x19MPushed).place(x=185, y=60)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "17M", 
              font = 'Times 16', 
              command = x17MPushed).place(x=185, y=110)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "293", 
              font = 'Times 16', 
              command = x293Pushed).place(x=325, y=10)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "751", 
              font = 'Times 16', 
              command = x751Pushed).place(x=325, y=60)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "296", 
              font = 'Times 16', 
              command = x296Pushed).place(x=325, y=110)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "257", 
              font = 'Times 16', 
              command = x257Pushed).place(x=325, y=160)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "1.75 Ca", 
              font = 'Times 16', 
              command = x175CAPushed).place(x=305, y=210)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "1.25 Ca", 
              font = 'Times 16', 
              command = x125CAPushed).place(x=305, y=260)
    tk.Label(enarkshKatametrhshsWindow, 
             textvariable = myStringVar, 
             font = 'Times 16',
             justify='center').place(x=25, y=325)  
    return


def printKatametrhsh():
    for item in item_list:
        tree.insert('',tk.END,values=item)    
    return


def emfanishKatametrhshs():
    new = tk.Toplevel(mainWindow)
    new.title("Πίνακας Καταμέτρησης")
    new.geometry("500x800+700+150")
    style = ttk.Style()
    style.configure("mystyle.Treeview",font=('Times',16),rowheight=30)
    global tree
    tree = ttk.Treeview(new, 
                        style="mystyle.Treeview", 
                        columns=('Αντικείμενο', 
                                 'Ποσότητα'),
                        show='headings')
    tree.column('Αντικείμενο', width=50)
    tree.column('Ποσότητα', width=50)
    tree.heading('Αντικείμενο', text = 'Αντικείμενο')
    tree.heading('Ποσότητα', text = 'Ποσότητα')
    printKatametrhsh()
    tree.pack(fill='both',expand=1)
    new.mainloop()        
    return

def savePushed():
    saveWindowEntry.delete(0,'end')

def save():
    global saveWindow
    saveWindow = tk.Toplevel(mainWindow)
    saveWindow.geometry("550x200+650+450")
    saveWindow.title('Αποθήκευση Καταμέτρησης')
    tk.Label(saveWindow, 
             text='Δώστε το όνομα της καταμέτρησης που θέλετε να αποθηκεύσετε: ', 
             font = 'Times 14').pack(pady=20)
    global saveWindowEntry
    saveWindowEntry = tk.Entry(saveWindow,
                               justify = 'center', 
                               font=defaultFont)
    saveWindowEntry.pack(pady=5)
    tk.Button(saveWindow, 
              text='Αποθήκευση', 
              font='Times 16', 
              command=savePushed).pack(side='left',
                                       padx=60)
    tk.Button(saveWindow, 
              text='Ακύρωση', 
              font='Times 16', 
              command=saveWindow.destroy).pack(side='right',
                                               padx=60)
    
    saveWindow.mainloop()

def load():
    pass

create_table()

mainWindow = tk.Tk()
mainWindow.geometry('600x800+650+150')
mainWindow.title("Πρόγραμμα Καταμέτρησης Υλικού")
defaultFont = 'Times 16'
tk.Button(mainWindow,
    text = 'Έναρξη Καταμέτρησης', 
    font = defaultFont, 
    command = enarkshKatametrhshs, 
    relief = 'groove', 
    bd = 10).pack(fill = 'x', 
        padx = 50, 
        pady = 10)
tk.Button(mainWindow, 
          text = "Εμφάνιση Καταμέτρησης", 
          font = defaultFont,
          command = emfanishKatametrhshs,
          relief = 'groove',
          bd = 10).pack(fill = 'x',
              padx = 50,
              pady = 10)   
tk.Button(mainWindow, 
          text = "Αποθήκευση Καταμέτρησης", 
          font = defaultFont,
          command = save,
          relief = 'groove',
          bd = 10).pack(fill = 'x',
              padx = 50,
              pady = 10)   
tk.Button(mainWindow, 
    text = "Φόρτωση Καταμέτρησης",
    font = defaultFont,
    command = load,
    relief = 'groove',
    bd = 10).pack(fill = 'x',
        padx = 50,
        pady = 10)

tk.Button(mainWindow, 
    text = "Έξοδος",
    font = defaultFont,
    command = mainWindow.destroy,
    relief = 'groove',
    bd = 10).pack(fill = 'x',
        padx = 50,
        pady = 10)



mainWindow.mainloop()
