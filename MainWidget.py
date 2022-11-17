from PyQt5.QtWidgets import *
from Application.MapWidget import MapWidget
from Application.NewCaseWidget import NewCaseChartWidget
from Application.NewVaccinateWidget import NewVaccinateChartWidget
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Covid 19 Tracking")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.chiltabs = []
        self.chiltabs.append((NewCaseChartWidget(),"New Cases"))
        #self.chiltabs.append((ChartWidget("new_deaths",True),"New Deaths"))
        self.chiltabs.append((NewVaccinateChartWidget(),"New Vaccinations"))
        self.chiltabs.append((MapWidget(),"Map"))
        tabs = QTabWidget()
        for _ in self.chiltabs:
            tabs.addTab(_[0],_[1])
        layout.addWidget(tabs)