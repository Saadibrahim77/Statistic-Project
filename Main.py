import sys
from PyQt5.QtWidgets import QApplication
from GUI import GUI
app =  QApplication(sys.argv)
widget = GUI()
widget.show()
sys.exit(app.exec_())