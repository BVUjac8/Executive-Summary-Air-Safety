# Julia Cuellar
# DSC 640
# Executive Summary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Will use in Executive Summary
def read_file():
    air = pd.read_csv('air-safety.csv')
    print("Display data with null:\n", air.isnull())
    print("Display counts of null from data:\n", air.isnull().sum())
    print('Data:\n', air)
    # plt.hist(air)
    plt.title('Histogram of Air')
    # plt.show()


def read_file2():
    dom = pd.read_excel('Domestic Passenger Revenue as a Percent of Total System Revenue.xls', index_col=0)
    print("Display data with null:\n", dom.isnull())
    print("Display counts of null from data:\n", dom.isnull().sum())
    dom = dom.fillna(" ")
    print("Display data with replaced nulls:\n", dom)
    print("Display recounts of null from data:\n", dom.isnull().sum())
    print('Data:\n', dom)
    dom.to_csv('Domestic PR.csv')


def read_file3():
    fin = pd.read_csv('Financial_Results__1947-Present_Full_Data_data.csv')
    print("Display data with null:\n", fin.isnull())
    print("Display counts of null from data:\n", fin.isnull().sum())
    fin = fin.fillna(" ")
    print("Display data with replaced nulls:\n", fin)
    print("Display recounts of null from data:\n", fin.isnull().sum())
    print('Data:\n', fin)
    # plt.hist(fin)
    plt.title('Histogram of Financial Results')
    # plt.show()


def read_file4():
    inter = pd.read_excel('International Passenger Revenue as a Percent of Total System Revenue.xls', index_col=0)
    print("Display data with null:\n", inter.isnull())
    print("Display counts of null from data:\n", inter.isnull().sum())
    inter = inter.fillna(" ")
    print("Display data with replaced nulls:\n", inter)
    print("Display recounts of null from data:\n", inter.isnull().sum())
    print('Data:\n', inter)
    inter.to_csv('International PR.csv')


# Will use in Executive Summary
def read_file5():
    pas = pd.read_excel('Passenger Revenue -- Domestic Operations.xls', index_col=0)
    print("Display data with null:\n", pas.isnull())
    print("Display counts of null from data:\n", pas.isnull().sum())
    pas = pas.fillna(" ")
    print("Display data with replaced nulls:\n", pas)
    print("Display recounts of null from data:\n", pas.isnull().sum())
    print('Data:\n', pas)
    pas.to_csv('PR Domestic.csv')


# Will use in Executive Summary
def read_file6():
    pas = pd.read_excel('Passenger Revenue -- International Operations.xls', index_col=0)
    print("Display data with null:\n", pas.isnull())
    print("Display counts of null from data:\n", pas.isnull().sum())
    pas = pas.fillna(" ")
    print("Display data with replaced nulls:\n", pas)
    print("Display recounts of null from data:\n", pas.isnull().sum())
    print('Data:\n', pas)
    pas.to_csv('PR International.csv')


def read_file7():
    pas = pd.read_excel('Passenger Revenue -- Total System Operations.xls', index_col=0)
    print("Display data with null:\n", pas.isnull())
    print("Display counts of null from data:\n", pas.isnull().sum())
    pas = pas.fillna(" ")
    print("Display data with replaced nulls:\n", pas)
    print("Display recounts of null from data:\n", pas.isnull().sum())
    print('Data:\n', pas)
    pas.to_csv('PR Total.csv')


# Will use in Executive Summary
def read_file8():
    enp = pd.read_excel('System Total Enplaned Passengers.xls', index_col=0)
    print("Display data with null:\n", enp.isnull())
    print("Display counts of null from data:\n", enp.isnull().sum())
    enp = enp.fillna(" ")
    print("Display data with replaced nulls:\n", enp)
    print("Display recounts of null from data:\n", enp.isnull().sum())
    print('Data:\n', enp)
    enp.to_csv('Total Enplanned.csv')


if __name__ == "__main__":
    read_file()
    read_file2()
    read_file3()
    read_file4()
    read_file5()
    read_file6()
    read_file7()
    read_file8()