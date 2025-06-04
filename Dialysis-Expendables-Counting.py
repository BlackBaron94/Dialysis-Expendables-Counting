# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 13:25:31 2025

@author: Equinox
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
from sqlite3 import Error
item_list = [
    ["25H", 0], 
    ["21H", 0], 
    ["19H", 0],
    ["FDY 210", 0],
    ["FDY 180", 0],
    ["FDY 150", 0],
    ["21M", 0],
    ["19M", 0],
    ["17M", 0],
    ["Γραμμές & Φύσιγγες", 0],
    ["Γραμμές Online", 0],
    ["293", 0],
    ["751", 0],
    ["296", 0],
    ["257", 0],
    ["1.75 Ca", 0],
    ["1.25 Ca", 0]
    ]

def dbconnect(db_file):
    """
    Βοηθητική συνάρτηση που συνδέεται με/δημιουργεί ΒΔ.
    
    
    Args:
        db_file (str): Όνομα του αρχείου ΒΔ.
        
    Returns:
        sqlite3.Connection: Αντικείμενο σύνδεσης στη βάση δεδομένων ή None σε 
        περίπτωση αποτυχίας.
    """
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_db():
    """
    Δημιουργεί βάση δεδομένων αν δεν υπάρχει.
    """
    my_conn = dbconnect('Καταμέτρηση.db') 
    my_conn.close()
    return

def addItem(string, window):
    """
    Ανανεώνει το πλήθος των αντικειμένων που καταμετρούνται.
    
    
    Args:
        string (str): Όνομα αντικειμένου προς προσθήκη.
        window (tkinter Toplevel object): Δέχεται το παράθυρο έναρξης 
        καταμέτρησης για να έχει πρόσβαση στη StringVar και στη μεταβλητή times
        για τις φορές καταμέτρησης ίδιου αντικειμένου κατά συρροήν.
    
    Returns:
        None.
    """
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
    if string in window.myStringVar.get(): 
        window.times += 1 
        text = string + " καταχωρήθηκε " + str(window.times) + " φορές επιτυχώς."
        window.myStringVar.set(text)
    
    else:
        # Αρχικοποίηση μεταβλητής times
        window.times = 1
        text = string + " καταχωρήθηκε επιτυχώς."
        window.myStringVar.set(text)
    return

    
def enarkshKatametrhshs():
    """
    Συνάρτηση κουμπιού έναρξης καταμέτρησης του κυρίου παραθύρου.
    Δημιουργεί δευτερεύον παράθυρο με κουμπιά για κάθε αντικείμενο της 
    καταμέτρησης και στο κάτω μέρος δείχνει το τελευταίο αντικείμενο που εισήχθη
    και τις φορές που προστέθηκε κατά συρροήν.
    """
    
    enarkshKatametrhshsWindow = tk.Toplevel(mainWindow)
    enarkshKatametrhshsWindow.geometry("425x400+770+220")
    enarkshKatametrhshsWindow.title("Καταμέτρηση")
    enarkshKatametrhshsWindow.bind(
        "<Escape>", 
        lambda event: enarkshKatametrhshsWindow.destroy()
        )
    
    # Πεδίο του παραθύρου που διατηρεί τις φορές κατά συρροήν 
    # που πατήθηκε το ίδιο κουμπί
    enarkshKatametrhshsWindow.times = 0
    
    # Η StringVar μπαίνει ως πεδίο του παραθύρου για πρόσβαση
    # από την addItem που μεταβάλει το Label αυτό δυναμικά
    enarkshKatametrhshsWindow.myStringVar = tk.StringVar()
    enarkshKatametrhshsWindow.myStringVar.set("Καμία καταχώρηση")
    
    # Λίστα με θέσεις κουμπιών
    button_locations = [
        [30, 10],
        [30, 60],
        [30, 110],
        [10, 160],
        [10, 210],
        [10, 260],
        [185, 10],
        [185, 60],
        [185, 110],
        [325, 10],
        [325, 60],
        [325, 110],
        [325, 160],
        [305, 210],
        [305, 260]
        ]
    # Δείκτης προσπέλασης λίστας θέσεων κουμπιών
    button_loc_index = 0
    # Δημιουργία κουμπιών
    for i in item_list:
        # Οι Γραμμές και οι φύσιγγες προστίθενται αυτόματα από το πρόγραμμα
        # άρα δεν χρειάζονται κουμπιά
        if i[0] == 'Γραμμές & Φύσιγγες' or i[0] == 'Γραμμές Online':
            continue
        tk.Button(
            enarkshKatametrhshsWindow,
            text = i[0],
            font = 'Times 16',
            command = lambda i=i: addItem(i[0], enarkshKatametrhshsWindow)
            ).place(
                x=button_locations[button_loc_index][0],
                y=button_locations[button_loc_index][1]
                 )
        button_loc_index +=1
        
    tk.Label(enarkshKatametrhshsWindow, 
             textvariable = enarkshKatametrhshsWindow.myStringVar, 
             font = 'Times 16',
             justify='center').place(x=25, y=325)  
    enarkshKatametrhshsWindow.focus_set()
    enarkshKatametrhshsWindow.mainloop()
    return


