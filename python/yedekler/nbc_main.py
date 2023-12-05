import numpy as np

def read_wine_data(filepath):
    D = np.genfromtxt(filepath, delimiter=",")
    y = D[:, 0].astype(np.int8)
    X = D[:, 1:]
    return X, y
    
if __name__ == '__main__':
    X, y = read_wine_data(data_folder + "wine.data")    
    print(X.shape)
    print(X)
    print(y)