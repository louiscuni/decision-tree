import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from metadata import *

def makeDF (name_file):#build a dataframe from a file
	path = os.path.dirname(os.getcwd())
	df=pd.read_csv(path+"/us_census_full/"+name_file, names = name_col, header = 0)
	return df

def value_possible(col):#return a list a possible value from a dataframe's column
	res = []
	index = 0
	for i in col :
		if not(i in res) : 
			res.append(i)
	return res

def hist_1D (df):#print a histogram for each column of a dataframe
	nb = 0
	for i in df.columns :
		if i != 'weight':#too much value in weight
			print(i, " (", nb,")")
			nb+=1
			col = df.get(i)
			nbv = value_possible(col)
			hist = plt.hist(col, bins = len(nbv), normed = False)
			res = fusion(nbv, hist[0])
			print(res)
			print("####")
			return res
		else :
			print("ingore weight (", nb, ")" )
			nb+=1
			print("####")

def ordhist(hist): 
	l = sorted(hist, key = lambda data: data[1])
	return l[::-1]

def fusion(l1, l2): #return a list of tuple 
	res = []
	for i in range(len(l1)):
		res.append((l1[i], l2[i]))
	return res

def hardcol(df):#return a list of column that have too much value
	res = []
	for i in df.columns :
		if i != 'weight' and len(value_possible(df[i])) > 10000 and i != 'label':
			res.append(i)
			print (i," has too much values possible")
	return res

def reducecol(col, n):#return an ordered list of the most frequent value of a column
	res = []
	vp = value_possible(col)
	h = plt.hist(col, bins = len(vp), normed = False)
	H = fusion(vp, h[0])
	H = ordhist(H)
	for i in range(n) :
		res.append(H[i][0])
	return res

def reducecolhard (df, hardcl):#return a dictionary with in index names of column and the most frequent value of those
	res = {}
	n = 25
	for i in hardcl :
		print("reducing ", i)
		lem = reducecol(df[i], n)
		res[i] = lem
		print(i," has been reduced to ", len(lem), " values")
	return res

def reduceDF (df) :
	hc = hardcol(df)
	return reducecolhard(df, hc) 


n="census_income_test_light.csv"
nn = "census_income_learn.csv"


