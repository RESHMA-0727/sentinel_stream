# 🚀 Sentinel Stream — Real-Time Fraud Detection System

## 📌 Overview
Sentinel Stream is a real-time transaction processing system that detects fraudulent activities using a hybrid approach combining rule-based logic and machine learning.

The system is designed to be **scalable, explainable, and production-ready**, with features like Redis caching, idempotency, and behavior tracking.

---

## ⚡ Key Features

### 🔍 Fraud Detection Engine
- Rule-based risk scoring
- ML-based anomaly detection
- Hybrid risk calculation

### 🧠 Explainable AI (NEW 🔥)
- Provides **reasons** for fraud decisions
- Improves transparency and interpretability

### 📊 Risk Classification
- LOW / MEDIUM / HIGH risk levels
- Easy human-readable output

### 🚨 Suspicious User Detection
- Flags users as **SUSPICIOUS** based on risky behavior
- Demonstrates behavior-based fraud detection

### 🌍 Context-Aware Detection
- Location-based risk (unusual countries)
- Time-based detection (midnight transactions)
- Frequency-based detection (rapid requests)

### ⚡ Performance Optimization
- Redis caching for fast responses
- Idempotency to prevent duplicate transactions

### 🗄️ Database Integration
- SQLite with SQLAlchemy ORM
- Persistent transaction storage

---

## 🧠 System Architecture
User Request
↓
FastAPI API
↓
Redis (Idempotency Check ⚡)
↓
Rule Engine + ML Model
↓
Context Checks (Location + Time + Frequency)
↓
Database (SQLite)
↓
Redis Cache
↓
Response (with explanation)
---## 🛠️ Tech Stack| Layer        | Technology ||-------------|------------|| Backend     | FastAPI || Database    | SQLite + SQLAlchemy || Caching     | Redis || Language    | Python || ML Logic    | Simulated ML Model |---## 🚀 How to Run### 1️⃣ Install dependencies```bashpip install -r requirements.txt
2️⃣ Start Redis
docker start pedantic_curie
3️⃣ Run API
uvicorn app.main:app --reload

📬 API Usage
Endpoint
POST /transactions/

🔹 Sample Request
{  "idempotency_key": "demo-1",  "user_id": 1,  "amount": 12000,  "location": "Russia"}

🔹 Sample Response (🔥 FINAL OUTPUT)
{  "status": "blocked",  "risk_score": 1,  "risk_level": "HIGH",  "reason": [    "High transaction amount",    "Unusual location"  ],  "user_flag": "SUSPICIOUS"}

🧠 How It Works


Checks Redis for duplicate requests (idempotency)


Applies rule-based + ML scoring


Evaluates contextual signals:


Location


Time


Transaction frequency




Generates explanation (reasons)


Assigns risk level


Flags suspicious users


Stores result in DB and Redis



🎯 Key Highlights


✅ Real-time fraud detection system


✅ Explainable AI with decision reasons


✅ Behavior-based user risk tracking


✅ Redis-based caching and idempotency


✅ Clean modular architecture


✅ Production-like backend design



📈 Future Enhancements


Integrate real ML model


Add Kafka for streaming


Deploy with Docker/Kubernetes


Add monitoring dashboards



👩‍💻 Author
Reshma Sri

⭐ Final Note
This project demonstrates real-world backend engineering concepts including:


Fraud detection systems


Distributed caching


Idempotent APIs


Explainable AI


Scalable service design
