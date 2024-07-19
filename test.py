from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from random import *

def check_win():
    lable.setText("Переможець")
    winner.setText(str(randint(1,100)))

    



app=QApplication([])
win=QWidget()

win.setWindowTitle("PyQt5")
win.resize(500,300)

lable=QLabel("Нажми щоб дізнатися переможця")
winner=QLabel("?")
button=QPushButton("Нажми")

styleSheet=("font-size:30px;color:#13EF10")



lable.setStyleSheet(styleSheet)
winner.setStyleSheet(styleSheet)

col=QVBoxLayout()

col.addWidget(lable,alignment=Qt.AlignCenter)
col.addWidget(winner,alignment=Qt.AlignCenter)
col.addWidget(button,alignment=Qt.AlignCenter)

button.clicked.connect(check_win)

win.setLayout(col)
win.show()
app.exec()

