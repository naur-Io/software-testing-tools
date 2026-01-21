# Software Testing Tools

This repository contains examples and experiments related to software testing in Java, focused on learning, practice, and project organization.

It is mainly used for study purposes, exercises, and small tools created during classes or self-learning about testing and test automation.

## Tech Stack for Gradle Projects
- Java
- Gradle
- Testing frameworks (e.g. JUnit)

### Gradle Testing Tool (Java)
Clone the repository:
```powershell
git clone https://github.com/naur-Io/software-testing-tools.git
cd software-testing-tools
```
Make sure a compatible JDK is installed:
- Recommended: Oracle JDK 25

Build the project and download dependencies:
```powershell
./gradlew build # Build the project
./gradlew test # Run tests
./gradlew clean run # Clean and run the project
```

Dependencies are automatically managed by Gradle and are not stored in the repository.

## Tech Stack for Python Projects
- Python
- pytest
- Testing frameworks (e.g. pytest)

Make sure a compatible Python version is installed:
- Recommended: Python 3.8 or higher
Create and activate a virtual environment:
```powershell
python -m venv .venv # Create virtual environment
pip install pytest # Install pytest
```
```powershell
python -m venv .venv # Create virtual environment
pip install pytest # Install pytest
pytest # to run all the tests
pytest -v # Test with detailed output
pytest -v --cov # Test with coverage report
pytest -cov -v --cov-report=html # Test with HTML report
```

# Getting Started (Selenium with Java)
Navigate to the Selenium Java project directory and Build and run tests:

```powershell
cd software-testing-tools/selenium-java

./gradlew build # Build the project
./gradlew test  # Run tests
```

## Selenium Configuration Notes
- WebDriver executables are not included in the repository
- Browser compatibility: Ensure your WebDriver version matches your browser version
- Headless testing is supported for both Chrome and Firefox
- Cross-browser testing configurations are available in the examples
### Notes
- Only source code is versioned
- Dependencies are managed via virtual environments
- Python installations, virtual environments, and caches are ignored via .gitignore

