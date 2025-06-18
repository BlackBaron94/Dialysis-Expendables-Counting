<a id="readme-top"></a>
<div align="center">
  <h1 align="center">Dialysis Expendables Counting Project</h1>

  <p align="center">
    Εφαρμογή που επιτρέπει την καταχώρηση αναλωσίμων αιμοκάθαρσης κατά τη μηνιαία καταμέτρησή τους! 
    </p>
</div>


## Περιεχόμενα
  - [Περιγραφή Project](#περιγραφή-project)
  - [Οδηγίες Εγκατάστασης](#οδηγίες-εγκατάστασης)
  - [Λειτουργίες](#λειτουργίες)
  - [Πλαίσιο Λειτουργίας](#πλαίσιο-λειτουργίας)
  - [Χρήση](#χρήση)
  - [Μελλοντικές Προσθήκες](#μελλοντικές-προσθήκες)
  - [Επικοινωνία](#επικοινωνία)
  - [License](#license)

## Περιγραφή Project
Πρόγραμμα για καταμέτρηση υλικού αιμοκάθαρσης. Το πρόγραμμα καταμετρεί φίλτρα αιμοκάθαρσης, διαλύματα 
αιμοκάθαρσης και αναλώσιμα όπως γραμμές, γραμμές OHDF αιμοκάθαρσης και φύσιγγες διττανθρακικών. Παρέχει πλήρη
ανατροφοδότηση καταχωρήσεσων για να ανταποκρίνεται στις ανάγκες της δουλειάς ακόμα κι όταν αυτή διακόπτεται!
Επιπλέον, οι καταμετρήσεις μπορούν να αποθηκεύονται και να φορτώνονται

### Τεχνολογίες και βιβλιοθήκες που χρησιμοποιήθηκαν

* [![Python][python.org]][Python-url]
* [![tkinter][tkinter.python]][tkinter-url]
* [![SQLite3][sqlite3.python]][sqlite3-url]
* [<img src="https://avatars.githubusercontent.com/u/1215332?v=4" alt="PyInstaller_Logo" width="40" />][PyInstaller-url] PyInstaller

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Οδηγίες Εγκατάστασης


- Executable

Το onefile .exe είναι fully portable και δεν υπάρχουν προαπαιτούμενα. Κάνοντας clone το repo είστε έτοιμοι!

1. Clone του repo
   ```sh
   git clone https://github.com/BlackBaron94/DialysisExpendablesCounting.git
   ```

- Κώδικας

Για να τρέξει το αρχείο .py χρειάζεται εγκατεστημένη έκδοση 3. Python καθώς και το πακέτο βιβλιοθήκης tkinter

2. Έλεγχος εγκατεστημένης έκδοσης Python
   ```sh
   python --version
   ```
3. Έλεγχος εγκατάστασης pip
   ```sh
   pip -v
   ```

4. Εγκατάταση πακέτου tkinter
   ```sh
   pip install tk
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Λειτουργίες


1. **Έναρξη καταμέτρησης**


Ανοίγει παράθυρο διαλόγου με προκαθορισμένες επιλογές αναλωσίμων για καταχώρηση με click στο ανάλογο κουμπί.

---

2. **Εμφάνιση καταμέτρησης**


Ανοίγει παράθυρο που παρουσιάζει την τρέχουσα καταμέτρηση σε πίνακα.

---

3. **Μηδενισμός τρέχουσας καταμέτρησης**


Μηδενίζει την τρέχουσα καταμέτρηση.

---

4. **Αποθήκευση καταμέτρησης**


Αποθηκεύει την τρέχουσα καταμέτρηση σε βάση δεδομένων. 

---

5. **Φόρτωση καταμέτρησης**


Μηδενίζει την τρέχουσα καταμέτρηση και φορτώνει την αποθηκευμένη καταμέτρηση στη βάση δεδομένων.

---

6. **Έξοδος**


Τερματίζει το πρόγραμμα.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Πλαίσιο Λειτουργίας

Η εφαρμογή δημιουργήθηκε με σκοπό την καταμέτρηση αναλωσίμων ανά ημέρα αιμοκάθαρσης. Ο σκοπός της καταμέτρησης
αυτής στο πλαίσιο της μονάδας αιμοκάθαρσης είναι ο καθορισμός αναγκών παραγγελιών αποθήκης. 

Για κάθε αιμοκάθαρση απαιτούνται:
- Γραμμή αιμοκάθαρσης
- Φύσιγγα διττανθρακικών
- Φίλτρο
- Διάλυμα αιμοκάθαρσης

Εάν το φίλτρο που χρησιμοποιείται είναι τύπου high-flux, χρειάζεται επιπλέον γραμμή online (OHDF) και σε κάποιες 
περιπτώσεις δεύτερο διάλλυμα αιμοκάθαρσης.

Το πρόγραμμα προσθέτει με κάθε φίλτρο μία γραμμή αιμοκάθαρσης και μία φύσιγγα, ενώ αν είναι τύπου High-Flux, προσθέτει
και την γραμμή online (OHDF). 

> High-flux φίλτρα: 25H, 21H, 19H, FDY 210/180/150

Εάν η αιμοκάθαρση απαιτεί πάνω από ένα διάλυμα αιμοκάθαρσης (πχ αν είναι OHDF), αυτό προστίθεται χειροκίνητα, καθώς ο κανόνας δεν
εφαρμόζεται καθολικά.

Το πρόγραμμα παρέχει ανατροφοδότηση των προσφάτως εισαχθέντων φίλτρων με σκοπό να διευκολύνει τον χρήστη για την
περίπτωση που η καταμέτρηση διακόπτεται λόγω κάποιου επείγοντως ιατρικού περιστατικού.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Χρήση

Υπάρχει διαθέσιμο video demo [εδώ](https://drive.google.com/file/d/1BmUC_56OBbTKn5Ff1qGO2_McGNij75kV/view?usp=drive_link).

Εναλλακτικά, παρακάτω φαίνονται παραδείγματα χρήσης με εικόνες.

---

> **Αυτό είναι το κύριο μενού της εφαρμογής.**

---

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Dialysis-Expendables-Counting/Main-Menu.jpg" alt="Main-Menu" width="500"/>
</div> 

<p align="center"><b> Κύριο μενού εφαρμογής. </b></p>

---

> **Ακολουθεί το παράθυρο διαλόγου καταμέτρησης πριν αυτή ξεκινήσει, και αφότου πατηθεί το κουμπί 21Η 3 φορές. Η εφαρμογή ενημερώνει τον χρήστη ποιο στοιχείο καταχωρήθηκε τελευταίο κι αν καταχωρήθηκε το ίδιο πολλές φορές, δείχνει πόσες.**

---

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Dialysis-Expendables-Counting/Counting-Window-None-Pressed.jpg" alt="Counting-Window-None-Pressed" width="500" style="display: inline-block;"/>
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Dialysis-Expendables-Counting/Counting-Window-21H-Pressed-x-3.jpg" alt="Counting-Window-21H-Pressed-x-3" width="500" style="display: inline-block;"/>
</div> 

<p align="center"><b> Παράθυρο καταμέτρησης. </b></p>

---

> **Πατώντας εμφάνιση καταμέτρησης ο χρήστης μπορεί να δει όλα τα διαθέσιμα υλικά και το πόσες φορές καταμετρήθηκαν κατά την τρέχουσα καταμέτρηση.**

---

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Dialysis-Expendables-Counting/Counting-Result.jpg" alt="Counting-Result" width="500" style="display: inline:block;"/>
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Dialysis-Expendables-Counting/Counting-Result-Edit.jpg" alt="Counting-Result-Edit" width="500" style="display: inline:block;"/>
</div> 

<p align="center"><b> Εμφάνιση και επεξεργασία καταμέτρησης. </b></p>

---

> **Εάν ο χρήστης πατήσει μηδενισμό καταμέτρησης ή φόρτωση καταμέτρησης, ζητείται επιβεβαίωση για αποφυγή μη επιθυμητής απώλειας δεδομένων τρέχουσας καταμέτρησης.**

---

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Dialysis-Expendables-Counting/Reset-Counting.jpg" alt="Reset-Counting" width="500" style="display: inline-block;"/>
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Dialysis-Expendables-Counting/Loading-Counting.jpg" alt="Loading-Counting" width="500" style="display: inline-block;"/>
</div> 

<p align="center"><b> Μηδενισμός και φόρτωση καταμέτρησης. </b> </p>

---


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Μελλοντικές Προσθήκες

- [X] Λειτουργίες αποθήκευσης και φόρτωσης καταμέτρησης.
- [ ] Απευθείας τροποποίηση δεδομένων καταμέτρησης με νούμερα.
- [ ] Τροποποίηση αναλώσιμων προς καταμέτρηση με προσθαφαίρεση φίλτρων και διαλυμάτων.
- [ ] Δυνατότητα αλλαγής τρόπου καταμέτρησης γραμμών/γραμμών OHDF/φυσιγγών διττανθρακικών.
- [ ] Διατήρηση πολλαπλών καταμετρήσεων με τίτλους (π.χ. ημερομηνία καταμέτρησης).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Επικοινωνία

Γιώργος Τσολακίδης - [Linked In: Giorgos Tsolakidis](https://www.linkedin.com/in/black-baron/) - black_baron94@hotmail.com 

Project Link: [Dialysis Expendables Counting](https://github.com/BlackBaron94/DialysisExpendablesCounting)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License


This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://python.org/
[tkinter.python]: https://img.shields.io/badge/Frontend-tkinter-blue
[tkinter-url]: https://docs.python.org/3/library/tkinter.html
[sqlite3.python]: https://img.shields.io/badge/SQLite-blue?logo=sqlite&logoColor=white
[sqlite3-url]: https://docs.python.org/3/library/sqlite3.html
[PyInstaller-url]: https://pyinstaller.org/
