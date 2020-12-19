from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(200, 200, 500, 500)
		self.setWindowTitle("App for renaming photos with date and time")
		self.initUI()

	def initUI(self):
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Open file")

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()
