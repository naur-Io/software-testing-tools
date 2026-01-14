# Software Testing Tools

This repository contains examples and experiments related to software testing in Java, focused on learning, practice, and project organization.

It is mainly used for study purposes, exercises, and small tools created during classes or self-learning about testing and test automation.

## Tech Stack for Gradle Projects
- Java
- Gradle
- Testing frameworks (e.g. JUnit)

### Getting Started
Clone the repository:
```powershell
git clone https://github.com/naur-Io/software-testing-tools.git
cd software-testing-tools
```
Make sure a compatible JDK is installed:
- Recommended: Oracle JDK 25

Build the project and download dependencies:
```powershell
./gradlew build 
./gradlew test
```

Dependencies are automatically managed by Gradle and are not stored in the repository.

### Notes
- Only source code is versioned
- Dependencies are handled by Gradle
- JDKs, build files, and caches are ignored via .gitignore


## Tech Stack for Python Projects
- Python
- pytest
- Testing frameworks (e.g. pytest)

### Getting Started
Clone the repository:
```powershel
git clone https://github.com/naur-Io/software-testing-tools.git
cd software-testing-tools/pytest test framework/pytest
```

Make sure a compatible Python version is installed:
- Recommended: Python 3.8 or higher
Create and activate a virtual environment:
```powershell
create virtual envrioment
python -m venv .venv

activate the virtual enviroment
.venv\Scripts\activate

install pytest
~ pip3 install pytest
```

Run the tests using pytest:
```powershell
pytest to run all the tests
pytest -v to run a detailed output of the tests
pytest -q to run a concise output of the tests
python -m pytest -s -v to see print statements during test execution
```

### Notes
- Only source code is versioned
- Dependencies are managed via virtual environments
- Python installations, virtual environments, and caches are ignored via .gitignore

