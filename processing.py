import pickle
def predict(x):
    regr1_1 = pickle.load(open('regr1_1_model.pkl', 'rb'))
    regr1_2 = pickle.load(open('regr1_2_model.pkl', 'rb'))
    regr1_1_predict = regr1_1.predict(x)
    regr1_2_predict = regr1_2.predict(x)
    return regr1_1_predict, regr1_2_predict