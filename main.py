from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

import json

notes = {
    "Ілля Сидорчук": {
        "текст": "Хороший хлопчик"
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

app = QApplication([])

notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')
button_note_create = QPushButton('Створити замітку') # з'являється вікно з полем "Введіть ім'я замітки"
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')
field_text = QTextEdit()

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

row_3 = QHBoxLayout()
row_4 = QHBoxLayout()

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def add_note():
    note_mane, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки:")
    if ok and note_mane != '':
        notes[note_mane] = {"текст": ""}
        list_notes.addItem(note_mane)
        print(notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file, sort_keys = True, ensure_ascii = False)
        print(notes)
    else:
        print('Замітка для збереження не вибрана!')

def note_del():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file, sort_keys = True, ensure_ascii = False)
        print(notes)
    else:
        print('Замітка для вилучення не обрана!')

button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(note_del)

with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)

notes_win.show()
app.exec_()
