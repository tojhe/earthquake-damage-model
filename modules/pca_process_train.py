from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import pandas as pd
import pickle



def pca_this(df):
    sel_cols = df.filter(regex="^has_superstructure|^has_secondary_use_", axis=1).columns

    # ---- standard scaler deprecated ----- #
    # X = df[sel_cols]
    # ss = StandardScaler().fit(X)
    # Xs = ss.transform(X)
    # Xs = pd.DataFrame(Xs, columns = X.columns.values)
    # ------------------------------------- #




    #fit PCA

    pca = PCA(n_components = 4, random_state = 42)
    pca.fit(Xs)

    #find eigenvectors / coefficients of PCs
    pd.DataFrame(pca.components_, columns=X.columns)

    #getting PC columns
    pcs = pca.transform(Xs)
    pcs = pd.DataFrame(pcs, columns=['PC'+str(i+1) for i in range(4)], index=X.index)
    pcs['building_id'] = df['building_id']

    return pcs, pca, ss

def dummify(df):
    numdf = df[['building_id','count_floors_pre_eq','age','area_percentage','height_percentage','count_families']]

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
    num_dum = pd.merge(numdf,dummy,how='inner',on='building_id')
    return num_dum

if __name__=='__main__':
    xtrain_path = "../data/" + input("Read file path xtrain: ") + ".csv"
    mod_xtrain_path = "../data/xtrain_pca.csv"
    pca_model_path = "../model/pca_model.pkl"
    standardize_model_path = "../model/standardize_model.pkl"

    df = pd.read_csv(xtrain_path, index_col="building_id")
    pcs, pca_model, standardize_model = pca_this(df)
    num_dum = dummify(df)
    pd.merge(num_dum,pcs,how='inner',right_index=True, left_index=True).to_csv(mod_xtrain_path)
    print ("PCA training values exported")
    with open(pca_model_path, 'wb') as pickle_file:
        pickle.dump(pca_model, pickle_file)
    with open(standardize_model_path, 'wb') as pickle_file:
        pickle.dump(standardize_model, pickle_file)