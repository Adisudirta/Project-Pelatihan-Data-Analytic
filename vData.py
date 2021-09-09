import pandas as pd
import matplotlib.pyplot as plt

# IDN : Indonesia
# JPN : Jepang
# SGP : Singapura
# KOR : Korea Selatan
# HKG : Hong Kong
# ISR : Israel

# convert file csv kedalam bentuk dataframe
df = pd.read_csv('./archive/transformed_data.csv')

# ambil kode unik tiap negara dengan select distinc
uniqueCode = df['CODE'].unique()

# function untuk menghitung mean
def calculateMean(code, col):
    for i in uniqueCode:
        if i == code:
            data = df[df['CODE'] == code]
            return data[col].mean()

# function untuk memvisualisasikan data
def visualisasi(col):
    listCountry = ['IDN', 'JPN', 'SGP', 'KOR', 'HKG', 'ISR']
    listMean = [calculateMean(x, col) for x in listCountry]

    df = pd.DataFrame({
        "country": listCountry,
        "mean": listMean
    })
    print(df)

    plt.bar(listCountry, listMean, width = 0.5, color = "#000099")

    # memberi marker value pada bar chart
    for i in range(len(listMean)):
        plt.text(i ,listMean[i],"{:.2f}".format(listMean[i]), horizontalalignment = 'center')
    
    # jika GDP yg akan divisulisasikan
    if col == 'GDPCAP':
        plt.title('Perbandingan GDP per kapita Indonesia dengan negara maju di asia')
        plt.ylabel('GDP per kapita')
        plt.grid(axis = 'y', color = "green")
        plt.show() 
    
    # jika HDI yg akan divisualisasikan
    else:
        plt.title('Perbandingan Human Development Index Indonesia dengan negara maju di asia')
        plt.ylabel('Human Development Index')
        plt.grid(axis = 'y', color = "green")
        plt.show()
    