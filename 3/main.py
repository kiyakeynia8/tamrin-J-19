import sys
import random
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

app = QApplication(sys.argv)
loder = QUiLoader()
main_window = loder.load("C:/Users/home/Desktop/python class/Assignment 19/3/mainwindow.ui")
main_window.show()
random_number = random.randint(0, 100)

def play():
    global random_number

    number = main_window.text.text()
    number = int(number)
    if number == random_number:
        main_window.check_t.setText("you win")
    elif number > random_number:
        main_window.check_t.setText("come down")
    else:
        main_window.check_t.setText("go up")

main_window.check.clicked.connect(play)

app.exec_()