## 📁 **Project Structure**
# SentinelStream 🚨 Real-Time Fraud Detection

**Zaalima Development Q4 Python Elite** – Week 1 COMPLETE ✅

Production-grade engine scoring 1000s transactions/sec with ML + rules. Neo-bank ready!

## 📁 Project Structure
app/
├── sentinel.py → Fraud scoring engine (asyncio)
├── transactions.py → Transaction generator
docs/
├── analytics_wireframe_v1.txt
├── transactions_wireframe.txt
├── rules_wireframe.txt
docker-compose.yml → Redis backend



## 🚀Week 1 Deliverables
- ✅ SRS  defined
- ✅ PostgreSQL schema (Star schema, 3NF)
- ✅ 3 Admin wireframes (Transactions/Rules/Analytics)
- ✅ GitHub repo with CICD ready
- ✅ FastAPI contract stable



## 🎯 Core Features
POST /transaction → <200ms fraud score (0-1.0)
Redis user cache + idempotency keys
Rule engine: amount>5000 + !home = RISK
ML Isolation Forest integration ready

## 🏃‍♂️ Quick Demo

 Terminal 1
python app/transactions.py

 Terminal 2  
python app/sentinel.py

Expected: Transaction 12345 RISK_SCORE=0.87


🛠️ Tech Stack
FastAPI (ASGI) | PostgreSQL (ACID) | Redis (cache)
SQLAlchemy Async | Pydantic (validation)
Docker | GitHub Actions CICD


📈 Performance Targets
100 req/sec local (Locust ready)
<200ms E2E latency
90%+ test coverage (Week 4)

# 🚀 COMPLETE SentinelStream - Week1 + Week2
# Zaalima Q4 Python Elite ✅✅

**Production FastAPI Fraud Engine** - Week1 Planning + Week2 LIVE API!

**Live Demo**: http://localhost:8000/docs  
**GitHub**: https://github.com/RESHMA-0727/week2-fastapi-backend

---

## 📁 WEEK1 Structure (Planning Phase)

week1-sentinelstream/
├── app/
│   ├── sentinel.py (asyncio scoring)
│   ├── transactions.py (generator)
├── docs/
│   ├── analytics_wireframe_v1.txt
│   ├── transactions_wireframe.txt
│   ├── rules_wireframe.txt
├── docker-compose.yml (Redis)


**Week1 Deliverables** ✅
- SRS + PostgreSQL schema (Star/3NF)
- 3 Admin wireframes
- GitHub CICD ready
- FastAPI contract stable


'''
week2-Structure fastapi-backend/
├── app/
│   ├── main.py (FastAPI /transaction)
│   ├── models.py (Pydantic)
│   ├── risk_engine.py (₹7500=90 BLOCKED)
├── requirements.txt


  Week2 Deliverables✅
- FastAPI POST /transaction (<200ms)
- Risk rules engine
- Locust 26 req/sec (0% fail)
- Curl demo + API docs

## 🎯 CORE API (Week2 LIVE)
**Live**: http://localhost:8000/docs 

**POST /transaction**
json
Input: {"amount":7500,"user_id":"vishn","merchant":"Flipkart"}
**Expected Output**: {"risk_score":90,"status":"BLOCKED"}


**Quick Demo**:
# Terminal 1
uvicorn app.main:app --reload --port 8000

# Terminal 2  
curl -s -X POST http://localhost:8000/transaction \
-H "Content-Type: application/json" \
-d '{"amount":7500,"user_id":"vishn","merchant":"Flipkart"}' | jq
**Expected**: {"risk_score":90,"status":"BLOCKED"}

curl -s -X POST http://localhost:8000/transaction \
-H "Content-Type: application/json" \
-d '{"amount":3000,"user_id":"vishn","merchant":"Amazon"}' | jq
**Expected**: {"risk_score":35,"status":"APPROVED"}


## 📈 PERFORMANCE (Locust)
| Metric | Value |
|--------|-------|
| **Peak** | 26 req/sec |
| **Fail** | 0% |
| **Max** | 200ms |

## 🛠️ Tech Stack
**FastAPI** | **Pydantic** | **Uvicorn** | **Locust** | **Python 3.12**

## 📋 ROADMAP
✅ **Week1**: Architecture + SRS  
✅ **Week2**: FastAPI Core API  
⏳ **Week3**: ML Isolation Forest + Redis  
⏳ **Week4**: Docker + JWT + 90% tests



