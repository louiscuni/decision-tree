import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from metadata import *
from stataudit import *
from predicter_organ import *
from test_tree import *

def save_tree(t):
	with open('savelight.txt', 'wb') as f :
		mp = pickle.Pickler(f)
		mp.dump(t)

#data file name
n="census_income_test_light.csv" #very light file to test without too much loading
nn = "census_income_learn.csv" #file to train your tree
nnn = "census_income_test.csv" #file to test your tree

#tree file name
m = "save.txt" #tree saved with 5 floors
mm = "save2.txt" #tree saved with 6 floors
mmm = "savelight.txt" #tree saved with 3 floors

## To build a new tree ##
# df = makeDF(nn)
# t = makeTree(df, 3)
# save_tree(t)

## To test a tree ##
df = makeDF(nnn)
with open('savelight.txt', 'rb') as handle:
    t = pickle.load(handle)
test_tree2(t, df)




	
