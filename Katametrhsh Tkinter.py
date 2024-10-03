import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
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

def create_db():
    my_conn = dbconnect('Καταμέτρηση.db') #Δημιουργεί ΒΔ αν δεν υπάρχει
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
    # Καταχώρηση εγγραφών στον πίνακα παρουσίασης
    for item in item_list:
        tree.insert('',tk.END,values=item)    
    return


def emfanishKatametrhshs():
    # Νέο παράθυρο
    new = tk.Toplevel(mainWindow)
    new.title("Πίνακας Καταμέτρησης")
    new.geometry("500x800+700+150")
    # Προετοιμασία για πίνακα παρουσίασης
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
    # Καλεί τη συνάρτηση για καταχώρηση εγγραφών
    printKatametrhsh()
    tree.pack(fill='both',expand=1)
    new.mainloop()        
    return


def updateDB(db_state):
    my_conn = dbconnect('Καταμέτρηση.db')
    c = my_conn.cursor()
    if db_state == 0:        ## Εαν δεν υπάρχει table
        sql_query = '''CREATE TABLE "ΑποθηκευμένηΚαταμέτρηση" (
    	"Αντικείμενο"	TEXT [30] NOT NULL,
    	"Ποσότητα"	INTEGER NOT NULL CHECK("Ποσότητα" >= 0),
    	PRIMARY KEY("Αντικείμενο")
    );''' 
        c.execute(sql_query) 
        
        for i in item_list:
            sql_query = '''INSERT INTO "ΑποθηκευμένηΚαταμέτρηση" 
            VALUES ("'''+str(i[0])+'''", '''+str(i[1])+''');'''
            c.execute(sql_query)
    else: # Eάν υπάρχει, με μηδενικά ή μη δεδομένα
        for i in item_list:
            sql_query= '''UPDATE "ΑποθηκευμένηΚαταμέτρηση" 
            SET "Ποσότητα" = '''+str(i[1])+'''
            WHERE "Αντικείμενο" = "'''+str(i[0])+'''";'''
            c.execute(sql_query)
    my_conn.commit()
    my_conn.close()
    return
    
    

def save_button():
    db_state = table_empty_check()
    if db_state == 2: 
    # Αν η καταχωρημένη καταμέτρηση έχει δεδομένα προειδοποιεί
        confirmation = msg.askyesno(
            title='Αποθήκευση Καταμέτρησης', 
            parent=mainWindow, 
            message='''Θέλετε σίγουρα να αποθηκεύσετε την καταμέτρηση; 
Η προηγούμενη καταμέτρηση θα σβηστεί.''')
        if not confirmation:
            msg.showerror(master=mainWindow, 
                          parent=mainWindow, 
                          title='Ειδοποίηση', 
                          message="Η αποθήκευση ακυρώθηκε από τον χρήστη.")
            return
    # Έλεγχος αν η τρέχουσα καταμέτρηση δεν έχει τιμές
    zeros_only= True
    for i in range(0, len(item_list)):
        if item_list[i][1] != 0:
            zeros_only = False
    # Επιβεβαίωση αποθήκευσης καταμέτρησης με μηδενικές τιμές
    if zeros_only:
        confirmation = msg.askyesno(
            title='Αποθήκευση Μηδενικής Καταμέτρησης', 
            parent=mainWindow, 
            message='''Θέλετε σίγουρα να αποθηκεύσετε τη μηδενική καταμέτρηση;''')
        if not confirmation:
            msg.showerror(master=mainWindow, 
                          parent=mainWindow, 
                          title='Ειδοποίηση', 
                          message="Η αποθήκευση ακυρώθηκε από τον χρήστη.")
            return
    updateDB(db_state)
    msg.showinfo(title = 'Επιτυχής Αποθήκευση', 
                 parent = mainWindow,
                 message = 'Η καταμέτρηση αποθηκεύτηκε επιτυχώς.')
    return

def table_empty_check(): 
# 0 = Δεν υπάρχει table 
# 1 = υπάρχει αλλά έχει μηδενικά δεδομένα
# 2 = υπάρχει κι έχει δεδομένα
    my_conn = dbconnect('Καταμέτρηση.db')
    sql_query = '''SELECT * FROM "ΑποθηκευμένηΚαταμέτρηση";'''
    c = my_conn.cursor()
    db_contents = []
    try:
        db_contents = c.execute(sql_query).fetchall()
    except sqlite3.OperationalError:
        db_state = 0
        my_conn.close()
        return db_state
    db_state = 1
    for i in db_contents:
        if i[1] != 0:
            db_state = 2    
    my_conn.close()
    return db_state
    

