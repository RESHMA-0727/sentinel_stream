# Sentinel Stream 🚨
Real-Time Fraud Detection Engine developed over a 4-week sprint using FastAPI, Redis, Celery, Docker, and testing tools.

## Project Overview
Sentinel Stream is a fraud detection system designed to process transaction data and return risk decisions in real time. The project was built step by step across four weeks, moving from planning and API structure to async processing, Docker setup, testing, and final documentation.

## My Contributions
I worked on the tasks assigned to me and completed the planned deliverables for my part of the project.

My contributions included:
- Redis caching setup and support work
- Celery/background-check related implementation support
- Docker setup with Dockerfile and `docker-compose.yml
- JWT dependency setup for secured flow
- Pytest files and issue fixing during testing
- README improvements and GitHub update work
- Docs and wireframe-related support during earlier stages

## Tech Stack
- Python
- FastAPI
- Pydantic
- Redis
- Celery
- Docker
- Pytest
- Locust


## Tech Stack
- Python
- FastAPI
- Pydantic
- Redis
- Celery
- Docker
- Pytest
- Locust

## Week-wise Deliverables

### Week 1 — Foundation and Planning
Main work completed:
- Set up the GitHub repository and project structure
- Defined the initial backend direction
- Prepared architecture and wireframe documents in `docs/
- Planned API contracts and fraud detection workflow

Deliverables:
- SRS and planning artifacts
- Admin/dashboard wireframes
- Initial FastAPI contract discussion
- Base project organization

### Week 2 — Core Backend API
Main work completed:
- Built the FastAPI backend for transaction processing
- Added request validation using Pydantic
- Implemented rule-based fraud scoring logic
- Tested the `/transaction workflow locally
- Performed Locust load testing

Deliverables:
- `POST /transaction
- Risk scoring engine
- API docs through FastAPI Swagger
- Load test result: **26 requests/sec with 0% failure**

Example output:
json
{
  "risk_score": 90,
  "status": "BLOCKED"
}


### Week 3 — Async Processing and Background Checks
Main work completed:
- Added Celery-based background task support
- Connected Redis as broker/cache layer
- Implemented background fraud-check workflow
- Added task status tracking flow

Deliverables:
- `POST /background-check
- `GET /task-status/{task_id}
- Redis-backed asynchronous execution
- Improved separation between request handling and long-running scoring

### Week 4 — Production Readiness
Main work completed:
- Added Dockerfile and `docker-compose.yml
- Brought up FastAPI/Redis/Celery using Docker
- Added JWT package support for protected background-check flow
- Added pytest files and validated test execution
- Cleaned repository documentation and final Git history

Deliverables:
- Docker-based local run setup
- JWT dependencies installed
- Pytest test files added
- Final README update
- Pull request merged

## Final System Built
At the end of the sprint, the project delivers:
- A FastAPI backend for transaction risk evaluation
- Rule-based fraud decision logic
- Async background-check processing with Celery
- Redis integration for cache and broker use
- Dockerized project setup for local execution
- Basic automated test coverage setup
- Documented week-wise development progress in GitHub

## Project Structure
``text
sentinel_stream/
├── app/
├── docs/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── locustfile.py
├── requirements.txt
└── README.md


## API Endpoints

### 1. Transaction Check
`POST /transaction

Purpose:
- Accept a transaction payload
- Run fraud/risk logic
- Return score and decision

### 2. Background Check
`POST /background-check

Purpose:
- Submit transaction data for asynchronous processing
- Return a task id immediately

### 3. Task Status
`GET /task-status/{task_id}

Purpose:
- Track whether the background job is pending, successful, or blocked

## How to Run

### Local run
bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000


### Docker run
bash
docker-compose up


### API docs
Open:
`text
http://localhost:8000/docs


## Testing
Pytest files were added in Week 4 to support basic validation of the backend flow.

Run:
`bash
pytest tests/


## Performance
Week 2 load-testing result:
- **26 requests/second**
- **0% failure rate**

This confirmed that the core transaction endpoint was functioning reliably during local testing.

## GitHub Progress
The repository history reflects incremental development across all four weeks:
- Week 1: planning and structure
- Week 2: backend API and risk engine
- Week 3: Celery and Redis async flow
- Week 4: Docker, JWT setup, tests, README cleanup

 ## Final Output
By the end of the sprint, the project includes:
- Fraud detection API flow
- Risk scoring logic
- Redis integration
- Celery background processing
- Docker setup for local run
- Pytest validation setup
- Updated GitHub history and README

## Today’s Fixes
Final work completed today included:
- Fixing test folder/file structure
- Fixing pytest import issues
- Adjusting Redis-related test behavior
- Installing JWT dependencies
- Updating README for final submission
- Merging Week 4 work into the repository

## Current Status
- Week 1 to Week 4 work recorded
- Redis, Celery, Docker, and testing work completed
- Final README updated
- PR merged
- Repository ready for mentor review

  ## Demo
Swagger UI available at http://127.0.0.1:8000/docs


## Conclusion
Sentinel Stream demonstrates a complete backend sprint progression from planning to production-ready setup. The final result is a working fraud detection backend with API endpoints, async task processing, Redis integration, Docker support, and test scaffolding.
