import pickle
import tree
import random

def tree_print (t):
	if t.nature == 'feuille' or t.nature == 'feuille impure' :
		print ("*** ",t.value)
	else :
		print (t.value)
		tree_print(t.leftson)
		tree_print(t.rightson)

def read_tree2 (t, df):#run the tree with a row from a dataframe
	random.seed()
	res = {"TP":0, "FP":0, "TN":0, "FN":0}
	#print ("plop")
	if t.nature == 'feuille' :
		#print ("************ label ", df['label'], " feuille ", t.value )
		if t.value == df['label']:
			#print("***! TRUE !")
			if df['label'] == ' 50000+.':
				res["TP"]+=1
			else :
				res["TN"]+=1
		else :
			#print ("***!!!! FALSE !!!***")
			if df['label'] == ' 50000+.':
				res["FP"]+=1
			else :
				res["FN"]+=1
		#print (res)
		return res
	elif t.nature == 'feuille impure':
		rand = random.random()
		#print ("ùùù! random ", rand, " against ", t.value )
		if rand > t.value:
			if df['label'] != ' 50000+.' :
				#print("***! TRUE !")
				res["TN"]+=1
			else :
				res["FN"]+=1
				#print ("***!!!! FALSE !!!***")
		else :
			if df['label'] == ' 50000+.' :
				#print("***! TRUE !")
				res["TP"]+=1
			else :
				#print ("***!!!! FALSE !!!***")
				res["FP"]+=1
		return res
	else :
		if type(df[t.value[0]]) == type('str'):
			#print ("is ", df[t.value[0]], " = ", t.value[1])
			if df[t.value[0]] == t.value[1]:
				#print(" yes")
				return read_treee(t.leftson, df)
			else:
				#print(" no")
				return read_treee(t.rightson, df)
		else :
			#print ("is ", df[t.value[0]], " > ", t.value[1])
			if df[t.value[0]] > t.value[1]:
				#print(" yes")
				return read_treee(t.leftson, df)
			else:
				#print(" no")
				return read_treee(t.rightson, df)

def test_tree2 (t, df):#test a decision tree and return accuracy, recall, precision et F1 score
	TP = 0.0
	TN = 0.0
	FP = 0.0
	FN = 0.0
	c = 1
	for i in df.index :
		r = read_tree2(t, df.iloc[i])
		TP += r["TP"]
		TN += r["TN"]
		FP += r["FP"]
		FN += r["FN"]
		print (c) #loading status
		c+=1

	print ("TP ", TP, "TN ", TN, "FP ", FP, "FN ", FN)
	a = (TP+TN)/(TP+TN+FP+FN)
	if TP >0 :
		p = TP/(TP+FN)
		re = TP/(TP+FP)
	else :
		p = 0
		re = 0 
	print ("accuracy : ", a)
	print ("precision : ", p)
	print ("recall : ", re)
	if p+re >0 :
		print ("F1 score : ", 2*(re*p)/(p+re))