import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindows

app = QApplication(sys.argv)

calculator = CalculatorWindows()

sys.exit(app.exec_())
