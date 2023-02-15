#cradit - OFFCODE TUTORIALS
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from urllib.parse import quote_plus

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Browser')
        self.setGeometry(100, 100, 800, 600)
        
        # Create a toolbar with back, forward, and search buttons
        toolbar = QToolBar()
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.back)
        toolbar.addAction(back_button)
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.forward)
        toolbar.addAction(forward_button)
        toolbar.addSeparator()
        self.search_box = QLineEdit()
        self.search_box.returnPressed.connect(self.search)
        toolbar.addWidget(self.search_box)
        search_button = QAction('Search', self)
        search_button.triggered.connect(self.search)
        toolbar.addAction(search_button)
        self.addToolBar(toolbar)
        
        # Create a line edit for entering URLs
        url_edit = QLineEdit()
        url_edit.returnPressed.connect(self.load)
        toolbar.addWidget(url_edit)
        
        # Create the web view widget
        self.view = QWebEngineView()
        self.view.loadProgress.connect(self.update_progress)
        self.setCentralWidget(self.view)
        
        # Create a progress bar
        self.progress_bar = QProgressBar()
        self.statusBar().addPermanentWidget(self.progress_bar)
        
    def back(self):
        self.view.back()
        
    def forward(self):
        self.view.forward()
        
    def load(self):
        url = self.sender().text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.view.load(QUrl(url))
        
    def update_progress(self, progress):
        self.progress_bar.setValue(progress)
        if progress == 100:
            self.progress_bar.hide()
        else:
            self.progress_bar.show()
            
    def search(self):
        query = self.search_box.text()
        if query:
            query = quote_plus(query)
            url = f'https://www.google.com/search?q={query}'
            self.view.load(QUrl(url))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    app.exec_()
