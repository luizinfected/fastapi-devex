# FastAPI DevEx

I created this demo project to show how CI/CD, Docker, testing, and observability can work together. It has a simple FastAPI service with a GitHub Actions pipeline and Prometheus/Grafana monitoring.

## Stack:
- FastAPI (Simple endpoint)
- Pytest (Automatic tests)
- Docker
- GitHub Actions (CI pipeline)
- Prometheus + Grafana (Observability)

## How to run:
```bash
git clone https://github.com/luizinfected/fastapi-devex.git
cd fastapi-devex
docker-compose up --build
```

## To stop and remove containers, networks, and volumes:
docker-compose down

## Access:
- API: [http://localhost:8000/im_ok](http://localhost:8000/im_ok)
- Prometheus metrics: [http://localhost:8000/metrics](http://localhost:8000/metrics)
- Prometheus UI: [http://localhost:9090](http://localhost:9090)
- Grafana UI: [http://localhost:3000](http://localhost:3000)

## GitHub Actions
This project performs::
- Dependency installation
- Pytest execution
- Docker image build

## Observability
The application exposes Prometheus-compatible metrics such as:
- Request size in bytes
- Request count per route

---