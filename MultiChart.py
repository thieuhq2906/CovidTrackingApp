import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import mplcursors
from matplotlib.figure import Figure
import pandas as pd
import UpdateAndReadData.readdata as READ
def GetChartMutli(fig:Figure,country = 'Vietnam',time = 'One Month'):
    data = READ.GetData(country,time)
    data['date'] = pd.to_datetime(data['date'], format="%Y-%m-%d")
    data['dayofmonth'] = data['date'].dt.strftime('%d/%m')
    sns.set_style('dark')
    line1 = sns.lineplot(x='dayofmonth',y='new_deaths',data=data,marker='o',color='r',label='New Deaths',legend=False)
    #plt.legend(loc=0)
    plt.xlabel("Date")
    plt.ylabel("New Deaths")
    ax2 = plt.twinx()
    line2 = sns.lineplot(x='dayofmonth',y='new_cases',data=data,marker='o',ax=ax2,label='New Cases')
    ax2.set_ylabel("New Cases")
    lines_1, labels_1 = line1.get_legend_handles_labels()
    lines_2, labels_2 = line2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    plt.legend(lines, labels, loc='upper left')
    curs = mplcursors.cursor(fig,hover = True)
    @curs.connect("add")
    def _(sel):
        inx = round(sel.index)
        if (abs(sel.index - inx)>=10**-1): sel.annotation.set_visible(False)
        #print(data.iloc[inx])
        sel.annotation.get_bbox_patch().set(fc="white")
        sel.annotation.arrow_patch.set(arrowstyle="simple", fc="white", alpha=.5)
        sel.annotation.set_text(f"Date: {data.iloc[inx]['dayofmonth']}\nNew Deaths: {data.iloc[inx]['new_deaths']}\nNew Cases:{data.iloc[inx]['new_cases']}")
    if time == 'One Month' : plt.xticks(ticks = [4,9,14,19,24,29])
    elif time =='Two Weeks': plt.xticks(ticks = [1,3,5,7,9,11,13])
    #plt.show()