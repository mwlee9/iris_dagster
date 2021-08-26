import pandas as pd
from dagster import solid
from sklearn.datasets import load_iris
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)

normalized_df = pd.DataFrame(normalize(df), columns=df.columns)

pca = PCA(n_components=4)
pca_normalized_df = pd.DataFrame(pca.fit_transform(normalized_df))

remote_storage_path = "./"
pca_normalized_df.to_csv(remote_storage_path + "pca.csv")

plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')