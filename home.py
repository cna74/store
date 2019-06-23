from PyQt5.QtCore import QThread, pyqtSignal, Qt, pyqtSlot, QEventLoop, QTimer
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
import home_page
import rent
import sys


class Home(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = home_page.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.new_rent.clicked.connect(self.new_rent)

    def new_rent(self):
        new_rnt = rent.RentForm()
        self.close()
        new_rnt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Home()
    f.show()
    sys.exit(app.exec_())
