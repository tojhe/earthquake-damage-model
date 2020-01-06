import pandas as pd
import pickle
from mord import LogisticAT

def model_train(features, target):

    model_ordinal = LogisticAT(alpha=0, max_iter=100)  # alpha parameter set to zero to perform no regularisation
    model_ordinal.fit(features, target)

    return model_ordinal

if __name__=='__main__':
    xtrain_path = "../data/" + input("Read file path xtrain: ") + ".csv"
    ytrain_path = "../data/" + input("Read file path ytrain: ") + ".csv"
    model_train_path = "../model/" + input("Write file path model_train: ") + ".pkl"

    xtrain_pca = pd.read_csv(xtrain_path)
    ytrain = pd.read_csv(ytrain_path)

    # divide df into features matrix and target vector
    features = xtrain_pca.drop('building_id', axis=1)
    target = ytrain['damage_grade']

    model_train = model_train(features, target)

    # Save to model
    with open(model_train_path, 'wb') as file:
        pickle.dump(model_train, file)