#Python GUI using PyQt5
#Requires Python 3.5.x and above
#Sample made by: MN
#Tutorials from:
#https://pythonspot.com/en/pyqt5/
#https://pythonprogramminglanguage.com/pyqt5-center-window/
#https://pythonprogramminglanguage.com/pyqt5-button/

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    #Initializes the window
    def __init__(self):
        super().__init__()
        self.title='PyQt5 Simple Window - Sample GUI for Python using PyQt5 lib'
        self.top = 10       #Window position relative to top (in pt or px)
        self.left = 10      #Window position relative to left (in pt or px)
        self.width = 500    #Window width (in pt or px)
        self.height = 250   #Window height (in pt or px)
        self.initUI()       #initializing function

    #Draws the window using initialization
    def initUI(self):
        #Centers the window
        #Optional but gives a nice touch
        qtRectangle = self.frameGeometry()  #Dimension of the window
        center = QDesktopWidget().availableGeometry().center()  #Gets center of presenting media
        qtRectangle.moveCenter(center)  #Moves the window plot to center

        #Label with absolute positioning
        label = QLabel('Python Sample GUI', self)
        label.move(10,0)    #absolute positioning for object

        #Statusbar message
        self.statusBar().showMessage('A sample GUI for Python using PyQt5 lib (sample made by MN)')

        #Button (Simple)
        button = QPushButton('Test Button (prints Hello World to Py Shell)', self)
        button.setToolTip('Sample Button')  #Button tooltip (when hovered)
        button.resize(300,50)   #Resizes the button
        button.move(30,30)      #absolute positioning
        button.clicked.connect(self.btn_click_test) #binds the button to an event listener (slot in pyqt5)

        #Button (Message Box Trigger)
        mb = QPushButton('Show Message Box', self)
        mb.setToolTip('Click to show message box.')
        mb.resize(300,50)
        mb.move(30,80)
        mb.clicked.connect(self.show_messagebox)

        #Text box
        self.textbox = QLineEdit(self)  #creates the textbox
        self.textbox.move(30,130)
        self.textbox.resize(300,80)

        #Sample button that prints the text from textbox into shell
        printbox = QPushButton('Print Text in Python Shell', self)
        printbox.setToolTip('Print text to Python Shell')
        printbox.resize(150,25)
        printbox.move(330,130)
        printbox.clicked.connect(self.print_text)

        #Sample button that shows messagebox with the text from textbox
        showbox = QPushButton('Display Message Box\nwith Text', self)
        showbox.setToolTip('Display text')
        showbox.resize(150,50)
        showbox.move(330,160)
        showbox.clicked.connect(self.show_text)
        
        #Window draw (takes all window and object initializations and then draws it)
        self.setWindowTitle(self.title) #sets window title
        self.setGeometry(self.left, self.top, self.width, self.height)  #sets window size
        self.move(qtRectangle.topLeft())    #Moves the actual window before showing

        #Shows the window
        self.show()

    #Click Listeners
    @pyqtSlot()
    def btn_click_test(self):
        print('Hello World from PyQt5 button click!')

    @pyqtSlot()
    def show_messagebox(self):
        QMessageBox.question(self, 'PyQt5 Message Box', 'Testing PyQt5 Message Box... \n\n Hello World!', QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def print_text(self):
        print(self.textbox.text())

    @pyqtSlot()
    def show_text(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'PyQt5 Message Box', 'You entered: ' + textboxValue, QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
