import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import mplcursors
from matplotlib.figure import Figure
import pandas as pd
import UpdateAndReadData.readdata as READ
def GetChart(fig : Figure,country = 'Vietnam',time = 'One Month', type = 'new_cases'):
    data = READ.GetData(country,time)
    data['date'] = pd.to_datetime(data['date'], format="%Y-%m-%d")
    data['dayofmonth'] = data['date'].dt.strftime('%d/%m')
    data.replace(np.nan,0,inplace=True)
    sns.set_style('darkgrid')
    #plt.plot(data['dayofmonth'],data[type],marker = 'o')
    sns.lineplot(x='dayofmonth', y=type, data=data,marker="o")
    if type == 'new_deaths': name = 'New Deaths'
    elif type == 'new_cases': name = 'New Cases'
    else: name = 'Vaccinated'
    #plt.title('title name')
    plt.xlabel('Date')
    plt.ylabel(name)
    curs = mplcursors.cursor(fig,hover = True)
    @curs.connect("add")
    def _(sel):
        inx = round(sel.index)
        #print(data.iloc[inx])
        sel.annotation.get_bbox_patch().set(fc="white")
        sel.annotation.arrow_patch.set(arrowstyle="simple", fc="white", alpha=.5)
        sel.annotation.set_text("Date: {}\n{}: {}".format(data.iloc[inx]['date'].strftime('%d/%m/%Y'),name ,round(data.iloc[inx][type])))
    if time == 'One Month' : plt.xticks(ticks = [4,9,14,19,24,29])
    elif time =='Two Weeks': plt.xticks(ticks = [1,3,5,7,9,11,13])
    plt.fill_between(data['dayofmonth'],data[type], alpha=0.2)