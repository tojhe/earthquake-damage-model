import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mord import LogisticAT
from pca_process_train import dummify

#pre-process test set
def preprocess(df, pickle_standardize, pickle_pca):
    '''
    pickle_standardize: fitted Standard Scaler object loaded from pickle (sklearn StandardScaler object)
    pickle_pca: fitted PCA object loaded from pickle (sklearn PCA object)
    '''
    #pca superstructure and secondary use data
    sel_cols = df.filter(regex="^has_superstructure|^has_secondary_use_", axis=1).columns
    Xs = pickle_standardize.transform(df[sel_cols])
    Xs = pd.DataFrame(Xs, columns = sel_cols.values)

    pcs = pickle_pca.transform(Xs)
    pcs = pd.DataFrame(pcs, columns=['PC'+str(i+1) for i in range(4)], index=df[sel_cols].index)
    pcs_x = pcs.iloc[:,:4]
    pcs_x['building_id'] = df['building_id']

    #get numeric columns and dummy object columns
    num_dum = dummify(df)
    num_dum['building_id'] = df['building_id']
    x_test_clean = pd.merge(num_dum,pcs_x,how='inner',on='building_id')

    #create dummy values of test set has less features than training
    xtrain_cols = ['building_id', 'count_floors_pre_eq', 'age', 'area_percentage',\
    'height_percentage', 'count_families', 'geo_level_1_id_6',\
    'geo_level_1_id_7', 'geo_level_1_id_8', 'geo_level_1_id_10',\
    'geo_level_1_id_17', 'geo_level_1_id_20', 'geo_level_1_id_21',\
    'geo_level_1_id_26', 'geo_level_1_id_Others',\
    'land_surface_condition_n', 'land_surface_condition_t',\
    'foundation_type_r', 'foundation_type_u', 'foundation_type_w',\
    'roof_type_q', 'roof_type_x', 'ground_floor_type_f',\
    'ground_floor_type_v', 'ground_floor_type_x', 'plan_configuration_d',\
    'position_j', 'position_s', 'position_t', 'PC1', 'PC2', 'PC3', 'PC4']
    # Get missing columns in the training test
    missing_cols = [col for col in xtrain_cols if col not in x_test_clean.columns]
    # Add a missing column in test set with default value equal to 0
    for c in missing_cols:
        x_test_clean[c] = 0
    # Ensure the order of column in the test set is in the same order than in train set
    x_test_clean = x_test_clean[xtrain_cols]
    return x_test_clean

#model prediction
def model_predict(pickle_model, x_test_clean):
    predictions = pickle_model.predict(x_test_clean.drop('building_id', axis=1))
    pred_df = pd.DataFrame(predictions, columns = ['prediction'])
    pred_df['building_id'] = x_test_clean['building_id']
    pred_df = pred_df[['building_id','prediction']]

    pred_df.columns = ['building_id', 'damage_grade']
    #write prediction to csv
    pred_df.to_csv("../data/predictions.csv", index=False)

    return pred_df

def check_pred_acc(y_test, pred_df):
    print("Model accuracy score:", accuracy_score(y_test['damage_grade'], pred_df['prediction']))
    print("Model F1 score:", f1_score(y_test['damage_grade'], pred_df['prediction'], average='micro'))
    print("Baseline score:", max(y_test['damage_grade'].value_counts()/len(y_test['damage_grade'])))

if __name__=='__main__':
    x_test_path = "../data/" + input("Read file path xtest: ") + ".csv"
    y_test_path = "../data/" + input("Read file path ytest, press enter if not present: ") + ".csv"
    model_path = "../model/" + input("Read file path for trained model: ") + ".pkl"


    # import test set
    x_test = pd.read_csv(x_test_path)
    try:
        y_test = pd.read_csv(y_test_path)
    except FileNotFoundError:
        print ("No such file")

    #import models
    # pickle_model_filename = "../model/model_train.pkl"
    pickle_pca_filename = "../model/pca_model.pkl"
    standardize_filename = "../model/standardize_model.pkl"
    with open(model_path, 'rb') as file:
        pickle_model = pickle.load(file)
    with open(pickle_pca_filename, 'rb') as file:
        pickle_pca = pickle.load(file)
    with open(standardize_filename, 'rb') as file:
        pickle_standardize = pickle.load(file)

    #preprocess
    x_test_clean = preprocess(x_test, pickle_standardize, pickle_pca)
    #predictions
    pred_df = model_predict(pickle_model, x_test_clean)
    #accuracy score
    if y_test_path != "../data/.csv":
        check_pred_acc(y_test, pred_df)
    else:
        pass
