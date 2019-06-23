from PyQt5.QtCore import QThread, pyqtSignal, Qt, pyqtSlot, QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from khayyam3 import JalaliDatetime
from rent_gui import *
from os import path
import store_db
import cv2
import sys

IMGS = path.join(path.abspath("."), "imgs/")


class CAM(QThread):
    change_pix_map = pyqtSignal(QImage)
    cap = cv2.VideoCapture(0)

    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        self.onStop = False
        self.path_to_save = None

    def __del__(self):
        self.wait()

    def stop(self, _path):
        try:
            self.path_to_save = _path
            self.onStop = True
        except Exception as E:
            print(E)

    def run(self):
        self.cap.open(0)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb_image = cv2.resize(rgb_image, (340, 201))
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                p = convert_to_qt_format.scaled(340, 201, Qt.KeepAspectRatio)
                self.change_pix_map.emit(p)
                if self.onStop:
                    cv2.imwrite(self.path_to_save, frame)
                    self.cap.release()
                    cv2.destroyAllWindows()
                    self.quit()
                    self.exit(0)
                    break


class LCD(QThread):
    change_time = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        self.dataCollectionTimer = QTimer()
        self.dataCollectionTimer.moveToThread(self)
        self.dataCollectionTimer.timeout.connect(self.show_lcd)

    def show_lcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.change_time.emit(text)

    def run(self):
        self.dataCollectionTimer.start(1000)
        loop = QEventLoop()
        loop.exec_()


class RentForm(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.customer_id.setText(str(store_db.get_last_row() + 1))
        self.today = JalaliDatetime.now().date()
        self.cur_time = JalaliDatetime.now().time()
        self.ui.date.setText(self.today.strftime("%y/%m/%d"))
        self.ui.submit.clicked.connect(self.display_submit)
        self.ui.capture.clicked.connect(self.capture)
        self.ui.again.clicked.connect(self.act_again)

        self.cam = CAM(self)
        self.lcd_clock = LCD(self)
        self.init_ui()

        self.show()
        # self._next = Next()

        self.img_path = ""

    @pyqtSlot(QImage)
    def set_image(self, image):
        self.ui.image.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str)
    def set_time(self, t):
        self.cur_time = JalaliDatetime.strptime(t, "%H:%M:%S").time()
        # hour : minute
        self.ui.lcdNumber.display(t[:-3])

    def init_ui(self):
        self.cam.change_pix_map.connect(self.set_image)
        self.cam.start()
        self.lcd_clock.change_time.connect(self.set_time)
        self.lcd_clock.start()

    def display_submit(self):
        """
        gathering data from widgets
        """

        _id = int(self.ui.customer_id.text())
        date = self.today.to_date()
        time = self.cur_time
        who = self.ui.comboBox.currentText()
        first_name = self.ui.first_name.text()
        last_name = self.ui.last_name.text()
        address = self.ui.address.text()
        product = self.ui.product.toPlainText()
        pre_paid = self.ui.pre_paid.text()
        post_paid = self.ui.post_paid.text()
        paid = self.ui.paid.text()
        others = self.ui.others.toPlainText()
        rent = store_db.Rent(_id, date, time, who, first_name, last_name, product,
                             address, pre_paid, post_paid, paid, others, self.img_path)
        store_db.add(rent)
        # self._next.show()

    def capture(self):
        try:
            self.img_path = path.join(IMGS, str(self.ui.customer_id.text()).zfill(9) + ".jpg")
            self.cam.stop(_path=self.img_path)
            self.ui.again.setEnabled(True)
        except Exception as E:
            print(E)

    def act_again(self):
        try:
            self.cam = CAM()
            self.init_ui()
            self.ui.again.setEnabled(False)
        except Exception as E:
            print(E)


# class Next(QDialog):
#     def __init__(self, parent=None):
#         super(Next, self).__init__(parent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = RentForm()
    f.show()
    sys.exit(app.exec_())