def printKatametrhsh(window):
    """
    Βοηθητική συνάρτηση για τη δημιουργία των στατιστικών στο παράθυρο 
    εμφάνισης καταμέτρησης.
    
    Args:
        window (TopLevel object): Το παράθυρο στου οποίου το treeview
        φορτώνονται τα δεδομένα. Απαιτείται για πρόσβαση στο attribute tree.
    """
    
    # Καταχώρηση εγγραφών στον πίνακα παρουσίασης
    for item in item_list:
        window.tree.insert('',tk.END,values=item)    
    return


def emfanishKatametrhshs():
    """
    Συνάρτηση για το κουμπί εμφάνισης καταμέτρησης του κυρίου παραθύρου.
    
    Δημιουργεί δευτερεύον παράθυρο με πίνακα των αντικειμένων και την ποσότητα
    της τρέχουσας καταμέτρησης.
    """
    
    # Νέο παράθυρο
    emfanishKatametrhshsWindow = tk.Toplevel(mainWindow)
    emfanishKatametrhshsWindow.title("Πίνακας Καταμέτρησης")
    emfanishKatametrhshsWindow.geometry("500x800+700+150")
    emfanishKatametrhshsWindow.bind(
        "<Escape>", 
        lambda event: emfanishKatametrhshsWindow.destroy()
        )
    # Προετοιμασία για πίνακα παρουσίασης
    style = ttk.Style()
    style.configure("mystyle.Treeview",font=('Times',16),rowheight=30)
    
    emfanishKatametrhshsWindow.tree = ttk.Treeview(
        emfanishKatametrhshsWindow, 
        style="mystyle.Treeview", 
        columns=(
            'Αντικείμενο', 
            'Ποσότητα'
            ),
        show='headings'
        )
    emfanishKatametrhshsWindow.tree.column('Αντικείμενο', width=50)
    emfanishKatametrhshsWindow.tree.column('Ποσότητα', width=50)
    emfanishKatametrhshsWindow.tree.heading('Αντικείμενο', text = 'Αντικείμενο')
    emfanishKatametrhshsWindow.tree.heading('Ποσότητα', text = 'Ποσότητα')
    # Καλεί τη συνάρτηση για καταχώρηση εγγραφών
    printKatametrhsh(emfanishKatametrhshsWindow)
    emfanishKatametrhshsWindow.tree.pack(fill='both',expand=1)
    emfanishKatametrhshsWindow.focus_set()
    emfanishKatametrhshsWindow.mainloop()        
    return


