from PyQt5.QtWidgets import *
import UpdateAndReadData.readdata as READ
import UpdateAndReadData.updatedata as Update
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from Chart.BarChart  import GetBarChart
from Chart.MultiChart import GetChartMutli
class NewCaseChartWidget(QWidget):
    def updating(self):
        READ.dataCovid =  Update.GetNewData()
        self.changeChart()
    def __init__(self):
        super().__init__()
        self.outerLayout  = QVBoxLayout()
        ComboLayout  = QHBoxLayout()
        self.resize(800, 500)
        self.current_Country   =  QComboBox(self)
        CountryList = sorted(READ.GetCountryName())
        self.current_Country.addItems(CountryList)
        self.current_Country.setCurrentText("Vietnam")
        self.current_time   =  QComboBox(self)
        CountryList = ['One Week','Two Weeks','One Month']
        self.current_time.addItems(CountryList)
        self.current_time.setCurrentIndex(2)
        TypeList = ['New Cases','New Deaths','BOTH']
        self.current_type = QComboBox(self)
        self.current_type.addItems(TypeList)
        self.current_type.setCurrentIndex(0)
        self.refreshbutton = QPushButton("REFRESH")
        self.refreshbutton.clicked.connect(self.changeChart)
        self.updatebutton = QPushButton("Download latest data")
        self.updatebutton.clicked.connect(self.updating)
        ComboLayout.addWidget(self.current_Country,1)
        ComboLayout.addWidget(self.current_time,1)
        ComboLayout.addWidget(self.current_type,0)
        ComboLayout.addWidget(self.refreshbutton,0)
        ComboLayout.addWidget(self.updatebutton,0)
        self.outerLayout.addLayout(ComboLayout)
        self.fig = plt.figure(figsize=(10,5))
        GetBarChart(self.fig)
        self.chart = FigureCanvasQTAgg(self.fig)
        self.outerLayout.addWidget(self.chart)
        self.setLayout(self.outerLayout)
        self.current_Country.currentIndexChanged.connect(self.changeChart)
        self.current_time.currentIndexChanged.connect(self.changeChart)
        self.current_type.currentIndexChanged.connect(self.changeChart)
    def changeChart(self):
        plt.close(self.fig)
        self.fig.clear()
        self.fig = plt.figure(figsize=(10,5))
        if (self.current_type.currentIndex()==2):
            GetChartMutli(self.fig,country=self.current_Country.currentText(),time=self.current_time.currentText())
        elif self.current_type.currentIndex() == 1:
            GetBarChart(self.fig,country=self.current_Country.currentText(),time=self.current_time.currentText(),type='new_deaths')
        else:
            GetBarChart(self.fig,country=self.current_Country.currentText(),time=self.current_time.currentText())
        self.outerLayout.removeWidget(self.chart)
        self.chart =FigureCanvasQTAgg(self.fig)
        self.outerLayout.addWidget(self.chart)