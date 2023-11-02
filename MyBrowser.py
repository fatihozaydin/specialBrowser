import sys
import PyQt5  
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()





app = QApplication(sys.argv)
QApplication.setApplicationName("F Browser")
window = Home()
app.exec_()