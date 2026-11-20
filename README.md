# CareerNest — Job & Internship Tracker
A Django website with registration, login/logout, application CRUD, search/filter, dashboard statistics, and interview dates.

## Run on Windows PowerShell
1. Extract the ZIP and open the `CareerNest` folder in terminal.
2. Create a virtual environment:
   `python -m venv venv`
3. Activate it (if PowerShell blocks scripts, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate):
   `.env\Scripts\Activate.ps1`
4. Install:
   `python -m pip install -r requirements.txt`
5. Create database:
   `python manage.py migrate`
6. Start:
   `python manage.py runserver`
7. Open http://127.0.0.1:8000/
8. Create account, then add and manage applications.

## Workflow
Home → Sign up / Login → Dashboard → Add opportunity → Applications list → Edit or delete → Logout.

This is a development starter; before public deployment, change SECRET_KEY, set DEBUG=False, configure allowed hosts and HTTPS, and review security settings.
