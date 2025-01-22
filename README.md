# PythonFlaskApi

A lightweight Python Flask API designed to provide a basic web application framework. This repository connects to a MySQL database and demonstrates basic CRUD operations. It is part of a larger project involving Terraform to provision infrastructure for deployment.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [CI/CD Workflow](#cicd-workflow)

## Features
- RESTful API implementation using Flask.
- Connects to a MySQL database (provisioned by Terraform).
- Provides a web UI to:
  - Create tables in the database.
  - Insert records into the created tables.
  - Display the inserted data.
- Integrated unit testing using `pytest`.
- Automatic CI/CD workflows for testing and quality checks.

## Prerequisites
Before running or contributing to this project, ensure you have:
- **Python** 3.9 or newer
- **pip** (Python package manager)
- An active MySQL database (e.g., provisioned by Terraform as part of the parent project).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Skyphoenixx/PythonFlaskApi.git
   cd PythonFlaskApi
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Set the `FLASK_APP` environment variable:
   - On Linux/MacOS:
     ```bash
     export FLASK_APP=application.py
     export DB_HOST=<DB_HOST> # Set the MySQL database host
     export DB_USER=<DB_USER> # Set the MySQL database user
     export DB_PASSWORD=<DB_PASSWORD> # Set the MySQL database password
     export DB_NAME=<DB_NAME> # Set the MySQL database name
     ```
   - On Windows (Command Prompt):
     ```bash
     set FLASK_APP=application.py
     set DB_HOST=<DB_HOST> # Set the MySQL database host
     set DB_USER=<DB_USER> # Set the MySQL database user
     set DB_PASSWORD=<DB_PASSWORD> # Set the MySQL database password
     set DB_NAME=<DB_NAME> # Set the MySQL database name
     ```
   - On Windows (PowerShell):
     ```bash
     $env:FLASK_APP="application.py"
     $env:DB_HOST="<DB_HOST>" # Set the MySQL database host
     $env:DB_USER="<DB_USER>" # Set the MySQL database user
     $env:DB_PASSWORD="<DB_PASSWORD>" # Set the MySQL database password
     $env:DB_NAME="<DB_NAME>" # Set the MySQL database name
     ```

2. Start the Flask application:
   ```bash
   flask run
   ```

3. The API will be available at `http://127.0.0.1:5000` if hosted locally.

4. Available Features:
   - **Create Table:** Use the web UI to create a new table in the MySQL database.
   - **Insert Record:** Add records to the created table.
   - **View Data:** View the inserted records directly in the app.

   Example usage:
   ```bash
   curl http://127.0.0.1:5000/create_table
   curl -X POST http://127.0.0.1:5000/insert_record -d '{"key": "value"}'
   ```

## Testing
Run unit tests using `pytest`:
```bash
pytest
```


## CI/CD Workflow
This repository is integrated with GitHub Actions for automated testing and code quality analysis. The workflow is triggered on:
- **Push events** to the `main` branch
- **Pull requests** targeting the `main` branch

### Workflow Details
1. **Parent CI/CD Integration:**
   - Activates the CI/CD pipeline in the [`TerraformAWSFlask`](https://github.com/Skyphoenixx/TerraformAWSFlask) repository.
   - Ensures the [`SimpleTerraformAWSProj`](https://github.com/Skyphoenixx/SimpleTerraformAWSProj) Terraform pipeline deploys the necessary MySQL database (on AWS RDS) before running this project.

2. **Test Stage:**
   - Installs dependencies.
   - Runs unit tests using `pytest`.

3. **Code Quality Stage:**
   - Integrates with SonarCloud for static code analysis.
   - Scans code and uploads results to SonarCloud.