def load():
    db_state = table_empty_check()
    if db_state == 0:
        msg.showerror(master = mainWindow,
                      parent = mainWindow,
                      title = 'Ειδοποίηση',
                      message = 'Δεν υπάρχουν δεδομένα για φόρτωση.')
        return
    # Έλεγχος αν η τρέχουσα καταμέτρηση δεν έχει τιμές
    zeros_only= True
    for i in range(0, len(item_list)):
        if item_list[i][1] != 0:
            zeros_only = False
    # Ζητάει επιβεβαίωση απαλοιφής τρέχουσας καταμέτρησης εφόσον περιέχει τιμές
    if not zeros_only:    
        confirmation = msg.askyesno(
                title='Φόρτωση Καταμέτρησης', 
                parent=mainWindow, 
                message='''Θέλετε σίγουρα να φορτώσετε την αποθηκευμένη καταμέτρηση; 
Τα δεδομένα της τρέχουσας καταμέτρησης θα σβηστούν.''')
        if not confirmation:
            msg.showerror(master=mainWindow, 
                          parent=mainWindow, 
                          title='Ειδοποίηση', 
                          message="Η φόρτωση ακυρώθηκε από τον χρήστη.")
            return

    my_conn = dbconnect('Καταμέτρηση.db')
    sql_query = '''SELECT * FROM "ΑποθηκευμένηΚαταμέτρηση";'''
    c = my_conn.cursor()
    db_contents = c.execute(sql_query).fetchall()
    for i in item_list:
        i[1] = db_contents[item_list.index(i)][1]
    my_conn.close()
    # Αν φορτώθηκε καταμέτρηση με μηδενικές τιμές
    if db_state == 1:
        msg.showinfo(parent = mainWindow,
                     title = 'Ειδοποίηση',
                     message = 'Φορτώθηκε μηδενική καταμέτρηση επιτυχώς.')
    else:
        msg.showinfo(parent = mainWindow,
                     title = 'Ειδοποίηση',
                     message = 'Φορτώθηκε καταμέτρηση επιτυχώς.')
    return
        

def reset_pushed():
    # Έλεγχος αν ο μηδενισμός είναι ανούσιος
    empty_flag = True
    for i in range(0,len(item_list)):
        if item_list[i][1] != 0:
            empty_flag = False
            break
    if empty_flag:
        msg.showinfo(parent = mainWindow,
                     title = 'Ειδοποίηση',
                     message = 'Η τρέχουσα καταμέτρηση είναι ήδη μηδενική.')
        return
    
    confirmation = msg.askyesno(
                title='Μηδενισμός Καταμέτρησης', 
                parent=mainWindow, 
                message='''Θέλετε σίγουρα να μηδενίσετε την τρέχουσα καταμέτρηση; 
Τα δεδομένα της θα σβηστούν.''')
    if not confirmation:
        msg.showerror(master=mainWindow, 
                      parent=mainWindow, 
                      title='Ειδοποίηση', 
                      message="Ο μηδενισμός ακυρώθηκε από τον χρήστη.")
        return
    for i in range(0, len(item_list) ):
        item_list[i][1]=0
    msg.showinfo(parent = mainWindow,
                 title = 'Ειδοποίηση',
                 message = 'Η τρέχουσα καταμέτρηση μηδενίστηκε επιτυχώς.')
    return
    
# Δημιουργία ΒΔ αν δεν υπάρχει
create_db()

mainWindow = tk.Tk()
mainWindow.geometry('600x500+650+150')
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
    text = "Μηδενισμός Τρέχουσας Καταμέτρησης",
    font = defaultFont,
    command = reset_pushed,
    relief = 'groove',
    bd = 10).pack(fill = 'x',
        padx = 50,
        pady = 10)

tk.Button(mainWindow, 
          text = "Αποθήκευση Καταμέτρησης", 
          font = defaultFont,
          command = save_button,
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

tk.Label(mainWindow, 
         text='Made by Black Baron', 
         font = ('Old English Text MT',12),
         justify='left').pack(side='right')

mainWindow.mainloop()