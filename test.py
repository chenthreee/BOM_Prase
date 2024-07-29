# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QTextEdit, QVBoxLayout, QWidget)

import TextEdit
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(522, 446)
        Dialog.setAcceptDrops(True)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 40, 219, 301))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_end_row = QLineEdit(self.layoutWidget)
        self.lineEdit_end_row.setObjectName(u"lineEdit_end_row")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_end_row)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_part_code = QLineEdit(self.layoutWidget)
        self.lineEdit_part_code.setObjectName(u"lineEdit_part_code")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_part_code)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_manufacturer = QLineEdit(self.layoutWidget)
        self.lineEdit_manufacturer.setObjectName(u"lineEdit_manufacturer")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_manufacturer)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_designator = QLineEdit(self.layoutWidget)
        self.lineEdit_designator.setObjectName(u"lineEdit_designator")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_designator)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_quantity = QLineEdit(self.layoutWidget)
        self.lineEdit_quantity.setObjectName(u"lineEdit_quantity")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_quantity)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_footprint = QLineEdit(self.layoutWidget)
        self.lineEdit_footprint.setObjectName(u"lineEdit_footprint")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_footprint)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_description = QLineEdit(self.layoutWidget)
        self.lineEdit_description.setObjectName(u"lineEdit_description")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_description)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.pushButton)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_initial_row = QLineEdit(self.layoutWidget)
        self.lineEdit_initial_row.setObjectName(u"lineEdit_initial_row")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_initial_row)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_customer_code = QLineEdit(self.layoutWidget)
        self.lineEdit_customer_code.setObjectName(u"lineEdit_customer_code")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_customer_code)

        self.BOMInput_textEdit = TextEdit.myTextEdit(Dialog)
        self.BOMInput_textEdit.setObjectName(u"BOMInput_textEdit")
        self.BOMInput_textEdit.setGeometry(QRect(280, 270, 104, 64))
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(280, 250, 81, 16))
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(390, 250, 66, 12))
        self.K3Input_textEdit = TextEdit.myTextEdit(Dialog)
        self.K3Input_textEdit.setObjectName(u"K3Input_textEdit")
        self.K3Input_textEdit.setGeometry(QRect(390, 270, 104, 64))
        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(280, 130, 212, 106))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_alternative_part_code_1 = QLineEdit(self.layoutWidget1)
        self.lineEdit_alternative_part_code_1.setObjectName(u"lineEdit_alternative_part_code_1")

        self.verticalLayout_2.addWidget(self.lineEdit_alternative_part_code_1)

        self.lineEdit_alternative_manufacturer_1 = QLineEdit(self.layoutWidget1)
        self.lineEdit_alternative_manufacturer_1.setObjectName(u"lineEdit_alternative_manufacturer_1")

        self.verticalLayout_2.addWidget(self.lineEdit_alternative_manufacturer_1)

        self.lineEdit_alternative_part_code_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_alternative_part_code_2.setObjectName(u"lineEdit_alternative_part_code_2")

        self.verticalLayout_2.addWidget(self.lineEdit_alternative_part_code_2)

        self.lineEdit_alternative_manufacturer_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_alternative_manufacturer_2.setObjectName(u"lineEdit_alternative_manufacturer_2")

        self.verticalLayout_2.addWidget(self.lineEdit_alternative_manufacturer_2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        QWidget.setTabOrder(self.lineEdit_customer_code, self.lineEdit_initial_row)
        QWidget.setTabOrder(self.lineEdit_initial_row, self.lineEdit_end_row)
        QWidget.setTabOrder(self.lineEdit_end_row, self.lineEdit_part_code)
        QWidget.setTabOrder(self.lineEdit_part_code, self.lineEdit_manufacturer)
        QWidget.setTabOrder(self.lineEdit_manufacturer, self.lineEdit_designator)
        QWidget.setTabOrder(self.lineEdit_designator, self.lineEdit_quantity)
        QWidget.setTabOrder(self.lineEdit_quantity, self.lineEdit_footprint)
        QWidget.setTabOrder(self.lineEdit_footprint, self.lineEdit_description)
        QWidget.setTabOrder(self.lineEdit_description, self.pushButton)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.on_click)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi
    def on_click(self):
        print("hello")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u539f\u59cbBOM\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7ed3\u675f\u884c\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6599\u53f7\u5217\u53f7", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5382\u5546\u5217\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u4f4d\u53f7\u5217\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf\u5217\u53f7", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5c01\u88c5\u5217\u53f7", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u89c4\u683c\u63cf\u8ff0\u5217\u53f7", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u63d0\u4ea4", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8d77\u59cb\u884c\u53f7", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u5ba2\u6237\u7f16\u7801", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u539f\u59cbBOM\u62d6\u653e", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"K3\u62d6\u653e", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u66ff\u4ee31\u6599\u53f7\u5217", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u66ff\u4ee31\u5382\u5546\u5217", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u66ff\u4ee32\u6599\u53f7\u5217", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u66ff\u4ee32\u5382\u5546\u5217", None))
    # retranslateUi
