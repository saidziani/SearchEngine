from PyQt5 import QtCore, QtGui, QtWidgets
import SearchSpaceBool, SearchSpaceVec

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 500)
        Form.setGeometry(300, 150, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #fff;\n"
"color: #0C2444;")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.hideWindow = Form.hide

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 330, 150, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 330, 150, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 330, 21, 51))

        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #bdbdbd;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        pixmap = QtGui.QPixmap('se.png').scaledToWidth(155)
        self.label_4.setPixmap(pixmap)
        self.label_4.setGeometry(QtCore.QRect(313, 100, 220, 200))

        self.label.mousePressEvent = self.openBoolean
        self.label_2.mousePressEvent = self.openVectorial

        self.label_3.setStyleSheet("font-weight:100")
        self.label_2.setStyleSheet("font-weight:600")
        self.label.setStyleSheet("font-weight:600")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_5.setObjectName("label_5")

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label_5.setPixmap(pixmap1)
        self.label_5.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label_5.mousePressEvent = self.retour

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef."))
        self.label.setText(_translate("Form", "Recherche\nBooléenne"))
        self.label_2.setText(_translate("Form", "Recherche\nVectorielle"))
        self.label_3.setText(_translate("Form", " |"))
        self.label_5.setText(_translate("Form", ""))


    def openBoolean(self, event):
        print('Boolean')
        self.window = QtWidgets.QMainWindow()
        self.ui = SearchSpaceBool.SearchSpaceBool()
        self.ui.setupUi(self.window)
        self.window.show()


    def openVectorial(self, event):
        print('ARABE')
        self.window = QtWidgets.QWidget()
        self.ui = SearchSpaceVec.SearchSpaceVec()
        self.ui.setupUi(self.window)
        self.window.show()

    def retour(self, event):
        print('BACK')
        Form.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
