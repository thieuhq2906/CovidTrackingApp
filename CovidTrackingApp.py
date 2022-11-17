from PyQt5.QtWidgets import * 
import sys
from Application.MainWidget import MainWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())