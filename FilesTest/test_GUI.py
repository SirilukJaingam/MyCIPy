# test_main.py
import pytest
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from mainGUI import MyMainWindow

@pytest.fixture(scope="session")
def app(qapp):
    yield qapp

@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.exit()

@pytest.fixture
def window(app):
    test_window = MyMainWindow()
    test_window.show()
    yield test_window

def test_initial_ui_state(window):
    assert window.label.text() == "Hello, World!"

def test_button_click_changes_label_text(window, qtbot):
    # Simulate a button click
    qtbot.mouseClick(window.button, Qt.LeftButton)

    assert window.label.text() == "Button Clicked!"

