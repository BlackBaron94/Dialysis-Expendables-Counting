# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:05:09 2024

@author: Equinox
"""

import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
item_list = ["25H", 
                "21H", 
                "19H",
                "21M",
                "19M",
                "17M",
                "FDY210",
                "FDY180",
                "FDY150",
                "RawNumber",
                "Online",
                "293",
                "751",
                "296",
                "257",
                "175CA",
                "125CA"]

quantity_list = []

quantity_list = [0] * (len(item_list))

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

def addItem(string):
    for i in item_list:
        if i == string:
            quantity_list[item_list.index(i)] += 1

def x25HPushed():
    addItem("25H")
    
def x21HPushed():
    addItem("21H")
    
def x19HPushed():
    addItem("19H")

def x21MPushed():
    addItem("21M")

def x19MPushed():
    addItem("19M")

def x17MPushed():
    addItem("17M")

def FDY210Pushed():
    addItem("FDY210")

def FDY180Pushed():
    addItem("FDY180")
    
def FDY150Pushed():
    addItem("FDY150")

def x293Pushed():
    addItem("293")

def x751Pushed():
    addItem("751")
    
def x296Pushed():
    addItem("296")

def x257Pushed():
    addItem("257")

def x175CAPushed():
    addItem("175CA")

def x125CAPushed():
    addItem("125CA")
    
def enarkshKatametrhshs():
    global enarkshKatametrhshsWindow
    enarkshKatametrhshsWindow = tk.Toplevel(mainWindow)
    enarkshKatametrhshsWindow.geometry("650x200+650+450")
    enarkshKatametrhshsWindow.title("Καταμέτρηση")
    tk.Button(enarkshKatametrhshsWindow, 
              text = "25H", 
              font = 'Times 16', 
              command = x25HPushed).place(x=35, y=10)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "21H", 
              font = 'Times 16', 
              command = x21HPushed).place(x=35, y=60)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "19H", 
              font = 'Times 16', 
              command = x19HPushed).place(x=35, y=110)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "FDY210", 
              font = 'Times 16', 
              command = FDY210Pushed).place(x=10, y=160)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "FDY180", 
              font = 'Times 16', 
              command = FDY180Pushed).place(x=10, y=210)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "FDY150", 
              font = 'Times 16', 
              command = FDY150Pushed).place(x=10, y=260)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "21M", 
              font = 'Times 16', 
              command = x21MPushed).place(x=150, y=10)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "19M", 
              font = 'Times 16', 
              command = x19MPushed).place(x=150, y=60)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "17M", 
              font = 'Times 16', 
              command = x17MPushed).place(x=150, y=110)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "293", 
              font = 'Times 16', 
              command = x293Pushed).place(x=320, y=10)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "751", 
              font = 'Times 16', 
              command = x751Pushed).place(x=320, y=60)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "296", 
              font = 'Times 16', 
              command = x296Pushed).place(x=320, y=110)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "257", 
              font = 'Times 16', 
              command = x257Pushed).place(x=320, y=160)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "175CA", 
              font = 'Times 16', 
              command = x175CAPushed).place(x=300, y=210)
    tk.Button(enarkshKatametrhshsWindow, 
              text = "125CA", 
              font = 'Times 16', 
              command = x125CAPushed).place(x=300, y=260)


create_table()

mainWindow = tk.Tk()
mainWindow.geometry('600x800+650+150')
mainWindow.title("Πρόγραμμα Καταμέτρησης Υλικού")
defaultFont = 'Times 16'
koumpiProsthhkhsFiltrou = tk.Button(mainWindow,
                                    text = 'Έναρξη Καταμέτρησης', 
                                    font = defaultFont, 
                                    command = enarkshKatametrhshs, 
                                    relief = 'groove', 
                                    bd = 10)
koumpiEksodou = tk.Button(mainWindow, 
                          text = "Έξοδος",
                          font = defaultFont,
                          command = mainWindow.destroy,
                          relief = 'groove',
                          bd = 10)
koumpiProsthhkhsFiltrou.pack(fill = 'x', 
                             padx = 50, 
                             pady = 10)
koumpiEksodou.pack(fill = 'x',
                   padx = 50,
                   pady = 10)


mainWindow.mainloop()
