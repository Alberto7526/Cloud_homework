import os
import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


if __name__ == "__main__":  
    
    PATH = os.path.join('..', 'data', 'nutrition.csv')
    df = pd.read_csv(PATH, sep = ",")
    
    del df["Hoja"]

    Y = df["class"]
    X = df.drop(["class"], axis = 1)
   

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 11)

    X_test.to_csv('../data/x_test.csv')
    y_test.to_csv('../data/y_test.csv')

    nutrition_model = make_pipeline(StandardScaler(), LinearDiscriminantAnalysis()).fit(X_train, y_train)

    y_hat=nutrition_model.predict(X_test)

    print(f"Precisión del modelo: {accuracy_score(y_test, y_hat)}")

    #Registro
    OUTPUT_PATH = os.path.join('..', 'outputs', 'nutrition_model.pkl')
    with open(OUTPUT_PATH, 'wb') as model_pkl:
        pickle.dump(nutrition_model, model_pkl)
