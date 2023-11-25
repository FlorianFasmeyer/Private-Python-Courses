from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
from tkinter import messagebox


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi('main.ui', self)

        self.pushButton.clicked.connect(self.clickhandler)
        self.comboBox.addItem('Information')
        self.comboBox.addItem('Warning')
        self.comboBox.addItem('Error')
        self.comboBox.addItem('Question Yes/No')
        self.comboBox.addItem('Question Ok/Cancel')
        self.comboBox.addItem('Warning Retry/Cancel')
        self.comboBox.setCurrentIndex(0)

    def clickhandler(self):
        print('Hello World')
        message = self.lineEdit.text()
        if self.comboBox.currentIndex() == 0:
            messagebox.showinfo("Information", message)
        elif self.comboBox.currentIndex() == 1:
            messagebox.showwarning("Warning", message)
        elif self.comboBox.currentIndex() == 2:
            messagebox.showerror("Error", message)
        elif self.comboBox.currentIndex() == 3:
            messagebox.askquestion("Confirm", message)
        elif self.comboBox.currentIndex() == 4:
            messagebox.askokcancel("Confirm", message)
        elif self.comboBox.currentIndex() == 5:
            messagebox.askretrycancel("Warning", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
