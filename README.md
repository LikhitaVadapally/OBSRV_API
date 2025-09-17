# OBSRV_API

A FastAPI-based REST API with PostgreSQL backend, containerized using Docker, and deployable to Kubernetes.

# Project Structure
OBSRV_API/
├── app/ # FastAPI application (CRUD, models, schemas, DB setup)

├── db_init/ # Database initialization SQL scripts

├── k8s/ # Kubernetes deployment and service manifests

├── tests/ # Unit tests for the API

├── docker-compose.yml # Docker Compose setup for local development

├── Dockerfile # Docker image build file

└── requirements.txt # Python dependencies


## Features
- FastAPI for REST API development  
- PostgreSQL database integration  
- Dockerized for portability  
- Kubernetes manifests for deployment  
- Unit tests with Pytest  

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/LikhitaVadapally/OBSRV_API.git
cd OBSRV_API

### 2. Run with Docker Compose
docker-compose up --build

### 3. Access API docs
http://127.0.0.1:8000/docs

### 4. Run tests
pytest tests/

