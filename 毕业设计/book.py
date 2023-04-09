import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Book Information"
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):
        # 添加标签
        self.book_title = QLabel(self)
        self.book_title.move(50, 50)
        self.book_title.resize(700, 50)

        self.isbn = QLabel(self)
        self.isbn.move(50, 100)
        self.isbn.resize(700, 50)

        self.publisher = QLabel(self)
        self.publisher.move(50, 150)
        self.publisher.resize(700, 50)

        self.pub_place = QLabel(self)
        self.pub_place.move(50, 200)
        self.pub_place.resize(700, 50)

        self.pub_date = QLabel(self)
        self.pub_date.move(50, 250)
        self.pub_date.resize(700, 50)

        self.book_description = QLabel(self)
        self.book_description.move(50, 300)
        self.book_description.resize(700, 50)
        self.book_description.setWordWrap(True)
        # 更新标签内容
        #data = your_function()  # 获取数据
        data ={
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
        book_info = data["data"]["details"][0]

        self.book_title.setText(f"Book Title: {book_info['title']}")
        self.isbn.setText(f"ISBN: {book_info['isbn']}")
        self.publisher.setText(f"Publisher: {book_info['publisher']}")
        self.pub_place.setText(f"Publication Place: {book_info['pubPlace']}")
        self.pub_date.setText(f"Publication Date: {book_info['pubDate']}")
        self.book_description.setText(f"Book Description: {book_info['gist']}")

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
