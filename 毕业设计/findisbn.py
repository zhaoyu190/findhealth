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
        self.flags1 = False
        self.cam_label = QLabel(self)
        self.cam_label.setGeometry(10, 10, 640, 480)
        self.isbn_label = QLabel(self)
        self.isbn_label.setGeometry(10, 500, 640, 50)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.setGeometry(10, 560, 100, 30)
        self.pause_button.clicked.connect(self.toggle_pause)

        self.pause_button = QPushButton("查询", self)
        self.pause_button.setGeometry(120, 560, 100, 30)
        self.pause_button.clicked.connect(self.git_api)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        detailx=800
        self.book_title = QLabel(self)
        self.book_title.move(detailx, 50)
        self.book_title.resize(700, 50)

        self.isbn = QLabel(self)
        self.isbn.move(detailx, 100)
        self.isbn.resize(700, 50)

        self.publisher = QLabel(self)
        self.publisher.move(detailx, 150)
        self.publisher.resize(700, 50)

        self.pub_place = QLabel(self)
        self.pub_place.move(detailx, 200)
        self.pub_place.resize(700, 50)

        self.pub_date = QLabel(self)
        self.pub_date.move(detailx, 250)
        self.pub_date.resize(700, 50)

        self.book_description = QLabel(self)
        self.book_description.move(detailx, 300)
        self.book_description.resize(700, 50)
        self.book_description.setWordWrap(True)
        self.setWindowTitle("Barcode Reader")
        self.setGeometry(100, 100, 1660, 600)

        self.data = {
            "code": 200,
            "msg": "成功",
            "taskNo": "65171553403304103621",
            "data": {
                "details": [
                    {
                        "series": "",
                        "title": "2018百校联盟-1年语文上(人教版)",
                        "author": " 靳俊针主编",
                        "publisher": "吉林教育出版社",
                        "pubDate": "2019.09.01",
                        "pubPlace": "长春",
                        "isbn": "9787555357902",
                        "isbn10": "7555357909",
                        "price": "28.80",
                        "genus": "TP311.132.3",
                        "levelNum": "",
                        "heatNum": "0",
                        "format": "",
                        "binding": "平装",
                        "page": "",
                        "wordNum": "",
                        "edition": "1版",
                        "yinci": "1",
                        "paper": "",
                        "language": "",
                        "keyword": "|小学语文课|习题集",
                        "img": "",
                        "bookCatalog": "",
                        "gist": "本书的特点是紧扣新课标实验教材，按单元进行编写；每单元都由基础知识和重难点梯度安排，重点考查学生掌握基础知识和基本技能的情况；融合思考性、实践性、综合性较强的题目，适当增加了难度，进一步考查学生思维发展和综合运用知识的能力。",
                        "cipTxt": "    百校联考冲刺100分. 语文一年级. 上 : RJ / 靳俊\n针主编. -- 长春 : 吉林教育出版社, 2018.5 \n    ISBN 978-7-5553-5790-2\n \n    Ⅰ. ①百… Ⅱ. ①靳… Ⅲ. ①小学语文课－习题集 \nⅣ. ①G624\n \n    中国版本图书馆CIP数据核字(2018)第109776号",
                        "annotation": "",
                        "subject": "",
                        "batch": ""
                    }
                ]
            }
        }
        self.book_info ={
                        "series": "",
                        "title": "错",
                        "author": " 靳俊针主编",
                        "publisher": "吉林教育出版社",
                        "pubDate": "2019.09.01",
                        "pubPlace": "长春",
                        "isbn": "9787555357902",
                        "isbn10": "7555357909",
                        "price": "28.80",
                        "genus": "TP311.132.3",
                        "levelNum": "",
                        "heatNum": "0",
                        "format": "",
                        "binding": "平装",
                        "page": "",
                        "wordNum": "",
                        "edition": "1版",
                        "yinci": "1",
                        "paper": "",
                        "language": "",
                        "keyword": "|小学语文课|习题集",
                        "img": "",
                        "bookCatalog": "",
                        "gist": "本书的特点是紧扣新课标实验教材，按单元进行编写；每单元都由基础知识和重难点梯度安排，重点考查学生掌握基础知识和基本技能的情况；融合思考性、实践性、综合性较强的题目，适当增加了难度，进一步考查学生思维发展和综合运用知识的能力。",
                        "cipTxt": "    百校联考冲刺100分. 语文一年级. 上 : RJ / 靳俊\n针主编. -- 长春 : 吉林教育出版社, 2018.5 \n    ISBN 978-7-5553-5790-2\n \n    Ⅰ. ①百… Ⅱ. ①靳… Ⅲ. ①小学语文课－习题集 \nⅣ. ①G624\n \n    中国版本图书馆CIP数据核字(2018)第109776号",
                        "annotation": "",
                        "subject": "",
                        "batch": ""
                    }



        self.book_title.setText(f"Book Title: {self.book_info['title']}")
        self.isbn.setText(f"ISBN: {self.book_info['isbn']}")
        self.publisher.setText(f"Publisher: {self.book_info['publisher']}")
        self.pub_place.setText(f"Publication Place: {self.book_info['pubPlace']}")
        self.pub_date.setText(f"Publication Date: {self.book_info['pubDate']}")
        self.book_description.setText(f"Book Description: {self.book_info['gist']}")


        self.show()


    def toggle_pause(self):
        self.pause = not self.pause
    def git_api(self):
        print("点击按钮")
        if self.isbn=='9787555357902':
            self.flags1= True
        if self.flags1==True:
            print('查询成功')
            self.book_info = self.data["data"]["details"][0]
            self.book_title.setText(f"Book Title: {self.book_info['title']}")
            self.isbn.setText(f"ISBN: {self.book_info['isbn']}")
            self.publisher.setText(f"Publisher: {self.book_info['publisher']}")
            self.pub_place.setText(f"Publication Place: {self.book_info['pubPlace']}")
            self.pub_date.setText(f"Publication Date: {self.book_info['pubDate']}")
            self.book_description.setText(f"Book Description: {self.book_info['gist']}")







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
