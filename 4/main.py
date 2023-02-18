import sys
import random
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

app = QApplication(sys.argv)
loder = QUiLoader()
main_window = loder.load("C:/Users/home/Desktop/python class/Assignment 19/4/mainwindow.ui")
main_window.show()
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num = ["1","2","3","4","5","6","7","8","9","0"]
op = ["*","/","+","-","!","@","#","$","%","^","&","(",")"]
password = []
f = 0

def pas():
    global f

    main_window.password.setText("")
    f = 0
    if main_window.standard.isChecked():
        d = 7
    if main_window.extra.isChecked():
        d = 9
    if main_window.super_2.isChecked():
        d = 11

    while f <= d:
        a = random.randint(0, 4)
        if a == 1:
            m = random.choice(abc)
            o_pas = main_window.password.text()
            n_pas = o_pas + m
            main_window.password.setText(n_pas)
            f+=1
        
        if a == 2:
            m = random.choice(ABC)
            o_pas = main_window.password.text()
            n_pas = o_pas + m
            main_window.password.setText(n_pas)
            f+=1
        
        if a == 3:
            m = random.choice(num)
            o_pas = main_window.password.text()
            n_pas = o_pas + m
            main_window.password.setText(n_pas)
            f+=1
      
        if a == 4:
            m = random.choice(op)
            o_pas = main_window.password.text()
            n_pas = o_pas + m
            main_window.password.setText(n_pas)
            f+=1

main_window.standard.toggled.connect(pas)
main_window.extra.toggled.connect(pas)
main_window.super_2.toggled.connect(pas)

app.exec_()