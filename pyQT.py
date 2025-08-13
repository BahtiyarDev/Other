import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow

# lesson1
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Simp Programm")
        self.setGeometry(0, 0, 450, 400) #Set window size

        self.text = QtWidgets.QLabel(self) #Add text in window
        self.text.setText("Hello, World!")
        self.text.adjustSize() #Set window size considering object in it
        self.text.move(200, 200) #Move text in window

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Tap Me!")
        self.button.move(185, 300)
        self.button.clicked.connect(self.button_action)

        self.label = QtWidgets.QLabel(self)


    def button_action(self):
        self.label.setText("Аболтуз!")
        self.label.move(215, 260)
        self.label.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()



    window.show() #Show window
    sys.exit(app.exec_())

application()

