
# Arknights Damage Calculator – DevOps Project

## Project Description
The application is a **FastAPI-based damage calculator** inspired by the game *Arknights*.The project consists of a Python-based web application exposing a REST API, deployed using Docker and Kubernetes. The application persists data in a PostgreSQL database and is supported by a comprehensive CI pipeline and a locally deployable Kubernetes environment using Minikube. 

The primary goal of this project is not the application logic itself, but the **DevOps pipeline and infrastructure** surrounding it, including CI/CD, containerization, Kubernetes orchestration, and database versioning.

---

## Technology Stack and Rationale

### Backend Application
- **Python (FastAPI)** – Provides a lightweight, asynchronous web framework suitable for modern APIs.
- **Uvicorn** – ASGI server used to run the application in production-like environments.

### Containerization
- **Docker** – Packages the application into a portable, reproducible container image.
- **Docker Hub** – Acts as a container registry for storing and distributing application images.

### Container Orchestration
- **Kubernetes** – Manages container deployment, scaling, service discovery, and persistence.
- **Minikube** – Enables local Kubernetes development and testing.

### Database Layer
- **PostgreSQL** – Production-grade relational database used for persistent data storage.
- **Persistent Volumes & Claims** – Ensure database state is preserved across pod restarts.
- **SQLAlchemy** – ORM for database interaction
- **Flyway** – Database schema versioning and migrations

### CI/CD and Automation
- **GitHub Actions** – Implements continuous integration and container image delivery.
- **Docker Build & Push** – Automatically builds and publishes versioned container images.

### Code Quality and Security
- **Black & Flake8** – Enforce consistent code formatting and static analysis.
- **Bandit** – Performs static security analysis on Python code.
- **Trivy** – Scans Docker images for known vulnerabilities.
- **SonarQube** – Provides maintainability, reliability, and security metrics.

---

## Continuous Integration Pipeline

The CI pipeline is triggered on pushes and pull requests to the `main` and `develop` branches. It consists of the following stages:

1. Source code checkout
2. Dependency installation
3. Automated testing with Pytest
4. Code formatting and linting
5. Static security analysis
6. Container image build
7. Container vulnerability scanning
8. Image publication to Docker Hub

This pipeline ensures that only tested, scanned, and quality-checked artifacts are published.

---

## Continuous Deployment (Conceptual)

While deployment is currently manual, the pipeline is designed to be extended with CD. A typical extension would include:

- Applying Kubernetes manifests after successful image publication
- Using environment-specific namespaces
- Introducing approval gates for production deployments

---

## CI/CD Architecture Diagram

```
┌──────────────┐
│   Developer  │
└──────┬───────┘
       │ Git Push / PR
       ▼
┌────────────────────┐
│   GitHub Actions   │
│  (CI Pipeline)     │
├────────────────────┤
│ • Tests            │
│ • Linting          │
│ • Security Scans   │
│ • Docker Build     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Docker Hub       │
│ Container Registry │
└─────────┬──────────┘
          │
          ▼
┌────────────────────────┐
│ Kubernetes (Minikube)  │
│ • App Deployment       │
│ • PostgreSQL           │
│ • Persistent Storage   │
└────────────────────────┘
```

---

## Running the Project Locally with Minikube

### Prerequisites
- Docker
- kubectl
- Minikube

### Step 1: Start Minikube
```bash
minikube start
```

### Step 2: Apply Kubernetes Manifests
```bash
kubectl apply -f k8s/postgres/
kubectl apply -f k8s/flyway-migrations-configmap.yaml
kubectl apply -f k8s/flyway-job.yaml
kubectl apply -f k8s/app/
```

This deploys:
- PostgreSQL (Deployment + Service + PVC)
- Application Deployment (multiple replicas)
- NodePort Service for external access

### Step 3: Verify Deployment
```bash
kubectl get pods
kubectl get svc
```

### Step 4: Access the Application
```bash
minikube ip
```
Then open in a browser:
```
http://<MINIKUBE_IP>:<NODEPORT>
```

```bash
minikube service arknights-service --url
```

Alternatively, port forwarding may be used:
```bash
kubectl port-forward deployment/arknights-app 8000:8000
```

---

## Database Schema

The database schema is **fully managed by Flyway migrations**.

### Operators Table

| Column | Type | Description |
|------|------|------------|
| id | INTEGER (PK) | Operator ID |
| name | VARCHAR | Operator name |
| attack | INTEGER | Attack value |
| damage_type | VARCHAR | Physical / Arts / True |

### Bosses Table

| Column | Type | Description |
|------|------|------------|
| id | INTEGER (PK) | Boss ID |
| name | VARCHAR | Boss name |
| defense | INTEGER | Defense value |
| resistance | INTEGER | Arts resistance |

All schema changes are tracked in the `flyway_schema_history` table.

---

## Educational Value

This project demonstrates:
- End-to-end DevOps workflows
- Infrastructure-as-Code principles
- Secure and automated software delivery
- Kubernetes-based application architecture
- Database persistence in containerized systems
- Database migrations

---

## Future Improvements
- Full CD automation using GitHub Actions
- Cloud deployment (AWS)
- More functionality reflecting the arknights world better
