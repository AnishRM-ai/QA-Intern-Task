# QA Automation: Signup Flow Testing with Playwright (Python)

## Overview
This project contains automated tests for the signup flow. Tests are written in python using Playwright following POM pattern.

## Prerequisites
Before running the tests, ensure you have following installed on your systems:
- Python
- Node.js
- pip

## Installation
1. **Clone the repository**
command "git clone https://github.com/AnishRM-ai/QA-Intern-Task.git" </br>
cd QA-Intern_Task
2. **Create virtual environment**
command "python -m venv venv"
3. **Activate virtual environment**
- Windows
command "venv/Scripts/activate"
- Mac/Linux
command "source venv/bin/activate"
4. **Install python dependencies:**
command "pip install -r requirements.txt"
5. **Install Playwright browsers**
command "playwright install"

## Project Setup/ Environment
- **Language**: Python 3.13.1
- **Framework**: Playwright
- **Test Runner**: pytest
- **Browsers Supported**: Chromium, Firefox
- **Environment Variables**:
Create a .env file in the project root to add API and test credentials.

## Running Tests
1. Run all tests:
pytest
2. Run a specific test file:
pytest tests/test_signup.py
3. Run tests with HTML report:
pytest --html=report.html

## Test Data
- The project uses test dummy accounts created for automation using mailosaur.

| Email | Password |
|-------|----------|
| abcya100-settlers@pcqiozhk.mailosaur.net | Password1! |




