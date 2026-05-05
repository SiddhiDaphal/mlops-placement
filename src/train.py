import mlflow
import mlflow.sklearn
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


def train_model(X, y):

    # Set experiment
    mlflow.set_experiment("placement_prediction")

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Models
    models = {
        "RandomForest": RandomForestClassifier(n_estimators=50),
        "LogisticRegression": LogisticRegression(),
        "DecisionTree": DecisionTreeClassifier()
    }

    best_model = None
    best_score = 0

    for name, model in models.items():

        with mlflow.start_run(run_name=name):

            # Train
            model.fit(X_train, y_train)

            # Evaluate
            acc = model.score(X_test, y_test)

            # Log
            mlflow.log_param("model", name)
            mlflow.log_metric("accuracy", acc)

            mlflow.sklearn.log_model(model, "model")

            print(f"{name} Accuracy: {acc}")

            # Save best model
            if acc > best_score:
                best_score = acc
                best_model = model

    # Save best model
    joblib.dump(best_model, "model.pkl")

    print("Best model saved with accuracy:", best_score)