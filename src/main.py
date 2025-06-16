
from PySide6.QtWidgets import QApplication
import sys
import os
# Handle ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ui.app import MyApp

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MyApp()
        window.show()
        app.exec()
    except Exception as e:
        print(e)
