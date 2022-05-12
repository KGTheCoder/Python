import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel 
from PyQt5.QtWidgets import QWidget 

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Nutrition App')
window.setGeometry(0, 0, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1></h1>', parent=window)
helloMsg.move(60, 15)

window.showMaximized()

window.show()

sys.exit(app.exec_())