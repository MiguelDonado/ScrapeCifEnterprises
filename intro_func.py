import pandas as pd
import os


def get_file_xlsx():
    file = [f for f in os.listdir(".") if f.endswith(".xlsx")]
    return file[0]


def get_enterprises(file):
    df = pd.read_excel(file, usecols=[0], header=None)
    series = df.iloc[:, 0]
    return series.tolist()
