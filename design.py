# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_lab2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.search_hash_res = QtWidgets.QLineEdit(self.centralwidget)
        self.search_hash_res.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.search_hash_res.setObjectName("search_hash_res")
        self.gridLayout.addWidget(self.search_hash_res, 15, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.search_btn.setObjectName("search_btn")
        self.gridLayout.addWidget(self.search_btn, 11, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 1)
        self.search_id = QtWidgets.QLineEdit(self.centralwidget)
        self.search_id.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.search_id.setObjectName("search_id")
        self.gridLayout.addWidget(self.search_id, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.filepath = QtWidgets.QLineEdit(self.centralwidget)
        self.filepath.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.filepath.setObjectName("filepath")
        self.gridLayout.addWidget(self.filepath, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.search_bin_res = QtWidgets.QLineEdit(self.centralwidget)
        self.search_bin_res.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.search_bin_res.setObjectName("search_bin_res")
        self.gridLayout.addWidget(self.search_bin_res, 13, 0, 1, 1)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.add_res = QtWidgets.QLineEdit(self.centralwidget)
        self.add_res.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.add_res.setObjectName("add_res")
        self.gridLayout.addWidget(self.add_res, 6, 0, 1, 1)
        self.add_id = QtWidgets.QLineEdit(self.centralwidget)
        self.add_id.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.add_id.setObjectName("add_id")
        self.gridLayout.addWidget(self.add_id, 4, 0, 1, 1)
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 15, 2, 1, 1)
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.download_btn.setObjectName("download_btn")
        self.gridLayout.addWidget(self.download_btn, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 14, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 450))
        self.listWidget.setStyleSheet("font: 12pt \"Consolas\";")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 1, 8, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 450))
        self.tableWidget.setStyleSheet("font: 12pt \"Consolas\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tableWidget, 1, 2, 8, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quit_btn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Новый ID"))
        self.search_btn.setText(_translate("MainWindow", "Найти"))
        self.label_6.setText(_translate("MainWindow", "Результат поиска в бинарном списке"))
        self.label_5.setText(_translate("MainWindow", "Поиск ID"))
        self.label.setText(_translate("MainWindow", "Путь к файлу"))
        self.add_btn.setText(_translate("MainWindow", "Добавить"))
        self.label_3.setText(_translate("MainWindow", "Таблица с простым рехэшированием"))
        self.quit_btn.setText(_translate("MainWindow", "Выход"))
        self.download_btn.setText(_translate("MainWindow", "Загрузить"))
        self.label_2.setText(_translate("MainWindow", "Бинарный список"))
        self.label_7.setText(_translate("MainWindow", "Результат поиска в хэш-таблице"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Идентификатор"))