import menu
import lista
from PyQt5 import QtCore, QtGui, QtWidgets


menu.Ui_Dialog
lista.Ui_MainWindow

def menuinic():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = menu.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()


def listainic():

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = lista.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec_()




menuinic()
listainic()

