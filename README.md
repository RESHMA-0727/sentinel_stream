# 🚀 Sentinel Stream — Real-Time Fraud Detection System

## 📌 Overview

Sentinel Stream is a real-time transaction processing system designed to detect fraudulent activities using a hybrid approach that combines rule-based logic and machine learning techniques.

The system ensures **high performance, scalability, and reliability** by integrating Redis caching and idempotent request handling.

---

## ⚡ Key Features

### 🔍 Fraud Detection Engine

* Rule-based risk evaluation (threshold-based logic)
* ML-based anomaly scoring (simulated model)
* Hybrid risk scoring system for better accuracy

### ⚡ Performance Optimization

* Redis caching for ultra-fast responses
* Reduced database load through caching layer

### 🔁 Idempotency Handling

* Prevents duplicate transaction processing
* Ensures consistent results for repeated requests

### 🗄️ Database Integration

* SQLite with SQLAlchemy ORM
* Persistent transaction storage

### 🌐 API Layer

* Built with FastAPI
* Async support for high performance
* Interactive Swagger UI for testing

---

## 🧠 System Architecture

```
User Request
     ↓
FastAPI API Layer
     ↓
Redis (Cache Check ⚡)
     ↓
Rule Engine + ML Model
     ↓
Database (SQLite)
     ↓
Redis (Store Response)
     ↓
Final Response
```

---

## 🛠️ Tech Stack

| Layer    | Technology          |
| -------- | ------------------- |
| Backend  | FastAPI             |
| Database | SQLite + SQLAlchemy |
| Caching  | Redis               |
| Language | Python              |
| ML Logic | Simulated ML Model  |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RESHMA-0727/sentinel_stream.git
cd sentinel_stream
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start Redis (Docker)

```bash
docker run -d -p 6379:6379 redis
```

### 4️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

---

## 📬 API Usage

### 🔹 Endpoint

```
POST /transactions/
```

### 🔹 Sample Request

```json
{
  "idempotency_key": "txn-123",
  "user_id": 1,
  "amount": 8000
}
```

---

### 🔹 Sample Response

```json
{
  "status": "declined",
  "risk_score": 0.72,
  "transaction_id": 1,
  "processed_at": "2026-04-07"
}
```

---

## 🧠 How It Works

1. Checks Redis for existing request (idempotency)
2. If found → returns cached response ⚡
3. If not:

   * Applies rule-based risk scoring
   * Applies ML-based anomaly detection
   * Combines both scores
4. Stores result in DB
5. Caches response in Redis

---

## 🎯 Key Highlights

* ✅ Real-time fraud detection system
* ✅ Hybrid (Rule + ML) scoring model
* ✅ Redis-based caching for performance
* ✅ Idempotent API design (production-grade concept)
* ✅ Clean modular architecture

---

## 📈 Future Enhancements

* Replace simulated ML with real trained model
* Add Kafka for event streaming
* Deploy using Docker + Kubernetes
* Add monitoring (Prometheus/Grafana)

---

## 👩‍💻 Author

**RESHMASRI**

---

## ⭐ Final Note

This project demonstrates real-world backend engineering concepts including:

* Distributed caching
* Idempotent APIs
* Fraud detection systems
* Scalable service design
