from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys

app = QApplication(sys.argv)

widget = QWidget()
widget.setWindowTitle("Widget")
widget.show()

window = QMainWindow()
window.setWindowTitle("Main Window")
window.show()

dialog = QDialog()
dialog. setWindowTitle("Dialog")
dialog.show()       # Modeless
# dialog.exec()       # Modal


sys.exit(app.exec())