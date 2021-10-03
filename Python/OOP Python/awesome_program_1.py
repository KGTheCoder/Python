# Filename: hello.py

"""Simple Hello World example with PyQt5."""

# Allows us to handle the exit status of the application
import sys

# 1. Import 'QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget 

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('PyQT App')
window.setGeometry(0, 0, 500, 500)
window.move(60, 15)
helloMsg = QLabel('<h1>Hi, this is my GUI!</h1>', parent=window)
helloMsg.move(30, 20)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())