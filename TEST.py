# this is for testing the code in the notebook, not for production use.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix



# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print ("Features shape:", X.shape)
print ("Labels shape:", y.shape)


