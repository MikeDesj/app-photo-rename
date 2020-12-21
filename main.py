import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit
from PySide6.QtCore import QFile, QObject

class MainWindow(QObject):
    
    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        
        btn = self.window.findChild(QPushButton, 'pushButton')
        btn.clicked.connect(self.ok_handler)
        self.window.show()

    def ok_handler(self):
        print("It works")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow('mainwindow.ui')
    sys.exit(app.exec_())