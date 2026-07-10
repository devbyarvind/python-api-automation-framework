# 🚀 API Automation Framework

<p align="center">
  <b>A lightweight and maintainable REST API automation framework built using Python, Pytest, and Requests</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Test%20Framework-pytest-green?logo=pytest" alt="Pytest">
  <img src="https://img.shields.io/badge/API%20Library-Requests-orange" alt="Requests">
  <img src="https://img.shields.io/badge/Reports-HTML-red" alt="HTML Reports">
  <img src="https://img.shields.io/badge/Logging-Enabled-purple" alt="Logging">
</p>

---

# 📌 Project Overview

This project is a **Python-based API Test Automation Framework** designed to automate REST API testing using **Pytest** and the **Requests** library.

The framework supports CRUD operations:

* 🟢 GET
* 🟡 POST
* 🔵 PUT
* 🔴 DELETE

The main objective of this framework is to provide a simple, scalable, and maintainable structure for API automation testing.

---

# 🎯 Framework Goals

This framework follows industry-standard automation practices:

✅ Modular framework design
✅ Reusable API client implementation
✅ Separate test data management
✅ Centralized logging mechanism
✅ Automated HTML reporting
✅ Clean and readable test cases

---

# 🏗️ Project Structure

```text
API_AUTOMATION_FRAMEWORK/
│
├── 📄 conftest.py
│   └── Pytest hooks and shared fixtures
│
├── ⚙️ pytest.ini
│   └── Pytest configuration and report settings
│
├── 📦 requirements.txt
│   └── Python project dependencies
│
├── 📂 testdata/
│   └── activity.json
│       └── Test payload data
│
├── 📂 tests/
│   └── test_getuser.py
│       └── API automation test cases
│
├── 📂 utils/
│   │
│   ├── api_client.py
│   │   └── Reusable API request handler
│   │
│   └── logger.py
│       └── Logging configuration
│
├── 📂 reports/
│   └── HTML test execution reports
│
├── 📂 logs/
│   └── Execution logs
│
└── 📘 README.md
    └── Project documentation
```

---

# 🛠️ Technology Stack

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| 🐍 Python 3      | Programming language      |
| 🧪 Pytest        | Test execution framework  |
| 🌐 Requests      | HTTP API communication    |
| 📊 pytest-html   | HTML test reports         |
| 🔐 python-dotenv | Environment configuration |

---

# ⚙️ Prerequisites

Before running this framework, make sure you have:

* Python 3 installed
* pip package manager available
* Internet connection for API execution

Check Python installation:

```bash
python --version
```

Check pip installation:

```bash
pip --version
```

---

# 🚀 Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <repository-url>

cd API_AUTOMATION_FRAMEWORK
```

---

## 2️⃣ Create Virtual Environment

### Windows PowerShell

```powershell
python -m venv arvind_venv

.\arvind_venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
python -m venv arvind_venv

arvind_venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv arvind_venv

source arvind_venv/bin/activate
```

---

## 3️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Tests

## Run Complete Test Suite

Execute all automation tests:

```bash
pytest
```

---

## Run Specific Test File

Example:

```bash
pytest tests/test_getuser.py
```

---

## Run Tests With HTML Report

```bash
pytest --html=reports/report.html
```

After execution:

```
reports/
 └── report.html
```

Open the HTML file in a browser to view the execution results.

---

# 🔄 Framework Execution Flow

```text
          📝 Test Case
               |
               ↓
        📂 Load Test Data
               |
               ↓
        🔌 API Client Layer
               |
               ↓
        🌐 REST API Request
               |
               ↓
        📥 API Response
               |
               ↓
        ✅ Assertions
               |
               ↓
        📝 Logging
               |
               ↓
        📊 HTML Report
```

---

# 🔌 API Client Design

All API calls are handled through:

```
utils/api_client.py
```

The API client provides reusable methods for:

```text
GET
POST
PUT
DELETE
```

Benefits:

✅ Avoids duplicate HTTP code
✅ Improves code maintenance
✅ Keeps test cases clean
✅ Provides centralized API handling

---

# 📂 Test Data Management

Test payloads are stored separately:

```
testdata/
 └── activity.json
```

Example:

```json
{
    "title": "Sample Activity",
    "completed": false
}
```

Benefits:

✅ Easy data updates
✅ Supports data-driven testing
✅ Separates data from automation logic

---

# 📝 Logging

The framework maintains execution logs using:

```
utils/logger.py
```

Captured information:

* API endpoint
* Request method
* Request payload
* Response status code
* Response body
* Execution details

Logs are stored in:

```
logs/
```

Example:

```
logs/
 └── execution.log
```

---

# 📊 Reporting

The framework generates HTML reports using:

```
pytest-html
```

Reports include:

✅ Test execution summary
✅ Passed/failed test cases
✅ Execution duration
✅ Failure details

Location:

```
reports/
```

---

# 🧪 Test Coverage

Current automation coverage:

| API Operation             | Status    |
| ------------------------- | --------- |
| GET Request Validation    | ✅ Covered |
| POST Request Validation   | ✅ Covered |
| PUT Request Validation    | ✅ Covered |
| DELETE Request Validation | ✅ Covered |

---

# 📈 Future Enhancements

The framework can be extended with:

## 🌍 Environment Configuration

Add support for:

* QA environment
* Stage environment
* Production environment

---

## 📊 Data Driven Testing

Support:

* CSV files
* Excel files
* Database test data

---

## 🔍 Schema Validation

Add:

* JSON schema validation
* Response contract testing

---

## 🔄 CI/CD Integration

Integrate with:

* GitHub Actions
* Jenkins
* Azure DevOps

---

## 🐳 Docker Support

Containerize the framework for:

* Consistent execution
* Easy deployment
* Pipeline integration

---

# 🤝 Contribution Guidelines

Contributions are welcome.

Steps:

1. Create a new branch
2. Add your improvements
3. Execute test cases
4. Create a pull request

---

# 🐞 Troubleshooting

## Issue: pytest command not found

Solution:

```bash
pip install pytest
```

---

## Issue: Module not found

Solution:

```bash
pip install -r requirements.txt
```

---

## Issue: Virtual environment not activated

Activate environment again:

Windows:

```powershell
.\arvind_venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source arvind_venv/bin/activate
```

---

# 👨‍💻 Author

**API Automation Framework**

Created for:

* API automation learning
* Testing practice
* Framework development experience

---

# ⭐ Happy API Testing! 🚀

<p align="center">
  Built with ❤️ using Python + Pytest
</p>
