# 🎯 MLOps Placement Prediction Project

## 📌 Overview

This project demonstrates a complete **MLOps pipeline** for predicting student placement outcomes based on academic and skill-related features.

It covers the **end-to-end lifecycle**:

* Data Versioning
* Model Training
* Experiment Tracking
* Pipeline Orchestration
* API Deployment
* CI/CD Automation
* Model Monitoring

---

## 🚀 Tech Stack

| Component           | Tool Used      |
| ------------------- | -------------- |
| Data Versioning     | DVC            |
| Experiment Tracking | MLflow         |
| Pipeline            | Prefect        |
| Model               | Random Forest  |
| API                 | FastAPI        |
| CI/CD               | GitHub Actions |
| Containerization    | Docker         |
| Monitoring          | Evidently AI   |

---

## 📂 Project Structure

```
mlops-placement/
│
├── data/                  # Dataset (tracked via DVC)
├── src/                   # ML pipeline code
│   ├── preprocessing.py
│   ├── train.py
│   ├── pipeline.py
│   ├── monitor.py
│
├── app/                   # FastAPI app
│   └── main.py
│
├── .github/workflows/     # CI/CD pipeline
├── Dockerfile             # Containerization
├── requirements.txt       # Dependencies
├── report.html            # Monitoring report (Evidently)
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/mlops-placement.git
cd mlops-placement
```

---

### 2️⃣ Create Environment

```bash
conda create -n mlops_env python=3.9
conda activate mlops_env
pip install -r requirements.txt
```

---

### 3️⃣ Run Training Pipeline

```bash
python src/pipeline.py
```

---

### 4️⃣ Run API

```bash
uvicorn app.main:app --reload
```

👉 Open:
http://127.0.0.1:8000/docs

---

### 5️⃣ Generate Monitoring Report

```bash
python src/monitor.py
```

👉 Open:

```
report.html
```

---

## 📊 Monitoring

This project uses **Evidently AI** to:

* Detect **data drift**
* Compare **training vs current data**
* Generate **HTML reports**

📌 Output:

```
report.html
```

---

## 🔄 CI/CD Pipeline

* Triggered on every push
* Installs dependencies
* Runs project checks

📍 Located in:

```
.github/workflows/ci.yml
```

---

## 🐳 Docker Support

Build image:

```bash
docker build -t mlops-app .
```

Run container:

```bash
docker run -p 8000:8000 mlops-app
```

---

## 📌 Key Features

✔ End-to-end ML pipeline
✔ Automated workflow with Prefect
✔ REST API deployment
✔ CI/CD integration
✔ Model monitoring with Evidently
✔ Clean project structure

---

## 🧠 MLOps Workflow

```
Data → Versioning → Training → Tracking → Deployment → Monitoring
```

---

## 💡 Important Notes

* Dataset is tracked using **DVC**
* `mlruns/` is excluded (MLflow artifacts)
* `model.pkl` is not version controlled
* Monitoring report is generated after training

---

## 🎯 Conclusion

This project demonstrates a **production-ready MLOps pipeline**, integrating modern tools and best practices for scalable machine learning systems.

---

## 👩‍💻 Author

**Siddhi Daphal**

---
