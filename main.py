import openpyxl
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("score.xlsx")
dx = df[['x']]
dy = df[['y']]
form_class = uic.loadUiType("main.ui")[0]
class MyDialog(QDialog) :
    def __init__(self) :
        QDialog.__init__(self)


        btx = QPushButton("x axis")
        bty = QPushButton("y axis")
        btt = QPushButton("Total")

        layout = QVBoxLayout()
        layout.addWidget(btx)
        layout.addWidget(bty)
        layout.addWidget(btt)
        self.setLayout(layout)
        btx.clicked.connect(self.btnXClicked)
        bty.clicked.connect(self.btnYClicked)
        btt.clicked.connect(self.btnTClicked)
    def btnXClicked(self):
        plt.plot(dx)
        plt.show()

    def btnYClicked(self):
        plt.plot(dy)
        plt.show()

    def btnTClicked(self):
        plt.plot(df)
        plt.show()



app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()