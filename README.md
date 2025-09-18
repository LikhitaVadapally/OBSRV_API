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

### Run with Docker Compose
#1.start Postgres and API
docker-compose up --build

#2. Access API docs
http://127.0.0.1:8000/docs

# 3. Run tests
pytest tests/


### Run with Kubernetes
#1. Build the app image
docker build -t obsrv_api-api:latest .

#2. Deploy Postgres in Kubernetes
- Apply the provided manifests that create a Postgres Deployment and a Service named db.
- Because the Service is named db in the same namespace as the app, the application can use the hostname db:5432 directly

#3. Deploy the FastAPI app
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/postgres.yaml

#4. Verify resources
kubectl get pods
kubectl get svc

#5. Access the API (with port-forward)
kubectl port-forward svc/fastapi-service 8080:80
http://localhost:8080/docs


#6. Running tests
pytest tests/

