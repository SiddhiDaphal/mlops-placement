from prefect import task, flow
from src.preprocessing import load_data, preprocess
from src.train import train_model   # 👈 IMPORT YOUR UPDATED TRAIN FILE

@task
def preprocess_task():
    df = load_data()
    X, y = preprocess(df)
    return X, y

@task
def train_task(X, y):
    train_model(X, y)   # 👈 CALL YOUR MLflow MULTI-MODEL CODE

@flow
def ml_pipeline():
    X, y = preprocess_task()
    train_task(X, y)

if __name__ == "__main__":
    ml_pipeline()