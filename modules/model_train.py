import pandas as pd
import pickle
from mord import LogisticAT
from catboost import CatBoostClassifier
from sklearn.model_selection import GridSearchCV

def model_train(features, target, model = 'mordcat'):
    if model == 'mordcat':
        model = LogisticAT()
        param_grid = {'alpha':[0, 0.01, 0.05, 0.1, 0.3, 0.8, 1, 1.3], 'max_iter':[100]}
    elif model == 'catboost':
        model = CatBoostClassifier(loss_function='MultiClass', eval_metric='TotalF1')
        param_grid = {'l2_leaf_reg': [0.5, 1.0, 2.0, 3.0, 4.5, 5.0]}

    model_ordinal = GridSearchCV(model, cv= 5, param_grid= param_grid, n_jobs=4)
    # model_ordinal = LogisticAT(alpha=0, max_iter=100)  # alpha parameter set to zero to perform no regularisation
    model_ordinal.fit(features, target)
    print ("Model trained")
    print (model_ordinal.best_params_)

    return model_ordinal

if __name__=='__main__':
    xtrain_path = "../data/" + input("Read file path xtrain: ") + ".csv"
    ytrain_path = "../data/" + input("Read file path ytrain: ") + ".csv"
    model_train_path = "../model/" + input("Write file path model_train: ") + ".pkl"
    model = input('Model type:')

    xtrain_pca = pd.read_csv(xtrain_path)
    ytrain = pd.read_csv(ytrain_path)

    # divide df into features matrix and target vector
    features = xtrain_pca.drop('building_id', axis=1)
    target = ytrain['damage_grade']
    model_train = model_train(features, target, model)

    # Save to model
    if input("save?") == 'y':
        with open(model_train_path, 'wb') as file:
            pickle.dump(model_train, file)

    print("Trained model exported")