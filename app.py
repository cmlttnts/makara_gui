
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QFormLayout)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.mak_num_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.mak_num_line = QLineEdit()
        self.mak_num_label = QLabel("Makara sayısı")


        self.hbox1.addWidget(self.mak_num_label)
        self.hbox1.addWidget(self.mak_num_line)
        self.hbox1.addWidget(self.mak_num_button)

        self.setLayout(self.hbox1)

        self.mak_num_button.clicked.connect(self.btn_clk)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


    def btn_clk(self):
        print(self.mak_num_line.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
