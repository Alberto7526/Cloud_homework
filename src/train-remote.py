import os
import argparse
import pickle
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

import pickle
from azureml.core import Run

run = Run.get_context()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_path',
        type=str,
        default='.',
        help='Path to the training data'
    )

    args = parser.parse_args()
    print("===== DATA =====")
    print("DATA PATH: " + args.data_path)
    print("LIST FILES IN DATA PATH...")
    print(os.listdir(args.data_path))
    print("================")

    PATH = os.path.join(args.data_path, os.listdir(args.data_path)[0])
    print("================")
    print(f'DataPath: {PATH}')
    df = pd.read_csv(PATH, sep = ",")


    del df["Hoja"]

    Y = df["class"]
    X = df.drop(["class"], axis = 1)
   

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 11)

    nutrition_model = make_pipeline(StandardScaler(), LinearDiscriminantAnalysis()).fit(X_train, y_train)

    y_hat=nutrition_model.predict(X_test)

    run.log('Accuracy model', accuracy_score(y_test, y_hat))

    #Registro
    pkl_output_path = 'outputs/nutrition_model.pkl'
    with open(pkl_output_path, 'wb') as model_pkl:
        pickle.dump(nutrition_model, model_pkl)
    print('Finished Training')