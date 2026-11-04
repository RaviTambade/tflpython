# Python + Playwright learning path

These lessons adapt the populated notes in the parent folder into a Python-first
curriculum. They keep the original lesson sequence and topics while replacing
TypeScript/Node.js examples with Python, pytest, and Playwright for Python.
The original notes remain unchanged.

## Lessons

1. [Python foundations for test automation](1.md)
2. [Python for SDETs and Playwright](2.md)
3. [Build a browser automation project](3.md)
4. [API testing with Playwright](4.md)
5. [pytest fixtures and test lifecycle](5.md)
6. [Database verification with MySQL](6.md)
7. [Advanced framework patterns](7.md)
8. [Authentication, roles, isolation, and parallel runs](8.md)

## Suggested learning order

Complete lessons 1–2 before building the browser suite in lesson 3. Lessons
4–6 add API and persistence coverage. Lessons 7–8 build on those foundations
with reusable authentication, isolated data, and parallel execution.

## Example application assumptions

The examples use placeholder routes such as `/api/auth/login` and
`/Account/Login`. Replace them with routes, accessible labels, and response
fields from the application under test. Run tests only against a dedicated
local or test environment.

## Quick setup

From a new project directory, create and activate a virtual environment, then
install the browser-testing dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest pytest-playwright
python -m playwright install chromium
```

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install pytest pytest-playwright
python -m playwright install chromium
```

Run the suite with `pytest`. The examples favor Playwright's synchronous Python
API for readability; the async API is available when the surrounding
application or test infrastructure is already asynchronous.
