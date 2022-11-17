from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import io
from Chart.MapChart import GetMapChart
class MapWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.Layout = QVBoxLayout()
        self.setLayout(self.Layout)
        self.refreshbutton = QPushButton("REFRESH")
        self.refreshbutton.clicked.connect(self.changeMap)
        self.webview = QWebEngineView()
        self.webview.setHtml(GetMapChart().getvalue().decode())
        self.Layout.addWidget(self.refreshbutton)
        self.Layout.addWidget(self.webview)
    def changeMap(self):
        self.webview.setHtml(GetMapChart().getvalue().decode())