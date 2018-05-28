import sys
from random import randint
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QPushButton,QLineEdit 
    ,QMessageBox)
from PyQt5.QtCore import pyqtSlot
 
def gen_rand_choice():
    return(randint(1,3))

class App(QWidget): 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Rock Paper Scissors')
        self.setGeometry(10, 10, 440, 280)
        
        #Creating Rock paper Scissors Label
        label1 = QLabel('Scissors(1), Rock(2) and Paper(3)?', self)
        label1.move(50,50)

        #Text Filed TO enter Choice
        self.textbox = QLineEdit(self)
        self.textbox.move(260, 47)

        #'Enter' Button
        Ent_btn = QPushButton('ENTER', self)
        Ent_btn.move(70,80) 
        Ent_btn.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        player=int(self.textbox.text())
        comp=gen_rand_choice()
        if(player==comp):
            temp=dic[player]+' vs '+ dic[comp] +'\n Match Draw'
        elif(player==1 and comp == 3):
            temp=dic[player]+' vs '+ dic[comp] +'\n PLAYER WON'
        elif(player==2 and comp == 1):
            temp=dic[player]+' vs '+ dic[comp] +'\n PLAYER WON'
        elif(player==3 and comp == 2):
            temp=dic[player]+' vs '+ dic[comp] +'\n PLAYER WON'
        else:
            temp=dic[player]+' vs '+ dic[comp] +'\n COMPUTER WIN'

        QMessageBox.question(self,'Result',temp, QMessageBox.Retry,QMessageBox.Retry)
        self.textbox.setText("")
        
if __name__ == '__main__':
    dic={1:"Scissors",2:'Rock',3:'Paper'}
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
