import numpy as np

def pd_to_score(pd, A=600, B=50):
    return A - B * np.log(pd / (1 - pd))
