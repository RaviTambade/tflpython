# TFLInsurance API Policy Testing

A small FastAPI project for learning automated tests of policy-management endpoints.
The example supports listing, retrieving, creating, updating, and deleting
insurance policies. Its data is held in memory and resets when the application
is restarted.

## Setup

From this directory, create and activate a virtual environment, then install the
dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the tests

```powershell
python -m pytest -v
```

The tests use FastAPI's in-process `TestClient`; they do not require a running
Uvicorn server. Each test gets a newly created application so its changes to the
in-memory policy list cannot affect other tests.

## Run the API

```powershell
python -m pip install uvicorn
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore the interactive API documentation.
