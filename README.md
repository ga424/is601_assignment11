# Module 11 - Calculation Model, Validation, and CI/CD

This module implements a polymorphic SQLAlchemy `Calculation` model, Pydantic validation schemas, and tests that verify both operation logic and persistence.

## What is implemented

- SQLAlchemy model with fields `id`, `type`, `inputs`, and optional `result`
- Computed compatibility properties `a` and `b` from `inputs`
- Pydantic schemas:
  - `CalculationCreate`
  - `CalculationRead`
- Validation rules:
  - Only valid operation types
  - At least two inputs
  - No divide-by-zero denominator
- Factory + polymorphism:
  - `Calculation.create()` returns `Addition`, `Subtraction`, `Multiplication`, or `Division`
- API endpoint:
  - `POST /calculate` validates, computes, persists, returns `CalculationRead`
- Health endpoint:
  - `GET /health`

## Pattern evidence checklist

- Factory Pattern: `app/models.py` (`Calculation.create`)
- Polymorphic Inheritance: `app/models.py` (`__mapper_args__` and subclasses)
- DTO/Schema Pattern: `app/schema.py` (`CalculationCreate`, `CalculationRead`)
- Validation Boundary Pattern: `app/schema.py` model validators
- CI/CD Continuity Pattern: `.github/workflows/ci.yml` + `.github/workflows/docker-publish.yml`

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run application

```bash
uvicorn app.main:app --reload
```

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## Example request

```bash
curl -X POST http://127.0.0.1:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{"type":"addition","inputs":[3,4]}'
```

## Run tests locally

```bash
pytest -q
```

For PostgreSQL-backed test runs:

```bash
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/module11_test"
pytest -q
```

## CI/CD

- CI workflow: `.github/workflows/ci.yml`
  - Runs pytest
  - Uses PostgreSQL service container
- Docker publish workflow: `.github/workflows/docker-publish.yml`
  - Builds and pushes Docker image to Docker Hub on tags (`v*`) or manual dispatch

Required repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

## Docker

Build:

```bash
docker build -t <dockerhub-username>/module11:latest .
```

Run:

```bash
docker run --rm -p 8000:8000 <dockerhub-username>/module11:latest
```

## Submission evidence checklist

- GitHub Actions screenshot showing successful CI run
- Docker Hub screenshot showing pushed image/tag
- Reflection notes addressing challenges and decisions
- Docker Hub repository link: `https://hub.docker.com/r/<dockerhub-username>/module11`