def updateDB(db_state):
    """
    Βοηθητική συνάρτηση που αποθηκεύει στη ΒΔ τα δεδομένα 
    της τρέχουσας καταμέτρησης.
    
    
    Args:
        db_state (int): Ύπαρξη table ή όχι. 
        Αν είναι 0, δεν υπάρχει table. 
        Αν δεν είναι 0, υπάρχει table.
    
    Returns:
        None.
    """
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
    """
    Συνάρτηση για την ανταπόκριση του κουμπιού αποθήκευση καταμέτρησης του 
    κυρίου παραθύρου. 
    Ελέγχει κατάσταση ΒΔ, (με ή χωρίς table, table με δεδομένα ή χωρίς), 
    εμφανίζει παράθυρο επιβεβαίωσης αναλόγως με την κατάσταση της καταμέτρησης
    και της ΒΔ.
    """
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
    """
    Ελέγχει τρέχουσα κατάσταση της ΒΔ.
    
    
    Returns:
        int:    0 = Δεν υπάρχει table.
                1 = Υπάρχει table, αλλά έχει μηδενικά δεδομένα.
                2 = Υπάρχει table και περιέχει δεδομένα.
    """

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
    """
    Ελέγχει την κατάσταση της ΒΔ και φορτώνει δεδομένα στην τρέχουσα καταμέτρηση.
    Ελέγχει αν η τρέχουσα καταμέτρηση περιέχει δεδομένα που θα χαθούν και 
    ενημερώνει με το κατάλληλο pop-up.
    """
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
        if db_state == 1:
            confirmation = msg.askyesno(
                    title='Φόρτωση Μηδενικής Καταμέτρησης', 
                    parent=mainWindow, 
                    message='''Προσπαθείτε να φορτώσετε αποθηκευμένη μηδενική 
καταμέτρηση ενώ η τρέχουσα καταμέτρηση περιέχει δεδομένα. 
Να γίνει φόρτωση;''')
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
        emfanishKatametrhshs()
    return
        

def reset_pushed():
    """
    Συνάρτηση απόκρισης στο κουμπί Μηδενισμός τρέχουσας καταμέτρησης.
    Μηδενίζει τις τιμές για όλα τα αντικείμενα της καταμέτρησης αφότου:
        Ελέγξει αν είναι ήδη μηδενική.
        Ζητήσει επιβεβαίωση από τον χρήστη.
    """
    
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
    



if __name__ == "__main__":
    # Δημιουργία ΒΔ αν δεν υπάρχει
    create_db()
    # Δημιουργία κυρίου παραθύρου
    mainWindow = tk.Tk()
    mainWindow.geometry('600x500+650+150')
    mainWindow.title("Πρόγραμμα Καταμέτρησης Υλικού")
    defaultFont = 'Times 16'
    
    tk.Button(
        mainWindow,
        text = 'Έναρξη καταμέτρησης', 
        font = defaultFont, 
        command = enarkshKatametrhshs, 
        relief = 'groove', 
        bd = 10
        ).pack(
            fill = 'x', 
            padx = 50, 
            pady = 10
            )                  
    
    tk.Button(mainWindow, 
              text = "Εμφάνιση καταμέτρησης", 
              font = defaultFont,
              command = emfanishKatametrhshs,
              relief = 'groove',
              bd = 10).pack(fill = 'x',
                  padx = 50,
                  pady = 10)   
    
    tk.Button(mainWindow, 
        text = "Μηδενισμός τρέχουσας καταμέτρησης",
        font = defaultFont,
        command = reset_pushed,
        relief = 'groove',
        bd = 10).pack(fill = 'x',
            padx = 50,
            pady = 10)
    
    tk.Button(mainWindow, 
              text = "Αποθήκευση καταμέτρησης", 
              font = defaultFont,
              command = save_button,
              relief = 'groove',
              bd = 10).pack(fill = 'x',
                  padx = 50,
                  pady = 10)   
    
    tk.Button(mainWindow, 
        text = "Φόρτωση καταμέτρησης",
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
