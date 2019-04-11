import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction


class  Ui_MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

    def setupUI(self):

        self.setGeometry(500, 300, 700, 700)

        self.setWindowTitle("window")

        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

        menubar = self.menuBar()
        fmenu = menubar.addMenu("File")
        fmenu.addAction(finish)

    def retranslateUi(self):
        ## codes
        codes = "___"


    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.setupUI()
    window.show()
    sys.exit(app.exec_())