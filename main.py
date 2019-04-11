
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
		line_edits = []
		buttons = []
		hboxes = [] # horizontal layout
		vbox2 = QVBoxLayout() # vertical layout

		# TODO make x,y,z inputs for each makara
		for i in range(mak_num):
			# each makara should get a horizontal line
			hboxes.append(QHBoxLayout())
			buttons.append(QPushButton("Ok"))
			label = QLabel("Makara "+ str(i))
			line_edits.append(QLineEdit())

			hboxes[i].addWidget(label)
			hboxes[i].addWidget(line_edits[i])
			hboxes[i].addWidget(buttons[i])
			# Each horizontal line should be listed vertically
			vbox2.addLayout(hboxes[i])

		self.Page2.setLayout(vbox2)

	# TODO: num_of_maks should be checked if integer and 0 < num
	def mak_num_but_func(self):
		num_of_maks = int (self.mak_num_line.text())
		self.page2_ui(num_of_maks)
		self.Stack_of_Pages.setCurrentIndex(1)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWindow()
	sys.exit(app.exec_())
