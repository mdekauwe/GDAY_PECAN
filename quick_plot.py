#!/usr/bin/env python

""" run GDAY, plot LAI, GPP, shoot NC """

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import plot_settings as ps
import pandas as pd
import datetime as dt

__author__  = "Martin De Kauwe"
__version__ = "1.0 (16.05.2013)"
__email__   = "mdekauwe@gmail.com"

def date_converter(*args):
    print(*args[0])
    return dt.datetime.strptime(str(int(float(args[0]))) + " " +\
                                str(int(float(args[1]))), '%Y %j')

def read_data(fname):
    df = pd.read_csv(fname, sep=",",
                     na_values=["-999.9"], skiprows=1)
    return df


def main():

    df = read_data("outputs/US-NR1_simulation.csv")

    plt.rcParams['font.sans-serif'] = "Helvetica"
    plt.rcParams['legend.fontsize'] = 9
    fig = plt.figure()

    ax = fig.add_subplot(311)

    ax.plot(df["gpp"]*100, "r-", label="Amb")
    ax.plot(df["gpp"]*100, "g-", label="Ele")
    ax.legend(numpoints=1, loc="best")
    ax.set_ylabel("GPP")
    ax.set_ylim(0, 20)

    ax = fig.add_subplot(312)
    ax.plot(df["lai"], "r-", label="Amb")
    ax.plot(df["lai"], "g-", label="Ele")
    ax.legend(numpoints=1, loc="best")
    ax.set_ylabel("LAI")
    ax.set_ylim(0, 4)

    ax = fig.add_subplot(313)
    ax.plot(df["pawater_root"], "r-", label="Amb")
    ax.plot(df["pawater_root"], "g-", label="Ele")
    ax.legend(numpoints=1, loc="best")
    ax.set_ylabel("Soil Water (mm)")


    plt.show()

if __name__ == "__main__":

    main()
