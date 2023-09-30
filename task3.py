from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])
my_win = QWidget()
my_win.resize(500,500)
title = QLabel("Натисни щоб дізнатись переможця!")
title1 = QLabel("?")
btn = QPushButton("Generate number")

line = QVBoxLayout()
line.addWidget(title, alignment=Qt.AlignCenter)
line.addWidget(title1, alignment=Qt.AlignCenter)
line.addWidget(btn)

my_win.setLayout(line)
my_win.show()
app.exec_()