import sys
import random
from functools import partial
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        numbers = []
        n = 0

        while len(numbers) <= 16:
            r = random.randint(1, 16)

            if r in numbers:
                r = random.randint(1, 16)
                
            else:
                numbers.append(r)

            if len(numbers) == 16:
                break
        
        self.buttons = [[self.ui.btn_1, self.ui.btn_2,self.ui.btn_3,self.ui.btn_4],
                        [self.ui.btn_5,self.ui.btn_6,self.ui.btn_7,self.ui.btn_8],
                        [self.ui.btn_9,self.ui.btn_10,self.ui.btn_11,self.ui.btn_12],
                        [self.ui.btn_13,self.ui.btn_14,self.ui.btn_15,self.ui.btn_16]]
        
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].setText(str(numbers[n]))
                self.buttons[i][j].clicked.connect(partial(self.play,i,j))
                if self.buttons[i] [j].text() == "16":
                    self.buttons[i][j].setVisible(False)
                    self.e_i = i
                    self.e_j = j            
                if n <= 16:
                    n+=1
                if n == 16:
                    break   

    def play(self,i,j):
        if (i == self.e_i and (j == self.e_j - 1 or j == self.e_j + 1)) or\
           (j == self.e_j and (i == self.e_i - 1 or i == self.e_i + 1)):
           
            self.buttons[self.e_i][self.e_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")

            self.buttons[self.e_i][self.e_j].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.e_i = i 
            self.e_j = j
        
        self.Check_win()
        if self.Check_win() == True:
            msg_box = QMessageBox()
            msg_box.setText("You winer")
            msg_box.exec_()

    def Check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):

                if int(self.buttons[i][j].text()) != index:
                    return False
                    index += 1

            else:
                return True

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec_()