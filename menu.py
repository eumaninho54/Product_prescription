# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import lista

class Ui_Dialog(object):

    def clean_program(self):
        self.Name.setText(None)
        self.description.setText(None)
        self.Value.setText(None)


    def close_program(self):
        pass

        
 
    # Chech Infs
    def chechField(self):
        text_name = ""
        text_desc = ""
        text_value = ""


        def lermensagem(msg):
                self.error.show()
                self.label_2.setText(msg)

        if not self.Name.text():
            text_name = 'Name Empty'
        else:
            text_name = ''
        if not self.description.text():
            text_desc = 'Description Empty'
        else:
            text_desc = ''
        if not self.Value.text():
            text_value = 'Value Empty'
        else:
            text_value = ''
        
        if text_name + text_desc + text_value != '':
            text = 'Empty Space'
            lermensagem(text)
            self.label_2.setGeometry(QtCore.QRect(185, 0, 350, 21))
        else:
            if not self.checkBox.isChecked():
                
                text = 'Successful registration'
                file = open('infs_note.txt', 'a')
                file.write(self.Name.text()+ '\n')
                file.write(self.description.text()+ '\n')
                file.write(self.Value.text()+'\n')
                self.label_2.setGeometry(QtCore.QRect(155, 0, 350, 21))
                app = QtWidgets.QApplication
                app.closeAllWindows()
                
                
            elif self.checkBox.isChecked():
                text = 'Successful registration'
                file = open('infs_note.txt', 'a')
                file.write(self.Name.text()+ '\n')
                file.write(self.description.text()+ '\n')
                file.write(self.Value.text()+'\n')
                text = text + '| Waiting for additional information'
                self.label_2.setGeometry(QtCore.QRect(90, 0, 350, 21))
        lermensagem(text)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(642, 459)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-50, -40, 791, 561))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Name = QtWidgets.QLineEdit(Dialog)
        self.Name.setGeometry(QtCore.QRect(250, 190, 251, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Name.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Muli Light")
        font.setPointSize(10)
        self.Name.setFont(font)
        self.Name.setTabletTracking(False)
        self.Name.setStyleSheet("QLineEdit {    \n"
"    border-color: rgb(85, 0, 255);\n"
"    background-color: rgb(222, 222, 222);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"    border:2px solid rgb(75, 0, 245);\n"
"}\n"
"QLineEdit:focus {\n"
"    border:2px solid rgb(45, 0, 205);\n"
"\n"
"}")
        self.Name.setText("")
        self.Name.setObjectName("Name")
        self.description = QtWidgets.QLineEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(250, 250, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Muli Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.description.setFont(font)
        self.description.setTabletTracking(False)
        self.description.setAcceptDrops(True)
        self.description.setStyleSheet("QLineEdit {    \n"
"    border-color: rgb(85, 0, 255);\n"
"    background-color: rgb(222, 222, 222);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"    border:2px solid rgb(75, 0, 245);\n"
"}\n"
"QLineEdit:focus {\n"
"    border:2px solid rgb(45, 0, 205);\n"
"\n"
"}")
        self.description.setText("")
        self.description.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.description.setClearButtonEnabled(False)
        self.description.setObjectName("description")
        self.Value = QtWidgets.QLineEdit(Dialog)
        self.Value.setGeometry(QtCore.QRect(250, 310, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Muli Light")
        font.setPointSize(10)
        self.Value.setFont(font)
        self.Value.setStyleSheet("QLineEdit {    \n"
"    border-color: rgb(85, 0, 255);\n"
"    background-color: rgb(222, 222, 222);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"    border:2px solid rgb(75, 0, 245);\n"
"}\n"
"QLineEdit:focus {\n"
"    border:2px solid rgb(45, 0, 205);\n"
"\n"
"}")
        self.Value.setObjectName("Value")
        self.descimage = QtWidgets.QLabel(Dialog)
        self.descimage.setGeometry(QtCore.QRect(170, 240, 81, 41))
        self.descimage.setStyleSheet("image: url(:/img/nome_00000/desc_1_00000.png);")
        self.descimage.setText("")
        self.descimage.setObjectName("descimage")
        self.nomeimg = QtWidgets.QLabel(Dialog)
        self.nomeimg.setGeometry(QtCore.QRect(170, 180, 81, 41))
        self.nomeimg.setStyleSheet("image: url(:/img/nome_1_00000.png);")
        self.nomeimg.setText("")
        self.nomeimg.setObjectName("nomeimg")
        self.valorimage = QtWidgets.QLabel(Dialog)
        self.valorimage.setGeometry(QtCore.QRect(170, 310, 81, 41))
        self.valorimage.setStyleSheet("image: url(:/img/nome_1_00001_00000.png);")
        self.valorimage.setText("")
        self.valorimage.setObjectName("valorimage")
        self.logotexto = QtWidgets.QLabel(Dialog)
        self.logotexto.setGeometry(QtCore.QRect(0, 10, 641, 141))
        self.logotexto.setStyleSheet("image: url(:/img/Capturar_00000.png);")
        self.logotexto.setText("")
        self.logotexto.setObjectName("logotexto")
        self.addbutton = QtWidgets.QPushButton(Dialog)
        self.addbutton.setGeometry(QtCore.QRect(250, 380, 75, 23))
        self.addbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(83, 83, 83);")
        self.addbutton.setObjectName("addbutton")
        self.cleanbutton = QtWidgets.QPushButton(Dialog)
        self.cleanbutton.setGeometry(QtCore.QRect(370, 380, 75, 23))
        self.cleanbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(83, 83, 83);")
        self.cleanbutton.setObjectName("cleanbutton")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(500, 380, 81, 20))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.error = QtWidgets.QFrame(Dialog)
        self.error.setGeometry(QtCore.QRect(110, 10, 431, 20))
        self.error.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius: 5px")
        self.error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error.setObjectName("error")
        self.label_2 = QtWidgets.QLabel(self.error)
        self.label_2.setGeometry(QtCore.QRect(195, 0, 350, 21))
        self.label_2.setObjectName("label_2")
        self.xcancel = QtWidgets.QPushButton(self.error)
        self.xcancel.setGeometry(QtCore.QRect(400, 0, 31, 21))
        self.xcancel.setStyleSheet("QPushButton {\n"
"    image: url(:/img/3052270_letter_lowercase_red_x_icon.png);\n"
"    botder-radius: 5px;\n"
"    \n"
"    background-color: rgb(255, 139, 189);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.xcancel.setText("")
        self.xcancel.setObjectName("xcancel")
        self.label.raise_()
        self.Name.raise_()
        self.description.raise_()
        self.Value.raise_()
        self.descimage.raise_()
        self.nomeimg.raise_()
        self.valorimage.raise_()
        self.addbutton.raise_()
        self.cleanbutton.raise_()
        self.checkBox.raise_()
        self.logotexto.raise_()
        self.error.raise_()

        # Functions
        

        # closed error image
        self.xcancel.clicked.connect(lambda: self.error.hide())

        self.error.hide()

        self.addbutton.clicked.connect(self.chechField)

        self.cleanbutton.clicked.connect(self.clean_program)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "@ymaninho54"))
        Dialog.setWindowIcon(QtGui.QIcon('logowindow.png'))
        self.Name.setPlaceholderText(_translate("Dialog", "Name "))
        self.description.setPlaceholderText(_translate("Dialog", "Description "))
        self.Value.setPlaceholderText(_translate("Dialog", "Value "))
        self.addbutton.setText(_translate("Dialog", "Add"))
        self.cleanbutton.setText(_translate("Dialog", "Viwer"))
        self.checkBox.setText(_translate("Dialog", "keep adding"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Error</span></p></body></html>"))
        

from imgs import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
