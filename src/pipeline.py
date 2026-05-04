from prefect import task, flow
from src.preprocessing import load_data, preprocess

import joblib

@task
def preprocess_task():
    df = load_data()
    X, y = preprocess(df)
    return X, y

@task
def train_task(X, y):
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=50)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    joblib.dump(model, "model.pkl")

    print("Accuracy:", acc)

@flow
def ml_pipeline():
    X, y = preprocess_task()
    train_task(X, y)

if __name__ == "__main__":
    ml_pipeline()