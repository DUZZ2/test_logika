from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from random import *

def check_win():
    lable.setText("Переможець")
    winner.setText(str(randint(1,100)))

    



#Створення віджета підпес
app=QApplication([])
#Створення вікна
win=QWidget()
#Добавлення заголовку до вікна програми
win.setWindowTitle("PyQt5")
#Задання розмірів вікна
win.resize(500,300)

lable=QLabel("Нажми щоб дізнатися переможця")
winner=QLabel("?")
#Створення віджета кнопка
button=QPushButton("Нажми")

styleSheet=("font-size:30px;color:#13EF10")


#Створення патерну для вигляду віджетів
lable.setStyleSheet(styleSheet)
winner.setStyleSheet(styleSheet)
#Створення вертекальної лінії
col=QVBoxLayout()

#Добавлення елементів на вертекальну лінію
col.addWidget(lable,alignment=Qt.AlignCenter)
col.addWidget(winner,alignment=Qt.AlignCenter)
col.addWidget(button,alignment=Qt.AlignCenter)
#Підклучення функції до кнопки при натисканні
button.clicked.connect(check_win)
#Добавлення лінії до вікна
win.setLayout(col)
win.show()
app.exec()

