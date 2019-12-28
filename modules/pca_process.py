from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd



def pca_this(df):
    struc_cols = df.filter(regex="^has_superstructure", axis=1).columns
    sec_cols = df.filter(regex="^has_secondary_use_", axis=1).columns

    X = df[struc_cols.append(sec_cols)]
    Xs = StandardScaler().fit_transform(X)
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

    return pcs_x

def dummify(df):
    numdf = df[['building_id','count_floors_pre_eq','age','area_percentage','height_percentage','count_families']]
    dummy = pd.get_dummies(df[['building_id','geo_level_1_id']],columns = ['geo_level_1_id'], drop_first = True, prefix= 'geo')
    num_dum = pd.merge(numdf,dummy,how='inner',on='building_id')

    return num_dum

if __name__=='__main__':
    xtrain_path = "../data/" + input("Read file path: ") + ".csv"
    mod_xtrain_path ="../data/" + input("Write file path: ") + ".csv"
    df = pd.read_csv(xtrain_path)
    pcs_x = pca_this(df)
    num_dum = dummify(df)
    pd.merge(num_dum,pcs_x,how='inner',on='building_id').to_csv(mod_xtrain_path, index=False)