import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
def display_image(digit):
    #digit_image = digit.reshape(128)
    plt.imshow(digit, cmap=matplotlib.cm.binary)
    plt.axis("off")
    plt.show()

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits['data'],digits['target'], random_state=0)
print(X_train.shape, X_test.shape)
print(digits.target_names)
display_image(digits.images[100])
