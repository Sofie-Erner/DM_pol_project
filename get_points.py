"""
This script takes in data for background or signal.

- Input:
Path to data file
The data needs to be structured into rows, where rows represent increasing CMS energy.
Columns represent cos-theta, and each value is the # entries per bin.

- Output:
Set of data points which will be used for regression
"""

import numpy as np
import sys
import os
import pandas

# ---------- Variables ----------
# --- Energy & Theta Values
Emin = 1.8 # mininum energy
Emax = 5.8 # maximum energy
d_E = 0.1 # delta for enery
E_vals = np.arange(Emin,Emax+d_E,d_E) # energy values list

tmin = 10 # minimum cos-theta
tmax = 160 # maximum cos-theta
d_t = 1 # delta for cos-theta

theta_vals = np.arange(tmin,tmax+d_t,d_t) # cos-theta values list

# --- Others
L = 20 # luminosity 20 fb^-1 50*10**3 

# ---------- Command Line Arguments ----------
if ( len(sys.argv) < 2 ): # less than two command line arguments
    print("Error: Not correct number of command line arguments")
    quit()

direc = sys.argv[1] # directory path
file = sys.argv[2] # data file

# ---------- Import file
df = pandas.read_csv(os.path.join(direc, file),sep=" ",header=None)
df = df.loc[:,df.notna().any(axis=0)] # remove column with NaN

rows, cols = df.shape
if (rows != len(E_vals)) and (cols != len(theta_vals)):
    print("Error: wrong dimensions of data")
    quit()

print("test")
