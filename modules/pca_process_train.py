from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import pickle



def pca_this(df):
    struc_cols = df.filter(regex="^has_superstructure", axis=1).columns
    sec_cols = df.filter(regex="^has_secondary_use_", axis=1).columns

    X = df[struc_cols.append(sec_cols)]
    ss = StandardScaler().fit(X)
    Xs = ss.transform(X)
    Xs = pd.DataFrame(Xs, columns = X.columns.values)

    #fit PCA

    pca = PCA()
    pca.fit(Xs)

    #find eigenvectors / coefficients of PCs
    pd.DataFrame(pca.components_, columns=X.columns)

    #getting PC columns
    pcs = pca.transform(Xs)
    pcs = pd.DataFrame(pcs, columns=['PC'+str(i+1) for i in range(len(X.columns))], index=X.index)

    pcs_x = pcs.iloc[:,:4]
    pcs_x['building_id'] = df['building_id']

    return pcs_x, pca, ss

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
    objdf['building_id'] = df['building_id']

    dummy = pd.get_dummies(objdf[['building_id', 'geo_level_1_id', 'land_surface_condition', 'foundation_type',
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
    df = pd.read_csv(xtrain_path)
    pcs_x, pca_model, standardize_model = pca_this(df)
    num_dum = dummify(df)
    pd.merge(num_dum,pcs_x,how='inner',on='building_id').to_csv(mod_xtrain_path, index=False)
    with open(pca_model_path, 'wb') as pickle_file:
        pickle.dump(pca_model, pickle_file)
    with open(standardize_model_path, 'wb') as pickle_file:
        pickle.dump(standardize_model, pickle_file)