# Marks Grader DevOps

A production-style FastAPI backend for managing student grades, built with a complete DevOps workflow in mind.

This project includes JWT authentication, role-based access control, PostgreSQL integration, automated API testing with Pytest, containerized deployment using Docker Compose, CI/CD integration with Jenkins, and monitoring using Prometheus + Grafana.

## Features

* FastAPI REST API
* JWT Authentication & Authorization
* Teacher-only protected routes
* PostgreSQL database integration
* Pydantic request validation
* Automated API testing with Pytest
* Dockerized application stack
* Jenkins CI/CD pipeline support
* Prometheus metrics collection
* Grafana dashboards & monitoring

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker & Docker Compose
* Jenkins
* Pytest
* Prometheus
* Grafana

## DevOps Focus

This project was built to simulate a real-world backend deployment workflow, including:

* container orchestration
* automated testing
* CI/CD pipelines
* infrastructure monitoring
* service isolation
* environment-based configuration

## API Flow

1. Authenticate via `/auth/login`
2. Receive JWT token
3. Access protected grade endpoints
4. Store and retrieve student marks securely

## Future Improvements

* Kubernetes deployment
* GitHub Actions pipeline
* Alembic migrations
* Nginx reverse proxy
* Redis caching
* Terraform infrastructure provisioning

Built as a hands-on DevOps and backend engineering portfolio project.
