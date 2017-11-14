#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
import BooleanSearch, Indexation, Vectorial
repertory = ""

class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(752, 436)
        font = QtGui.QFont()
        font.setPointSize(15)
        Form.setFont(font)
        Form.setAutoFillBackground(False)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 261, 31))
        self.label_2.setObjectName("label_2")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(36, 249, 671, 42))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 60, 207, 68))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_2)

        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(179, 139, 361, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 322, 661, 68))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 2)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Form)
        self.radioButton_2.clicked.connect(self.label.show)
        self.radioButton_2.clicked.connect(self.comboBox.show)
        self.radioButton.clicked.connect(self.comboBox.hide)
        self.radioButton.clicked.connect(self.label.hide)
        self.pushButton.clicked.connect(self.label_3.show)
        self.pushButton.clicked.connect(self.label_4.show)
        self.pushButton.clicked.connect(self.label_5.show)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.comboBox.hide()
        self.label.hide()

        self.lineEdit.setDisabled(True)
        self.pushButton.setDisabled(True)

        self.comboBox.addItem('Inner.Product')
        self.comboBox.addItem('Dice.Coef')
        self.comboBox.addItem('Cosinus.Mesure')
        self.comboBox.addItem('Jaccard.Mesure')

        self.pushButton_2.clicked.connect(self.vectorialSearch)
        self.pushButton.clicked.connect(self.methods)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search Engine"))
        self.label_2.setText(_translate("Form", "Just type your query here..."))
        self.pushButton.setText(_translate("Form", "Search"))
        self.pushButton_2.setText(_translate("Form", "..."))
        self.radioButton.setText(_translate("Form", "Boolean Search"))
        self.radioButton_2.setText(_translate("Form", "Vectorial Search"))
        self.label.setText(_translate("Form", "Choose the method"))
        self.label_3.setText(_translate("Form", "Result"))
        self.label_4.setText(_translate("Form", "Result"))
        self.label_5.setText(_translate("Form", "Pertinences"))


    def vectorialSearch(self):
        global repertory
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setDisabled(False)
        self.pushButton.setDisabled(False)
        repertory = directory

    def methods(self):
        global repertory
        query = str(self.lineEdit.text())
        dirrr = str(repertory)+"/"

        if self.radioButton_2.isChecked():
            vectorial = Vectorial.Vectorial(str(dirrr), query)

            choice = self.comboBox.currentText()
            result = []
            if choice == "Inner.Product":
                result = vectorial.innerProduct()
            elif choice == "Dice.Coef":
                result = vectorial.diceCoef()
            elif choice == "Cosinus.Mesure":
                result = vectorial.cosinusMesure()
            else:
                result = vectorial.jaccardMesure()

            self.label_4.setText("Document: "+result[0][0]+" / RSV: "+str(result[0][1]))
            toString = [res[0]+", "+str(res[1]) for res in result]
            toString = " > ".join(toString)
            self.label_5.setText("All docs: "+toString)


        if self.radioButton.isChecked():
            self.label_5.hide()
            result = []
            index = Indexation.Indexation(False)
            result = index.booleanSearch(dirrr, query)
            self.label_4.setText((" & ".join(result)))


    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

