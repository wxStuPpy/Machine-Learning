from sklearn.cluster import KMeans
import  matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import  calinski_harabasz_score

def func():
    x,y=make_blobs(n_samples=1000,n_features=2,centers=[[-1,-1],[0,0],[1,1],[2,2]],cluster_std=[0.4,0.2,0.2,0.2],random_state=10)
    plt.figure()

