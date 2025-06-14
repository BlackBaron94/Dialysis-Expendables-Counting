# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 13:25:31 2025

@author: Equinox
"""

import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import messagebox as msg
import sqlite3
from sqlite3 import Error


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
    my_conn = dbconnect("Καταμέτρηση.db")
    my_conn.close()
    return


def add_item(string, window, main_window):
    """
    Ανανεώνει το πλήθος των αντικειμένων που καταμετρούνται.


    Args:
        string (str): Όνομα αντικειμένου προς προσθήκη.
        window (tkinter Toplevel object): Δέχεται το παράθυρο έναρξης
        καταμέτρησης για να έχει πρόσβαση στη StringVar και στη μεταβλητή times
        για τις φορές καταμέτρησης ίδιου αντικειμένου κατά συρροήν.
        main_window (Tk Object): Το κύριο παράθυρο της εφαρμογής για αλλαγή
        των ποσοτήτων του πεδίου main_window.item_list.

    Returns:
        None.
    """
    # Μεταβλητή για έλεγχο φορών καταχώρησης
    for item in main_window.item_list:
        if item[0] == string:
            main_window.item_list[main_window.item_list.index(item)][1] += 1
            if "M" in item[0] or "F" in item[0] or "H" in item[0]:
                main_window.item_list[9][1] += 1
            if "H" in item[0] or "F" in item[0]:
                main_window.item_list[10][1] += 1
    # Έλεγχος αν το τρέχον αντικείμενο είναι αυτό που καταχωρήθηκε στην
    # προηγούμενη καταχώρηση
    if string in window.my_string_var.get():
        window.times += 1
        text = (
            string + " καταχωρήθηκε " + str(window.times) + " φορές επιτυχώς."
        )
        window.my_string_var.set(text)

    else:
        # Αρχικοποίηση μεταβλητής times
        window.times = 1
        text = string + " καταχωρήθηκε επιτυχώς."
        window.my_string_var.set(text)
    return


def enarksh_katametrhshs(main_window):
    """
    Συνάρτηση κουμπιού έναρξης καταμέτρησης του κυρίου παραθύρου.
    Δημιουργεί δευτερεύον παράθυρο με κουμπιά για κάθε αντικείμενο της
    καταμέτρησης και στο κάτω μέρος δείχνει το τελευταίο αντικείμενο που εισήχθη
    και τις φορές που προστέθηκε κατά συρροήν.


    Args:
        main_window (Tk Object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """

    enarksh_katametrhshs_window = tk.Toplevel(main_window)
    enarksh_katametrhshs_window.geometry("425x400+770+220")
    enarksh_katametrhshs_window.title("Καταμέτρηση")
    enarksh_katametrhshs_window.bind(
        "<Escape>", lambda event: enarksh_katametrhshs_window.destroy()
    )

    # Πεδίο του παραθύρου που διατηρεί τις φορές κατά συρροήν
    # που πατήθηκε το ίδιο κουμπί
    enarksh_katametrhshs_window.times = 0

    # Η StringVar μπαίνει ως πεδίο του παραθύρου για πρόσβαση
    # από την addItem που μεταβάλει το Label αυτό δυναμικά
    enarksh_katametrhshs_window.my_string_var = tk.StringVar()
    enarksh_katametrhshs_window.my_string_var.set("Καμία καταχώρηση")

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
        [305, 260],
    ]
    # Δείκτης προσπέλασης λίστας θέσεων κουμπιών
    button_loc_index = 0
    # Δημιουργία κουμπιών
    for item in main_window.item_list:
        # Οι Γραμμές και οι φύσιγγες προστίθενται αυτόματα από το πρόγραμμα
        # άρα δεν χρειάζονται κουμπιά
        if item[0] == "Γραμμές & Φύσιγγες" or item[0] == "Γραμμές Online":
            continue
        tk.Button(
            enarksh_katametrhshs_window,
            text=item[0],
            font="Times 16",
            command=lambda item=item: add_item(
                item[0], enarksh_katametrhshs_window, main_window
            ),
        ).place(
            x=button_locations[button_loc_index][0],
            y=button_locations[button_loc_index][1],
        )
        button_loc_index += 1

    tk.Label(
        enarksh_katametrhshs_window,
        textvariable=enarksh_katametrhshs_window.my_string_var,
        font="Times 16",
        justify="center",
    ).place(x=25, y=325)
    enarksh_katametrhshs_window.focus_set()
    enarksh_katametrhshs_window.mainloop()
    return


def fill_tree(tree, item_list):
    """
    Βοηθητική συνάρτηση για τη δημιουργία των στατιστικών στο παράθυρο
    εμφάνισης καταμέτρησης.

    Args:
        window (TopLevel object): Το παράθυρο στου οποίου το treeview
        φορτώνονται τα δεδομένα. Απαιτείται για πρόσβαση στο attribute tree.
    """
    # Διαγράφει τα δεδομένα του Treeview.
    # Αν είναι άδειο, δεν κάνει κάποια αλλαγή.
    tree.delete(*tree.get_children())

    icon = PhotoImage(file="pencil-button.png")
    tree.image_references = []
    # Καταχώρηση εγγραφών στον πίνακα παρουσίασης
    for item in item_list:
        tree.insert("", tk.END, text=" ", image=icon, values=item)
        tree.image_references.append(icon)
    return


def emfanish_katametrhshs(main_window):
    """
    Συνάρτηση για το κουμπί εμφάνισης καταμέτρησης του κυρίου παραθύρου.

    Δημιουργεί δευτερεύον παράθυρο με πίνακα των αντικειμένων και την ποσότητα
    της τρέχουσας καταμέτρησης.


    Args:
        main_window (Tk Object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """

    # Νέο παράθυρο
    emfanish_katametrhshs_window = tk.Toplevel(main_window)
    emfanish_katametrhshs_window.title("Πίνακας Καταμέτρησης")
    emfanish_katametrhshs_window.geometry("500x800+700+150")
    emfanish_katametrhshs_window.bind(
        "<Escape>", lambda event: emfanish_katametrhshs_window.destroy()
    )
    # Προετοιμασία για πίνακα παρουσίασης
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=("Times", 16), rowheight=30)
    style.configure("mystyle.Treeview.Heading", font=("Times", 16))

    emfanish_katametrhshs_window.tree = ttk.Treeview(
        emfanish_katametrhshs_window,
        style="mystyle.Treeview",
        columns=("Αντικείμενο", "Ποσότητα"),
        show="tree headings",
    )
    emfanish_katametrhshs_window.tree.column("#0", width=50)
    emfanish_katametrhshs_window.tree.column("Αντικείμενο", width=50)
    emfanish_katametrhshs_window.tree.column("Ποσότητα", width=50)
    emfanish_katametrhshs_window.tree.heading("#0", text="Επεξεργασία")
    emfanish_katametrhshs_window.tree.heading(
        "Αντικείμενο", text="Αντικείμενο"
    )
    emfanish_katametrhshs_window.tree.heading("Ποσότητα", text="Ποσότητα")
    # Καλεί τη συνάρτηση για καταχώρηση εγγραφών
    fill_tree(emfanish_katametrhshs_window.tree, main_window.item_list)
    emfanish_katametrhshs_window.tree.pack(fill="both", expand=1)
    emfanish_katametrhshs_window.focus_set()
    emfanish_katametrhshs_window.tree.bind(
        "<Button-1>",
        lambda event: on_tree_click(
            event, emfanish_katametrhshs_window.tree, main_window
        ),
    )
    emfanish_katametrhshs_window.mainloop()
    return


def on_tree_click(event, tree, main_window):
    """
    Συνάρτηση που λαμβάνει τα events clicks στο παράθυρο και ελέγχει αν ήταν
    στο κουμπί επεξεργασίας. Αν ήταν όντως, καλεί την on_edit_click().


    Args:
        event (Event Object): Αντικείμενο με τα στοιχεία του event.
        tree (Treeview Object): Το Tree του αρχικού παραθύρου.
        main_window (Tk Object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """

    region = tree.identify("region", event.x, event.y)
    col = tree.identify_column(event.x)
    row = tree.identify_row(event.y)
    if col == "#0" and region == "tree" and row:
        on_edit_click(row, tree, main_window)
    return


def on_edit_click(item_id, tree, main_window):
    """
    Συνάρτηση απόκρισης στο click στην στήλη επεξεργασία. Ανοίγει παράθυρο
    διαλόγου για επεξεργασία της ποσότητας.


    Args:
        item_id (event.y object): Παράμετρος που καθορίζει ποια γραμμή επιλέχθηκε.
        tree (Treeview object): Ο πίνακας του παραθύρου.
        main_window (Tk object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """
    edit_details_dialog = tk.Toplevel(main_window)
    edit_details_dialog.title("Επεξεργασία")
    edit_details_dialog.geometry("350x150+800+350")
    edit_details_dialog.bind(
        "<Escape>", lambda event: edit_details_dialog.destroy()
    )
    edit_details_dialog.item_pushed = tree.item(item_id, "values")
    tk.Label(
        edit_details_dialog,
        font=main_window.default_font,
        text=edit_details_dialog.item_pushed[0],
    ).pack(pady=5)
    edit_details_dialog.entry = tk.Entry(
        edit_details_dialog,
        font=main_window.default_font,
        justify="center",
    )
    edit_details_dialog.entry.insert(0, edit_details_dialog.item_pushed[1])
    edit_details_dialog.entry.pack(pady=5)

    edit_details_dialog.focus_set()
    edit_details_dialog.bind(
        "<Return>",
        lambda event: on_edit_save(edit_details_dialog, tree, main_window),
    )

    tk.Button(
        edit_details_dialog,
        font=main_window.default_font,
        text="Αποθήκευση",
        command=lambda: on_edit_save(edit_details_dialog, tree, main_window),
    ).pack(pady=5)
    edit_details_dialog.mainloop()
    return


def on_edit_save(edit_dialog, tree, main_window):
    """
    Συνάρτηση κουμπιού αποθήκευσης στην επεξεργασία ποσοτήτων αντικειμένων.
    Ελέγχει εισαγωγή θετικών ακεραίων και ανανεώνει τα δεδομένα στη ΒΔ με κλήση
    της συνάρτησης update_DB().
    """
    try:
        new_value = int(edit_dialog.entry.get())
        if new_value < 0:
            raise ValueError
    except ValueError:
        msg.showerror(
            parent=edit_dialog,
            title="Ειδοποίηση",
            message="Παρακαλώ, εισάγετε ακέραιο θετικό αριθμό για την ποσότητα.",
        )
        edit_dialog.entry.delete(0, "end")
        edit_dialog.entry.insert(0, edit_dialog.item_pushed[1])
        return
    for index in range(0, len(main_window.item_list)):
        if main_window.item_list[index][0] == edit_dialog.item_pushed[0]:
            main_window.item_list[index][1] = new_value
            fill_tree(tree, main_window.item_list)
            msg.showinfo(
                parent=edit_dialog,
                title="Ειδοποίηση",
                message="Η ποσότητα καταχωρήθηκε επιτυχώς.",
            )
            edit_dialog.destroy()
            return


def update_DB(db_state, item_list):
    """
    Βοηθητική συνάρτηση που αποθηκεύει στη ΒΔ τα δεδομένα
    της τρέχουσας καταμέτρησης.


    Args:
        db_state (int): Ύπαρξη table ή όχι.
        Αν είναι 0, δεν υπάρχει table.
        Αν δεν είναι 0, υπάρχει table.
        item_list (list): Λίστα με ("Όνομα", Ποσότητα) του κάθε αντικειμένου.

    Returns:
        None.
    """
    my_conn = dbconnect("Καταμέτρηση.db")
    c = my_conn.cursor()
    if db_state == 0:  ## Εαν δεν υπάρχει table
        sql_query = """CREATE TABLE "ΑποθηκευμένηΚαταμέτρηση" (
    	"Αντικείμενο"	TEXT [30] NOT NULL,
    	"Ποσότητα"	INTEGER NOT NULL CHECK("Ποσότητα" >= 0),
    	PRIMARY KEY("Αντικείμενο")
    );"""
        c.execute(sql_query)

        for item in item_list:
            c.execute(
                """INSERT INTO "ΑποθηκευμένηΚαταμέτρηση" VALUES (?, ?);""",
                (str(item[0]), str(item[1])),
            )
    else:  # Eάν υπάρχει, με μηδενικά ή μη δεδομένα
        for item in item_list:
            c.execute(
                """UPDATE "ΑποθηκευμένηΚαταμέτρηση"
                SET "Ποσότητα" = ?
                WHERE "Αντικείμενο" = ?;""",
                (str(item[1]), str(item[0])),
            )
    my_conn.commit()
    my_conn.close()
    return


def save_button(main_window):
    """
    Συνάρτηση για την ανταπόκριση του κουμπιού αποθήκευση καταμέτρησης του
    κυρίου παραθύρου.
    Ελέγχει κατάσταση ΒΔ, (με ή χωρίς table, table με δεδομένα ή χωρίς),
    εμφανίζει παράθυρο επιβεβαίωσης αναλόγως με την κατάσταση της καταμέτρησης
    και της ΒΔ.


    Args:
        main_window (Tk Object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """
    db_state = table_empty_check()
    if db_state == 2:
        # Αν η καταχωρημένη καταμέτρηση έχει δεδομένα προειδοποιεί
        confirmation = msg.askyesno(
            title="Αποθήκευση Καταμέτρησης",
            parent=main_window,
            message="""Θέλετε σίγουρα να αποθηκεύσετε την καταμέτρηση; 
Η προηγούμενη καταμέτρηση θα σβηστεί.""",
        )
        if not confirmation:
            msg.showerror(
                master=main_window,
                parent=main_window,
                title="Ειδοποίηση",
                message="Η αποθήκευση ακυρώθηκε από τον χρήστη.",
            )
            return
    # Έλεγχος αν η τρέχουσα καταμέτρηση δεν έχει τιμές
    zeros_only = True
    for i in range(0, len(main_window.item_list)):
        if main_window.item_list[i][1] != 0:
            zeros_only = False
    # Επιβεβαίωση αποθήκευσης καταμέτρησης με μηδενικές τιμές
    if zeros_only:
        confirmation = msg.askyesno(
            title="Αποθήκευση Μηδενικής Καταμέτρησης",
            parent=main_window,
            message="""Θέλετε σίγουρα να αποθηκεύσετε τη μηδενική καταμέτρηση;""",
        )
        if not confirmation:
            msg.showerror(
                master=main_window,
                parent=main_window,
                title="Ειδοποίηση",
                message="Η αποθήκευση ακυρώθηκε από τον χρήστη.",
            )
            return
    update_DB(db_state, main_window.item_list)
    msg.showinfo(
        title="Επιτυχής Αποθήκευση",
        parent=main_window,
        message="Η καταμέτρηση αποθηκεύτηκε επιτυχώς.",
    )
    return


def table_empty_check():
    """
    Ελέγχει τρέχουσα κατάσταση της ΒΔ.


    Returns:
        int:    0 = Δεν υπάρχει table.
                1 = Υπάρχει table, αλλά έχει μηδενικά δεδομένα.
                2 = Υπάρχει table και περιέχει δεδομένα.
    """

    my_conn = dbconnect("Καταμέτρηση.db")
    sql_query = """SELECT * FROM "ΑποθηκευμένηΚαταμέτρηση";"""
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


def load(main_window):
    """
    Ελέγχει την κατάσταση της ΒΔ και φορτώνει δεδομένα στην τρέχουσα καταμέτρηση.
    Ελέγχει αν η τρέχουσα καταμέτρηση περιέχει δεδομένα που θα χαθούν και
    ενημερώνει με το κατάλληλο pop-up.


    Args:
        main_window (Tk Object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """
    db_state = table_empty_check()
    if db_state == 0:
        msg.showerror(
            master=main_window,
            parent=main_window,
            title="Ειδοποίηση",
            message="Δεν υπάρχουν δεδομένα για φόρτωση.",
        )
        return
    # Έλεγχος αν η τρέχουσα καταμέτρηση δεν έχει τιμές
    zeros_only = True
    for i in range(0, len(main_window.item_list)):
        if main_window.item_list[i][1] != 0:
            zeros_only = False
    # Ζητάει επιβεβαίωση απαλοιφής τρέχουσας καταμέτρησης εφόσον περιέχει τιμές
    if not zeros_only:
        confirmation = msg.askyesno(
            title="Φόρτωση Καταμέτρησης",
            parent=main_window,
            message="""Θέλετε σίγουρα να φορτώσετε την αποθηκευμένη καταμέτρηση; 
Τα δεδομένα της τρέχουσας καταμέτρησης θα σβηστούν.""",
        )
        if db_state == 1:
            confirmation = msg.askyesno(
                title="Φόρτωση Μηδενικής Καταμέτρησης",
                parent=main_window,
                message="""Προσπαθείτε να φορτώσετε αποθηκευμένη μηδενική 
καταμέτρηση ενώ η τρέχουσα καταμέτρηση περιέχει δεδομένα. 
Να γίνει φόρτωση;""",
            )
        if not confirmation:
            msg.showerror(
                master=main_window,
                parent=main_window,
                title="Ειδοποίηση",
                message="Η φόρτωση ακυρώθηκε από τον χρήστη.",
            )
            return

    my_conn = dbconnect("Καταμέτρηση.db")
    sql_query = """SELECT * FROM "ΑποθηκευμένηΚαταμέτρηση";"""
    c = my_conn.cursor()
    db_contents = c.execute(sql_query).fetchall()
    for item in main_window.item_list:
        item[1] = db_contents[main_window.item_list.index(item)][1]
    my_conn.close()
    # Αν φορτώθηκε καταμέτρηση με μηδενικές τιμές
    if db_state == 1:
        msg.showinfo(
            parent=main_window,
            title="Ειδοποίηση",
            message="Φορτώθηκε μηδενική καταμέτρηση επιτυχώς.",
        )
    else:
        msg.showinfo(
            parent=main_window,
            title="Ειδοποίηση",
            message="Φορτώθηκε καταμέτρηση επιτυχώς.",
        )
        emfanish_katametrhshs(main_window)
    return


def reset_pushed(main_window):
    """
    Συνάρτηση απόκρισης στο κουμπί Μηδενισμός τρέχουσας καταμέτρησης.
    Μηδενίζει τις τιμές για όλα τα αντικείμενα της καταμέτρησης αφότου:
        Ελέγξει αν είναι ήδη μηδενική.
        Ζητήσει επιβεβαίωση από τον χρήστη.


    Args:
        main_window (Tk Object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """

    # Έλεγχος αν ο μηδενισμός είναι ανούσιος
    empty_flag = True
    for i in range(0, len(main_window.item_list)):
        if main_window.item_list[i][1] != 0:
            empty_flag = False
            break
    if empty_flag:
        msg.showinfo(
            parent=main_window,
            title="Ειδοποίηση",
            message="Η τρέχουσα καταμέτρηση είναι ήδη μηδενική.",
        )
        return

    confirmation = msg.askyesno(
        title="Μηδενισμός Καταμέτρησης",
        parent=main_window,
        message="""Θέλετε σίγουρα να μηδενίσετε την τρέχουσα καταμέτρηση; 
Τα δεδομένα της θα σβηστούν.""",
    )
    if not confirmation:
        msg.showerror(
            master=main_window,
            parent=main_window,
            title="Ειδοποίηση",
            message="Ο μηδενισμός ακυρώθηκε από τον χρήστη.",
        )
        return
    for i in range(0, len(main_window.item_list)):
        main_window.item_list[i][1] = 0
    msg.showinfo(
        parent=main_window,
        title="Ειδοποίηση",
        message="Η τρέχουσα καταμέτρηση μηδενίστηκε επιτυχώς.",
    )
    return


def terminate(main_window):
    """
    Τερματίζει το παράθυρο και την εφαρμογή.


    Args:
        main_window (Tk Object): Κύριο παράθυρο εφαρμογής.

    Returns:
        None.
    """
    main_window.destroy()


def start_app():
    # Δημιουργία ΒΔ αν δεν υπάρχει
    create_db()
    # Δημιουργία κυρίου παραθύρου
    main_window = tk.Tk()
    main_window.geometry("600x500+650+150")
    main_window.title("Πρόγραμμα Καταμέτρησης Υλικού")
    # Διατήρηση του default_font και της λίστας αντικειμένων ως πεδίο του
    # παραθύρου
    main_window.default_font = "Times 16"
    main_window.item_list = [
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
        ["1.25 Ca", 0],
    ]

    main_buttons = [
        ("Έναρξη καταμέτρησης", enarksh_katametrhshs),
        ("Εμφάνιση καταμέτρησης", emfanish_katametrhshs),
        ("Μηδενισμός τρέχουσας καταμέτρησης", reset_pushed),
        ("Αποθήκευση καταμέτρησης", save_button),
        ("Φόρτωση καταμέτρησης", load),
        ("Έξοδος", terminate),
    ]

    for label, function in main_buttons:
        tk.Button(
            main_window,
            text=label,
            font=main_window.default_font,
            command=lambda f=function: f(main_window),
            relief="groove",
            bd=10,
        ).pack(fill="x", padx=50, pady=10)

    tk.Label(
        main_window,
        text="Made by Black Baron",
        font=("Old English Text MT", 12),
        justify="left",
    ).pack(side="right")

    main_window.focus_set()
    main_window.mainloop()


if __name__ == "__main__":
    start_app()
