from UpdateAndReadData.updatedata import ReadData
dataCovid = ReadData()
def GetData(country = 'Vietnam',time = 'One Month'):
    number_of_day = 30 if time == 'One Month' else 7 if time =='One Week' else 14
    result= dataCovid[dataCovid['location'] == country].sort_values("date",ascending=True).tail(number_of_day)
    #print(result)
    return result
def GetCountryName():
    return list(set(dataCovid['location']))