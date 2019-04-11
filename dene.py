from PyQt5 import QtGui, QtCore, QtWidgets
from time import sleep

class Test(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        button = QtWidgets.QPushButton("Button")
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(button)
        self.setLayout(hbox)
        button.clicked.connect(self.slot)

    def slot(self):
        progress = QtWidgets.QProgressDialog(self)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.setLabel(QtWidgets.QLabel("Doing things..."))
        progress.setAutoClose(True)
        for i in range(101):
             progress.setValue(i);
             sleep(0.05)
             if progress.wasCanceled():
                 break


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = Test()
    myapp.show()
    sys.exit(app.exec_())
