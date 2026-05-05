# 🚀 End-to-End MLOps Pipeline for Placement Prediction

## 📌 Overview

This project demonstrates a complete **end-to-end MLOps pipeline** for predicting student placement.
It covers the full lifecycle from **data versioning → model training → deployment → monitoring → CI/CD → containerization**.

---

## 🧠 Problem Statement

Predict whether a student will be placed based on features like:

* CGPA
* Internships
* Projects
* Skills

---

## 🏗️ Architecture

```
Data (DVC)
   ↓
Preprocessing
   ↓
Training (MLflow)
   ↓
Pipeline (Prefect)
   ↓
Model (model.pkl)
   ↓
API (FastAPI)
   ↓
Monitoring (Evidently)
   ↓
CI/CD (GitHub Actions)
   ↓
Docker Deployment
```

---

## ⚙️ Tech Stack

| Category               | Tools          |
| ---------------------- | -------------- |
| Data Versioning        | DVC            |
| Experiment Tracking    | MLflow         |
| Pipeline Orchestration | Prefect        |
| Backend API            | FastAPI        |
| Monitoring             | Evidently AI   |
| CI/CD                  | GitHub Actions |
| Containerization       | Docker         |

---

## 📂 Project Structure

```
mlops-placement/
│
├── data/
│   ├── placement.csv.dvc
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── pipeline.py
│   ├── monitor.py
│
├── app/
│   └── main.py
│
├── Dockerfile.app
├── Dockerfile.monitor
├── requirements.txt
├── requirements-monitor.txt
├── .github/workflows/ci.yaml
└── README.md
```

---

## 🔁 Workflow Explanation

### 1. Data Versioning

* Managed using DVC
* Dataset changes are tracked via `.dvc` files

---

### 2. Pipeline Execution (Prefect)

```bash
python -m src.pipeline
```

* Automates preprocessing + training
* Ensures reproducibility

---

### 3. Model Tracking (MLflow)

* Logs parameters, metrics, and models
* Stores experiment runs in `mlruns/`

---

### 4. API Deployment (FastAPI)

```bash
uvicorn app.main:app --reload
```

Access API:

```
http://127.0.0.1:8000/docs
```

---

### 5. Monitoring (Evidently)

```bash
python src/monitor.py
```

Output:

```
report.html
```

* Detects data drift
* Compares reference vs current data

---

### 6. CI/CD (GitHub Actions)

* Automatically runs on every push
* Validates dependencies and environment

---

### 7. Docker Usage

#### Run App Container

```bash
docker build -t mlops-app -f Dockerfile.app .
docker run -p 8000:8000 mlops-app
```

#### Run Monitoring Container

```bash
docker build -t mlops-monitor -f Dockerfile.monitor .
docker run -v %cd%:/app mlops-monitor
```

---

## ⚠️ Important Notes

* Dataset is managed using DVC and not stored directly in Git
* Generated files like `model.pkl`, `mlruns/`, and `report.html` are ignored
* Monitoring and pipeline run in separate environments due to dependency conflicts

---

## 🧠 Key Learnings

* End-to-end MLOps workflow design
* Data versioning using DVC
* Workflow orchestration using Prefect
* Model deployment with FastAPI
* Monitoring using Evidently
* CI/CD automation
* Containerization with Docker

---

## 🎯 Future Improvements

* Add cloud deployment (AWS/GCP)
* Integrate real-time data pipeline
* Use Prometheus + Grafana for monitoring
* Add model retraining triggers

---

## 👩‍💻 Author

**Siddhi Daphal**

---

## ⭐ Conclusion

This project demonstrates how to build a **production-ready MLOps system** by integrating multiple tools to ensure scalability, reproducibility, and monitoring.
