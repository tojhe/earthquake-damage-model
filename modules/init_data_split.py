import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def data_split():
    train_x = pd.read_csv('../data/train_values.csv')
    train_y = pd.read_csv('../data/train_labels.csv')
    print("Original training data loaded")

    x_train, x_test, y_train, y_test = train_test_split(train_x, train_y,
                                                        stratify=train_y['damage_grade'],
                                                        test_size = 0.1, random_state = 42)
    print("Data has been split")
    return x_train, x_test, y_train, y_test

if __name__ == "__main__":
    x_train, x_test, y_train, y_test = data_split()
    xtrain_path = input("Filename for training values (exclude .csv extension): ")
    ytrain_path = input("Filename for training target (exclude .csv extension): ")
    xtest_path = input("Filename for test values (exclude .csv extension): ")
    ytest_path = input("Filename for test target (exclude .csv extension): ")

    x_train.to_csv("../data/" + xtrain_path + ".csv", index=False)
    y_train.to_csv("../data/" + ytrain_path + ".csv", index=False)
    x_test.to_csv("../data/" + xtest_path + ".csv", index=False)
    y_test.to_csv("../data/" + ytest_path + ".csv", index=False)