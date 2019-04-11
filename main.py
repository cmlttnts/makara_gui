
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QStackedWidget,
							QHBoxLayout, QVBoxLayout, QApplication, QLineEdit)

makara_coords = []


class MyWindow(QWidget):

	def __init__(self):
		super(MyWindow, self).__init__()

		self.mak_num_line = QLineEdit()
		self.mak_num_label = QLabel("Makara Sayısı:")
		self.line_edits_z = []
		self.line_edits_y = []
		self.line_edits_x = []
		self.mak_num_but = QPushButton("Next")
		self.xyz_next_button = QPushButton("Next")
		self.xyz_back_button = QPushButton("Back")
		# self.mak_num_but.setEnabled(False)
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
		self.xyz_next_button.clicked.connect(self.xyz_next_func)

		self.setGeometry(100, 100, 500, 500)
		self.setWindowTitle("Makara")
		self.show()

	def page1_ui(self):
		hbox = QHBoxLayout()
		hbox.addWidget(self.mak_num_label)
		hbox.addWidget(self.mak_num_line)
		vbox = QVBoxLayout()
		vbox.addLayout(hbox)
		vbox.addWidget(self.mak_num_but)

		self.Page1.setLayout(vbox)

	def page2_ui(self, mak_num):
		hboxes = [] # horizontal layout
		vbox2 = QVBoxLayout() # vertical layout

		for i in range(mak_num):
			# each makara should get a horizontal line
			hboxes.append(QHBoxLayout())
			label = QLabel("Makara "+ str(i))
			self.line_edits_x.append(QLineEdit())
			self.line_edits_y.append(QLineEdit())
			self.line_edits_z.append(QLineEdit())

			# name of the makara
			hboxes[i].addWidget(label)
			# x value box
			hboxes[i].addWidget(QLabel("x:"))
			hboxes[i].addWidget(self.line_edits_x[i])
			# y value box
			hboxes[i].addWidget(QLabel("y:"))
			hboxes[i].addWidget(self.line_edits_y[i])
			# z value box
			hboxes[i].addWidget(QLabel("z:"))
			hboxes[i].addWidget(self.line_edits_z[i])

			# Each horizontal line should be listed vertically
			vbox2.addLayout(hboxes[i])
		hbox3 = QHBoxLayout()
		hbox3.addWidget(self.xyz_back_button)
		hbox3.addWidget(self.xyz_next_button)
		vbox2.addLayout(hbox3)
		self.Page2.setLayout(vbox2)

	# TODO: num_of_maks should be checked if integer and 0 < num
	def mak_num_but_func(self):
		try:
			num_of_maks = int(self.mak_num_line.text())
			if num_of_maks <= 0:
				self.mak_num_line.setText("Try positive integers")
				return
			elif num_of_maks > 10:
				self.mak_num_line.setText("Try smaller integers")
				return
		except ValueError:
			self.mak_num_line.setText("Try numbers")
			return
		self.num_maks = num_of_maks
		self.page2_ui(num_of_maks)
		self.Stack_of_Pages.setCurrentIndex(1)

	def xyz_next_func(self):
		mak_coords = []
		temp = []
		m, k = 0, 0
		mak_num = self.num_maks
		try:
			for i in range(mak_num):
				m = i
				temp.append(float(self.line_edits_x[i].text()))
				k += 1
				temp.append(float(self.line_edits_y[i].text()))
				k += 1
				temp.append(float(self.line_edits_z[i].text()))
				mak_coords.append(temp)
				temp = []
				k = 0
		except ValueError:
			if k == 0:
				self.line_edits_x[m].setText("Error!")
			elif k == 1:
				self.line_edits_y[m].setText("Error!")
			else:
				self.line_edits_z[m].setText("Error!")
			return
		global makara_coords
		makara_coords = mak_coords


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWindow()
	try:
		app.exec_()
	except Exception as e:
		print(e)
	print(makara_coords)

