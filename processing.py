import pickle
def predict(x):
    regr1_1 = pickle.load(open('regr1_1_model.pkl', 'rb'))
    regr1_2 = pickle.load(open('regr1_1_model.pkl', 'rb'))
    regr1_1_predict = regr1_1.predict(x)
    regr1_2_predict = regr1_1.predict(x)
    return regr1_1_predict, regr1_2_predict

'''
    # TEST SAMPLE
    test_X = np.array([0.35400458, 0.30046821, 0.34173371, 0.58132256, 0.18992045,
                       0.40323708, 0.28171864, 0.36879701, 0.10178524, 0.70299847,
                       0.], ndmin=2)
    # EXPECTED RESULT
    print(regr1_1.predict(test_X))
    # [73.22975439]'''