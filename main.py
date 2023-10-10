import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
# Displays image of digit to user
def display_image(digit):
    #digit_image = digit.reshape(128)
    plt.imshow(digit, cmap=matplotlib.cm.binary)
    plt.axis("off")
    plt.show()

digits = load_digits()
# Split dataset into test and train
X_train, X_test, y_train, y_test = train_test_split(digits['data'],digits['target'], random_state=0)

# K Nearest Neighbour setup
knn = KNeighborsClassifier(n_neighbors=10) # Need to test value of k, 10 for now
# adding training data
knn.fit(X_train, y_train)


