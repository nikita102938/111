# Form implementation generated from reading ui file 'mainadd.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Addd(object):
    def setupUi(self, Addd):
        Addd.setObjectName("Addd")
        Addd.resize(625, 353)
        Addd.setMinimumSize(QtCore.QSize(625, 353))
        Addd.setMaximumSize(QtCore.QSize(625, 353))
        Addd.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color: black;\n"
"}\n"
"\n"
"QFormLayout {\n"
"    border: 1px solid black;\n"
"}")
        self.label = QtWidgets.QLabel(parent=Addd)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.label.setStyleSheet("QLabel {\n"
"    \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(parent=Addd)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 581, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setStyleSheet("QLabel {\n"
"    text-align: center;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setStyleSheet("QLabel {\n"
"    text-align: center;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setStyleSheet("QLabel {\n"
"    text-align: center;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setStyleSheet("QLabel {\n"
"    text-align: center;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_5)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setStyleSheet("QLabel {\n"
"    text-align: center;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_4)
        self.dobavit = QtWidgets.QPushButton(parent=Addd)
        self.dobavit.setGeometry(QtCore.QRect(480, 310, 120, 30))
        self.dobavit.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(187, 142, 255);\n"
"    transition: 0.5s;\n"
"}\n"
"QPushButton {\n"
"    border: 1px solid black;\n"
"    border-radius:  10px;\n"
"    transition: 0.5s;\n"
"}")
        self.dobavit.setObjectName("dobavit")
        self.error = QtWidgets.QLabel(parent=Addd)
        self.error.setGeometry(QtCore.QRect(250, 20, 360, 13))
        self.error.setStyleSheet("QLabel {    \n"
"    font: 12зч \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 41, 41);\n"
"}")
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Addd)
        QtCore.QMetaObject.connectSlotsByName(Addd)

    def retranslateUi(self, Addd):
        _translate = QtCore.QCoreApplication.translate
        Addd.setWindowTitle(_translate("Addd", "Form"))
        self.label.setText(_translate("Addd", "Добавление нового цветка"))
        self.label_2.setText(_translate("Addd", "Название цветка"))
        self.lineEdit.setText(_translate("Addd", "Не указано"))
        self.label_3.setText(_translate("Addd", "Где находится"))
        self.lineEdit_2.setText(_translate("Addd", "Не указано"))
        self.lineEdit_3.setText(_translate("Addd", "Не указано"))
        self.label_5.setText(_translate("Addd", "Отличительные черты"))
        self.lineEdit_4.setText(_translate("Addd", "Не указано"))
        self.label_6.setText(_translate("Addd", "Поливать раз во сколько дней"))
        self.lineEdit_5.setText(_translate("Addd", "1"))
        self.label_4.setText(_translate("Addd", "Необходимый объем воды"))
        self.dobavit.setText(_translate("Addd", "Отправить  ->"))
