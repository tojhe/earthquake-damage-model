import pandas as pd
import pickle
from mord import LogisticAT
from catboost import CatBoostClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV

def model_train(features, target, model = 'mordcat'):
    if model == 'mordcat':
        model_local = LogisticAT()
        param_grid = {'alpha':[0, 0.01, 0.05, 0.1, 0.3, 0.8, 1, 1.3], 'max_iter':[100]}
    elif model == 'catboost':
        model_local = CatBoostClassifier(loss_function='MultiClass', eval_metric='TotalF1')
        param_grid = {'l2_leaf_reg': [0.5, 1.0, 2.0, 3.0, 4.5, 5.0]}
    elif model == 'multinomialnb':
        model_local = MultinomialNB()
        param_grid = {'alpha': [0.1, 0.3, 0.5, 0.7, 0.9]}
    elif model == 'voting': # recursively trains base estimators
        mdcat = model_train(features, target, model='mordcat')
        catbst = model_train(features, target, model='catboost')
        mnb = model_train(features, target, model='multinomialnb')
        model_local = VotingClassifier(estimators=[('mdcat', mdcat), ('catbst', catbst), ('mnb', mnb)],
                                 voting='soft', weights=[1, 2, 1])
        model_local.fit(features, target)
        model_ordinal = model_local

    if model in ('mordcat', 'catboost', 'multinomialnb'):
        model_ordinal = GridSearchCV(model_local, cv= 5, param_grid= param_grid, n_jobs=4)
        if model == "multinomialnb":
            model_ordinal.fit(features.iloc[:, :-4], target)
        else:
            model_ordinal.fit(features, target)
        print ("Model trained")
        print (model_ordinal.best_params_)

    return model_ordinal

if __name__=='__main__':
    xtrain_path = "../data/" + input("Read file path xtrain: ") + ".csv"    # processed xtrain data with pca already done
    ytrain_path = "../data/" + input("Read file path ytrain: ") + ".csv"    # processed ytrain data with pca already done
    model_train_path = "../model/" + input("Write file path model_train: ") + ".pkl"

    model = input('Model type \n(mordcat/catboost/multinomialnb/voting): ')

    xtrain_pca = pd.read_csv(xtrain_path, index_col="building_id")
    ytrain = pd.read_csv(ytrain_path, index_col="building_id")

    # divide df into features matrix and target vector
    features = xtrain_pca.drop('building_id', axis=1)
    target = ytrain['damage_grade']
    model_train = model_train(features, target, model)

    # Save to model
    if input("save? y/n:") == 'y':
        with open(model_train_path, 'wb') as file:
            pickle.dump(model_train, file)

    print("Trained model exported")