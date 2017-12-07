from PyQt5 import QtCore, QtGui, QtWidgets
import Indexation
import functools

repertory = ""

class SearchSpaceBool(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 500)
        Form.setGeometry(300, 150, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #0C2444;")
        self.closeWindow = Form.close
        
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(280, 35, 500, 30))
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet("font-weight:500;\n"
"font-size:20px")
        self.labelTitle.setText("Recherche Booléenne")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 67, 17))
        self.label_2.setObjectName("label_2")

        pixmap = QtGui.QPixmap('MonChef-logo.png').scaledToWidth(90)
        self.label_2.setPixmap(pixmap)
        self.label_2.setGeometry(QtCore.QRect(680, 15, 100, 30))

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label.mousePressEvent = self.retour

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 450, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFrame(False)
        self.lineEdit.setStyleSheet("background-color: #fff;border: 1px solid #0C2444;border-left:0px")
        self.lineEdit.setPlaceholderText('Exemple: Python ou Linux et ( Libre ou Puissant ) ')
        self.lineEdit.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(Form) 
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(600, 100, 50, 30))
        self.pushButton_2.setStyleSheet("background-color: #0C2444;\n"
"color:#fff;font-size:14px;border-top-right-radius: 15px;border-bottom-right-radius: 15px;")
        self.pushButton_2.clicked.connect(self.getDir)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 180, 500, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-weight:500;\n"
"font-size:17px")
        self.label_3.hide()

        self.label2Hide = QtWidgets.QLabel(Form)
        self.label2Hide.setGeometry(QtCore.QRect(110, 250, 600, 30))
        self.label2Hide.setObjectName("label2Hide")
        self.label2Hide.setStyleSheet("font-weight:200;\n"
"font-size:15px")
        self.label2Hide.setText("NOTE: Ajouter votre collection, taper votre requête et cliquer sur l’icône de recherche. ")     


        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background-color: #fff;\n"
"border-top-left-radius: 15px;border-bottom-left-radius: 15px;border: 1px solid #0C2444;border-right:0px")
        pixmap2 = QtGui.QPixmap('search.png').scaledToWidth(18)
        self.label_4.setPixmap(pixmap2)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 30, 30))
        self.label_4.setDisabled(True)
        self.label_4.mousePressEvent = self.booleanSearch
        self.lineEdit.returnPressed.connect(self.booleanSearch)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(180, 230, 450, 200))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color:#f7f7f7;font-size:22px;font-weight:500;")
        self.listWidget.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Les résultats de la recherche dans l'ordre de pertinence:"))
        self.pushButton_2.setText(_translate("Form", "..."))
        self.label_4.setText(_translate("Form", ""))
        

    def retour(self, event):
        self.closeWindow()

    def getDir(self):
        global repertory
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setDisabled(False)
        self.label_4.setDisabled(False)
        repertory = directory
        print(repertory)

    

    def booleanSearch(self, event = False):
        global repertory
        self.label_3.show()
        self.label2Hide.hide()
        query = str(self.lineEdit.text().lower())
        dirrr = str(repertory)+"/"
        result = []
        index = Indexation.Indexation(False)
        result = index.booleanSearch(dirrr, query)
        sizeResult = len(result)

        for i, res in zip(range(sizeResult),result):
            self.listWidget.addItem(res)
        self.listWidget.show()
        self.listWidget.itemClicked.connect(self.openFile)

        
    def openFile(self, item):
        import os
        file = repertory+"/"+item.text()
        os.system("subl "+file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SearchSpaceBool()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

