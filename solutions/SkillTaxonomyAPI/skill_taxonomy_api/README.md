# Skill Taxonomy API

A small FastAPI application that serves and manages skill taxonomy data stored in JSON files.

## Requirements

- Python 3.11 or newer

## Run locally

From this directory, create and activate a virtual environment, then install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the development server:

```powershell
uvicorn app.main:app --reload
```

Interactive API documentation is available at <http://127.0.0.1:8000/docs>.

## Endpoints

All catalog endpoints are under `/api/v1` and support `GET` collection, `GET` by ID,
`POST`, `PUT` by ID, and `DELETE` by ID:

- `/taxonomies`
- `/categories`
- `/skills`
- `/technologies`
- `/job_roles`

`GET /api/v1/proficiencies` returns the supported proficiency levels. `GET /` is a
small health/info endpoint.

Catalog changes are written back to their corresponding files in `data/`. The JSON
files are seeded with linked example records and can be edited directly while the
server is stopped.