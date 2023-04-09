import sys
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from pyzbar import pyzbar


class BarcodeReader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.isbn = ""
        self.pause = False

        self.cam_label = QLabel(self)
        self.cam_label.setGeometry(10, 10, 640, 480)
        self.isbn_label = QLabel(self)
        self.isbn_label.setGeometry(10, 500, 640, 50)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.setGeometry(10, 560, 100, 30)
        self.pause_button.clicked.connect(self.toggle_pause)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.setWindowTitle("Barcode Reader")
        self.setGeometry(100, 100, 660, 600)
        self.show()

    def toggle_pause(self):
        self.pause = not self.pause

    def update_frame(self):
        if not self.pause:
            ret, frame = self.cam.read()
            if ret:
                self.display_cam_image(frame)

                self.isbn = self.read_barcode(frame)
                if self.isbn:
                    self.isbn_label.setText("ISBN: " + self.isbn)
                else:
                    #self.isbn_label.setText("")
                    a=1

    def display_cam_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w, ch = image.shape
        bytes_per_line = ch * w
        q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.cam_label.setPixmap(pixmap)

    def read_barcode(self, image):
        barcodes = pyzbar.decode(image)
        if barcodes:
            return barcodes[0].data.decode("utf-8")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    reader = BarcodeReader()
    reader.cam = cv2.VideoCapture(0)
    sys.exit(app.exec_())
