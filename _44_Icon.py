from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon
import sys

app = QApplication(sys.argv)

# window = QMainWindow()
# window.setWindowTitle("Main Window")
# window.setWindowIcon(QIcon('Sun.png'))
# # window.setStyleSheet('background:blue')
# # window.setWindowOpacity(0.5)
# window.setGeometry(100, 100, 300, 500)
# btn = QPushButton("Click this")
# btn.show()

# hBox = QHBoxLayout()
# hBox.addWidget(btn)
# window.setLayout(hBox)

# window.show()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Click")
        hBox = QHBoxLayout()
        hBox.addWidget(btn)
        self.setLayout(hBox)

window = MyWindow()
window.show()


sys.exit(app.exec())