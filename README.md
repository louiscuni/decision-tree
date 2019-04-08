# **Decision Tree**
a decision tree to predict salary

## Installation 
* clone the repository 
* in the main file, you will find every thing necessary to
    * launch a statistical audit
    * build a new tree 
    * test a new tree

## Files 
* **main** :
    regroup elementary fonctions to make a statistical audit, build a new tree and test a tree. 
* **stataudit** :
    regroup the basic functions for statistic audition
* **predicter_organ**
    regroup every functions to build a decision tree
* **test_tree**
    regroup every functions to test a decision tree
* **metadata**
    A big list with all the columns names
* **tree**
    The source code of the node class that is used to build trees

## Results

With my bigest tree (6 floors), I had an accuracy of 92% (F1-score around 0.30) wich is not good considering that a predictor that would only predict "-50000" would get 94% . I think it is due to the fact that i don't use correctly nominal data and because of the tree size.


