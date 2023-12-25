#20th Dec 2023, first GUI
# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App(My App)")
window.setGeometry(100, 100, 380, 80)
helloMsg = QLabel("<h1>Hello, World!\n Anusri here!</h1>", parent=window)
helloMsg.move(60, 15)


# 4. Show your application's GUI
window.show()
#it should also cancel the folders or any application database before opening

# 5. Run your application's event loop
sys.exit(app.exec())