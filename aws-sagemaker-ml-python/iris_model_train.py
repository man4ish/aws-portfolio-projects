import argparse
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_estimators', type=int, default=100)
    args = parser.parse_args()

    # Load training data
    input_path = os.path.join('/opt/ml/input/data/train', 'iris.csv')
    df = pd.read_csv(input_path)
    X = df.drop('target', axis=1)
    y = df['target']

    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=args.n_estimators)
    model.fit(X_train, y_train)

    # Evaluate and log
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test Accuracy: {acc:.4f}")

    # Save the model
    model_path = os.path.join('/opt/ml/model', 'model.joblib')
    joblib.dump(model, model_path)
