import sys
import random
from functools import partial
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

app = QApplication(sys.argv)
rps = ["rock", "paper", "scissor"]
player_s = 0
compater_s = 0

loder = QUiLoader()
main_window = loder.load("C:/Users/home/Desktop/python class/Assignment 19/2/mainwindow.ui")
main_window.show()

def play(player_rps):
    global player_s
    global compater_s

    main_window.y_g.setText(player_rps)
    compater_rps = random.choice(rps)
    main_window.c_g.setText(compater_rps)
    if compater_rps == player_rps:
        main_window.text.setText("Draw!")
    elif compater_rps == "rock" and player_rps == "scissor" or compater_rps == "paper" and player_rps == "rock" or compater_rps == "scissor" and player_rps == "paper":
        main_window.text.setText("compater win!")
        compater_s += 1
        main_window.c_s.setText(str(compater_s))
    else:
        main_window.text.setText("player win!")
        player_s += 1
        main_window.y_s.setText(str(player_s))


main_window.rock.clicked.connect(partial(play,"rock"))
main_window.paper.clicked.connect(partial(play,"paper"))
main_window.scissor.clicked.connect(partial(play,"scissor"))

app.exec_()