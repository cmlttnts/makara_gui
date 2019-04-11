
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QGridLayout, QStackedWidget, QLineEdit,
							 QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QFormLayout)

class MyWindow(QWidget):

	def __init__(self):
		super(MyWindow, self).__init__()


		self.mak_num_but = QPushButton("Ok")
		self.Page1 = QWidget()
		self.Page2 = QWidget()




		self.page1_ui()

		self.Stack_of_Pages = QStackedWidget(self)
		self.Stack_of_Pages.addWidget(self.Page1)
		self.Stack_of_Pages.addWidget(self.Page2)

		hbox = QHBoxLayout()
		hbox.addWidget(self.Stack_of_Pages)



		self.setLayout(hbox)
		self.mak_num_but.clicked.connect(self.mak_num_but_func)
		self.setGeometry(100, 100, 100, 100)
		self.setWindowTitle("Makara")
		self.show()

	def page1_ui(self):
		self.mak_num_label = QLabel("Makara Sayısı:")
		self.mak_num_line = QLineEdit()
		hbox = QHBoxLayout()
		hbox.addWidget(self.mak_num_label)
		hbox.addWidget(self.mak_num_line)
		hbox.addWidget(self.mak_num_but)
		self.Page1.setLayout(hbox)

	def page2_ui(self, mak_num):
		buttons = []
		hbox2 = QHBoxLayout()

		for i in range(mak_num):
			buttons.append(QPushButton("button " + str(i)))
			hbox2.addWidget(buttons[i])
		self.Page2.setLayout(hbox2)

	# TODO: num_of_maks should be checked if integer and 0 < num
	def mak_num_but_func(self):
		num_of_maks = int (self.mak_num_line.text())
		self.page2_ui(num_of_maks)
		self.Stack_of_Pages.setCurrentIndex(1)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWindow()
	sys.exit(app.exec_())
