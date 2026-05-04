import mlflow
import mlflow.sklearn
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from preprocessing import load_data, preprocess

# Set experiment
mlflow.set_experiment("placement_prediction")

# Load + preprocess
df = load_data()
X, y = preprocess(df)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

with mlflow.start_run():

    # Model
    model = RandomForestClassifier(n_estimators=50)
    model.fit(X_train, y_train)

    # Accuracy
    acc = model.score(X_test, y_test)

    # Log to MLflow
    mlflow.log_param("n_estimators", 50)
    mlflow.log_metric("accuracy", acc)

    mlflow.sklearn.log_model(model, "model")

    # Save locally
    joblib.dump(model, "model.pkl")

    print("Model trained")
    print("Accuracy:", acc)