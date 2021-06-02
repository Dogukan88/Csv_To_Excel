import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pandas as pd
from pyexcelerate import Workbook

from FileBrowser import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):

     def __init__(self):
         super(myApp, self). __init__()
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)
         self.ui.pushButton.clicked.connect(self.openFileNameDialog)



         
     def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            dataset = pd.read_csv(fileName)
            df_to_excel(dataset,fileName, sheet_name="Sheet 1")
            


def df_to_excel(df, path, sheet_name='Sheet 1'):
    data = [df.columns.tolist(), ] + df.values.tolist()
    wb = Workbook()
    wb.new_sheet(sheet_name, data=data)
    wb.save(path)    


   

def app():

    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())



app()

