import numpy as np

def MAPE(y,p):
    return np.mean(
        np.abs((y-p)/(y+1e-8))
    )

def RMSE(y,p):
    return np.sqrt(
        np.mean((y-p)**2)
    )