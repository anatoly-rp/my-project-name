import numpy as np
import pickle
def data_preparation(list):
    x = np.array(list).reshape(1,-1)
    my_mms = pickle.load(open('my_mms.pkl', 'br'))
    x = my_mms.transform(x)
    return x