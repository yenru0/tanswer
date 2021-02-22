import pickle


# to see Weight
if __name__ == '__main__':
    with open("preference/weight/W.pkl", 'rb') as f:
        X = pickle.load(f)

    print(X)
