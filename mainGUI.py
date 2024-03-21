# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Hello, World!", self)
        self.label.setGeometry(100, 50, 200, 30)

        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(100, 100, 100, 30)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText("Button Clicked!")


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
