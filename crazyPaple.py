from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QHBoxLayout, QVBoxLayout
def right_ans():
    print("Правильна відповідь")
def wrong_ans():
    print("Неправильна відповідь")
app = QApplication([])

main_win = QWidget()
main_win.resize(500,500)
main_win.show()

btn1 = QRadioButton("2005")
btn1.clicked.connect(wrong_ans)
btn2 = QRadioButton("2022")
btn2.clicked.connect(right_ans)
btn3 = QRadioButton("2023")
btn4 = QRadioButton("2024")

layout_main = QVBoxLayout()
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
text = QLabel("В якому році безіменний герой світу під найменуванням(відомим мрекрасним імям НАЗАРІЙ ) зустрівся зі мною")
layout_main.addWidget(text, alignment=Qt.AlignCenter)
main_win.setLayout(layout_main)
layout_h1.addWidget(btn1)
layout_h1.addWidget(btn2)

layout_h2.addWidget(btn3)
layout_h2.addWidget(btn4)
layout_main.addLayout(layout_h1)
layout_main.addLayout(layout_h2)

main_win.show()
app.exec_()