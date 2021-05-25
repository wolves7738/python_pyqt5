import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QListWidgetItem, QPushButton, QWidget

conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='pyschool', charset='utf8')
curs = conn.cursor()

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.name1 = QLabel('이름')
        self.height1 = QLabel('키')
        self.weight1 = QLabel('몸무게')

        grid.addWidget(self.name1, 0,0)
        grid.addWidget(self.height1, 1,0)
        grid.addWidget(self.weight1, 2,0)

        self.name2 = QLineEdit()
        self.height2 = QLineEdit()
        self.weight2 = QLineEdit()
        # self.result = QLineEdit()
        

        grid.addWidget(self.name2,0,1)
        grid.addWidget(self.height2,1,1)
        grid.addWidget(self.weight2,2,1)
        # grid.addWidget(self.result, 4,1)

        self.mybutton = QPushButton('추가', self)
        self.mybutton.clicked.connect(self.insert)

        grid.addWidget(self.mybutton, 3,1)

        self.setWindowTitle("insert idol_info")
        self.setGeometry(300,300,400,100)
        self.show()

    def insert(self):
        self.name3 = self.name2.text()
        self.height3 = int(self.height2.text())
        self.weight3 = int(self.weight2.text())

        sql = "insert into idol values('{0}',{1}, {2})".format(self.name3, self.height3, self.weight3)
        curs.execute(sql)
        conn.commit()
        # sql = "select * from idol"
        # curs.execute(sql)
        # rows = curs.fetchall()
        # for row in rows:
        #     print("{0}, {1}, {2}".format(row[0], row[1], row[2]))
        #     print("-----------------------------")
        self.name2.setText("")
        self.weight2.setText("")
        self.height2.setText("")


        
    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())


conn.close()