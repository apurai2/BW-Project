import sqlite3
import glob
import csv
import os

#List of all the stocks available

def find_symbol(file_name):
    with open(file_name,'r') as fin:
        bear = csv.DictReader(fin)
        for i in bear:
            if(i['SYMBOL']==None):
                print(file_name)
            return i['SYMBOL']

#List of all the stocks available
#Currently only the first 500 stocks available in SQL database stocks_data.db
        
stocks_symbols =[]
for file in glob.glob('/data/finance/stocks/permno_csv/permno*.csv'):
    stocks_symbols.append(find_symbol(file))
    
#Full CSV files list
    
dir_list=glob.glob('/data/finance/stocks/permno_csv/*.csv')

#Get respective dates series given csv file

def dates_df(csv_file):
    df = pd.read_csv(csv_file)
    dates= pd.Series(df['DATE'])
    dates = pd.to_timedelta(dates, unit='D') + pd.Timestamp('1960-1-1')
    for x in range(len(dates)):
        dates[x]=pd.Timestamp(str(dates[x])[:11]+(df['itime'][x]))
    return dates

#Get the respective dates from stock symbol

def dates_df_from_directory(symbol):
    csv_file=dir_list[stock_symbols.index(symbol)]
    df = pd.read_csv(csv_file)
    dates= pd.Series(df['DATE'])
    dates = pd.to_timedelta(dates, unit='D') + pd.Timestamp('1960-1-1')
    for x in range(len(dates)):
        dates[x]=pd.Timestamp(str(dates[x])[:11]+(df['itime'][x]))
        
    return dates
