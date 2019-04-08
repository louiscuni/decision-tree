import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math 
from metadata import *
from stataudit import *
from tree import *

def gain_info_smart(df,col, val):#return entropy's weighted average
	carddf = df.index.size*1.0

	if df[col].dtypes == 'int64' or df[col].dtypes == 'float64' :
		df_Trou = df.loc[df[col] > val]
		df_noTrou = df.loc[df[col] <= val]
	else :
		df_Trou = df.loc[lambda df: df[col] == val]
		df_noTrou = df.loc[lambda df: df[col] != val]

	cardTrou = df_Trou.index.size*1.0
	cardnoTrou = df_noTrou.index.size*1.0

	pTrou = df_Trou.loc[ lambda df: df['label'] == ' 50000+.'].index.size*1.0
	pnoTrou = df_noTrou.loc[ lambda df: df['label'] == ' 50000+.'].index.size*1.0 

	return (cardTrou/carddf)*entropy(pTrou, cardTrou)+(cardnoTrou/carddf)*entropy(pnoTrou, cardnoTrou)

def entropy(proportion, cardinal):#return dataframe's entropy
	if cardinal == 0 :#cas extreme : pour des valeurs numeriques : plus grand que le max
		return 0
	p = proportion/cardinal
	q = 1-p
	if p == 0 or q == 0:
		return 0
	try :
		res = -1*p*math.log(p, 2)-q*math.log(q, 2)
	except :
		print("pro ", proportion, " car ", cardinal)
		
	return res

def detMval (df, col, dico):#return the best value to maximize gain information with a given column 
	E = entropy(df.loc[ lambda df: df['label'] == ' 50000+.'].index.size*1.0, df.index.size*1.0)
	if col in dico.keys() :
		vals = dico[col]
	else :
		vals = value_possible(df[col])
	res = (-10.0, "plop")
	for i in vals :
		lem = gain_info_smart(df, col, i)
		lem = E - lem
		print(lem)
		if lem > res[0] :
			res = (lem, i)
	return res #tuple (gain information, val seuil)

def detCrit (df, dico ):#return a column and a value in order to maximize gain information 
	res = ('col', (0, 'plop'))
	for i in df.columns :
		if i != 'label' and i != 'weight':
			print("***** ", i, "\n")
			lem = (i, detMval(df, i, dico))
			if lem[1][0] > res[1][0] :
				res = lem
	print(res[1][0])
	return (res[0], res[1][1]) #tuple (column, val seuil)

def makeTree (df, profondeur):#build a decision tree
	p = df.loc[ lambda df: df['label'] == ' 50000+.'].index.size*1.0
	c = df.index.size*1.0
	E = entropy(p, c)
	if E == 0 :
		return node(0, ' ', ' ', 'feuille', df.iat[0,41] )
	elif profondeur == 0 :
		p = df.loc[ lambda df: df['label'] == ' 50000+.'].index.size*1.0
		c = df.index.size*1.0
		return node(0, ' ', ' ', 'feuille impure', p/c )
	else :
		d = reduceDF(df)
		C = detCrit(df, d)
		df_l, df_r = split (df, C)
		return node(0, makeTree(df_l, profondeur-1), makeTree(df_r, profondeur-1), 'node', C)
		
def split (df, C):#cut a dataframe with a condition C and return the couple
	print("type split ", df[C[0]].dtypes)
	if df[C[0]].dtypes == 'int64' or df[C[0]].dtypes == 'float64' :
		print("it's int !")
		df_Trou = df.loc[df[C[0]] > C[1]]
		df_noTrou = df.loc[df[C[0]] <= C[1]]
	else :
		df_Trou = df.loc[lambda df: df[C[0]] == C[1]]
		df_noTrou = df.loc[lambda df: df[C[0]] != C[1]]
	return (df_Trou, df_noTrou)



