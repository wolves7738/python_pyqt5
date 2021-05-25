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
        grid.addWidget(self.height1, 4,0)
        grid.addWidget(self.weight1, 5,0)

        self.name2 = QLineEdit()
        self.height2 = QLineEdit()
        self.weight2 = QLineEdit()
        
        grid.addWidget(self.name2,0,1)
        grid.addWidget(self.height2,4,1)
        grid.addWidget(self.weight2,5,1)

        self.mybutton = QPushButton('검색', self)
        self.mybutton.clicked.connect(self.select)

        grid.addWidget(self.mybutton, 3,1)

        self.setWindowTitle("select idol_info")
        self.setGeometry(300,300,400,100)
        self.show()

    def select(self):
        self.name3 = self.name2.text()
        sql = "select * from idol where name like '%{0}%'".format(self.name3)
        curs.execute(sql)
        row = curs.fetchone()
        self.height2.setText(str(row[1]))
        self.weight2.setText(str(row[2]))
    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())


conn.close()