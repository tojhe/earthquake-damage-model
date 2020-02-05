from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import pandas as pd
import pickle


def pca_this(df):
    '''
    Transforms features for "has_superstructure" and "has_secondary_use_" into 4 Principal Components
    :param df: Dataframe of predictors
    :return: pcs -> DataFrame of 4 Principal Components
            pca -> fitted PCA model
    '''
    sel_cols = df.filter(regex="^has_superstructure|^has_secondary_use_", axis=1).columns

    # ---- standard scaler deprecated ----- #
    # X = df[sel_cols]
    # ss = StandardScaler().fit(X)
    # Xs = ss.transform(X)
    # Xs = pd.DataFrame(Xs, columns = X.columns.values)
    # ------------------------------------- #

    #fit PCA
    X = df[sel_cols]
    pca = PCA(n_components = 4, random_state = 42)
    pca.fit(X)

    #find eigenvectors / coefficients of PCs
    pd.DataFrame(pca.components_, columns=X.columns)

    #getting PC columns
    pcs = pca.transform(X)
    pcs = pd.DataFrame(pcs, columns=['PC'+str(i+1) for i in range(4)], index=X.index)

    return pcs, pca

def dummify(df):
    '''
    Dummy codes selected features from predictor DataFrame
    :param df: Dataframe of predictors
    :return: Dataframe with dummy codes and selected numeric features
    (Processed Principal Components,"has_superstructure" and "has_secondary_use_" features are excluded)
    '''

    numdf = df[['count_floors_pre_eq','age','area_percentage','height_percentage','count_families']]

    # replace categories in original dataframe with less than 5% of dataframe len with Others for credible sample size and limit no. of dummies
    df['geo_level_1_id'] = df['geo_level_1_id'].astype('O')
    objdf = df.select_dtypes('O')
    for col in objdf.columns:
        otherls = []
        for i, e in objdf[col].value_counts().items():
            if e < 0.05 * len(df):
                otherls.append(i)
        objdf.loc[objdf[col].isin(otherls), col] = 'Others'

    dummy = pd.get_dummies(objdf[['geo_level_1_id', 'land_surface_condition', 'foundation_type',
                                  'roof_type', 'ground_floor_type', 'plan_configuration', 'position']],
                           columns=['geo_level_1_id', 'land_surface_condition', 'foundation_type',
                                    'roof_type', 'ground_floor_type', 'plan_configuration', 'position'], drop_first=True,)
    num_dum = pd.merge(numdf,dummy,how='inner',left_index=True, right_index=True)
    return num_dum

def scaler(df):
    mm_scaler = MinMaxScaler()
    df[['age','PC1', 'PC2', 'PC3', 'PC4']] = mm_scaler.fit_transform(df[['age', 'PC1', 'PC2', 'PC3', 'PC4']])
    return df, mm_scaler

if __name__=='__main__':
    xtrain_path = "../data/" + input("Read file path xtrain: ") + ".csv"
    mod_xtrain_path = "../data/xtrain_pca_2.csv"
    pca_model_path = "../model/pca_model_2.pkl"
    scaler_model_path = "../model/scaler_model.pkl"

    df = pd.read_csv(xtrain_path, index_col="building_id")

    pcs, pca_model = pca_this(df)
    num_dum = dummify(df)

    df_merged = pd.merge(num_dum,pcs,how='inner',right_index=True, left_index=True)
    df_merged, mm_scaler = scaler(df_merged)
    df_merged.to_csv(mod_xtrain_path)

    print ("PCA training values exported")
    with open(pca_model_path, 'wb') as pickle_file:
        pickle.dump(pca_model, pickle_file)
    with open(scaler_model_path, 'wb') as pickle_file:
        pickle.dump(mm_scaler, pickle_file)