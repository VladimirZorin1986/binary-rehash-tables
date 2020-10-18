from PyQt5 import QtWidgets
from design import Ui_MainWindow
import sys
from binary_table import BinaryTable
from hash_table import RehashTable, N


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bin_table = None
        self.rehash_table = None
        self.ui.tableWidget.setRowCount(N)
        self.ui.download_btn.clicked.connect(self.download)
        self.ui.add_btn.clicked.connect(self.add)
        self.ui.search_btn.clicked.connect(self.search)

    def download(self):
        path = self.ui.filepath.text()
        self.bin_table = BinaryTable(path)
        self.rehash_table = RehashTable(path)
        self.ui.listWidget.addItems(self.bin_table.data)
        self.rehash_fill()

    def add(self):
        value = self.ui.add_id.text()
        self.ui.add_res.setText(self.bin_table.add_element(value))
        self.rehash_table.add_element(value)
        if self.ui.add_res.text() != 'Уже есть в таблице':
            self.ui.listWidget.insertItem(self.bin_table.get_index(value), value)
        self.ui.tableWidget.clearContents()
        self.rehash_fill()

    def search(self):
        value = self.ui.search_id.text()
        self.ui.search_bin_res.setText(self.bin_table.search_element(value))
        self.ui.search_hash_res.setText(self.rehash_table.search_element(value))

    def rehash_fill(self):
        for row, value in self.rehash_table.data.items():
            self.ui.tableWidget.setItem(row + 1, 0, QtWidgets.QTableWidgetItem(str(row)))
            if value is None:
                value = '--'
            self.ui.tableWidget.setItem(row + 1, 1, QtWidgets.QTableWidgetItem(value))


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
