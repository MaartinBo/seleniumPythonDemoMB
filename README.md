# selenium_python_mb

## Technologies Used

- Python
- Selenium
- Pytest
- Allure
- Pre-commit
- Black
- Pylint
- GitHub Actions
## Test Website

- [mb-qa.eu](https://mb-qa.eu/)

## Getting Started

Create a Virtual Environment (Optional)
It's recommended to create a virtual environment for this project to manage dependencies cleanly:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

To set up the project, you can manually install all the required packages listed in the `requirements.txt` file or run the following command:

```bash
pip install -r requirements.txt
```

After installing all packages, set up the hooks for this repository by running:

```bash
pre-commit install
```

## Test the Pre-commit Setup

To test if pre-commit is properly set up, modify some Python files and attempt to commit them.
The pre-commit hooks will automatically format your code with Black and check it with Pylint.

```bash
echo "print('Hello world')" > test.py
git add test.py
git commit -m "feat: add test script"
```

If any issues are detected, pre-commit will block the commit and prompt you to fix the formatting or linting errors.

## Optional Configuration for Black and Pylint

Configuring Black
To customize the behavior of Black, such as adjusting the maximum line length, create a pyproject.toml file with the following content:

## Running the Tests

To run these tests without allure report, I recommend using the startup script `simple_run.sh` or `simple_run.bat`, depending on your system and terminal. You can execute it with the following commands:

Bash: `bash simple_run.sh`

Windows: `.\simple_run.bat`

To run these test with allure report, use one of the following files:

Bash: `bash run_tests_with_report.sh`

Windows: `.\run_tests_with_report.bat`

In the end the new report will open in your browser.

You can customize which tests you run by editing the line with the tag in the file. By default, the tests are tagged as `pytest -m login`.

### List of Available Tags

Here are the available tags for running specific test categories:

- `login`: Tests related to the login process.
- `checkout`: Tests related to the checkout process.
- `register`: Tests related to the registration process.
- `billing`: Tests related to billing in the account section.
- `smoke`: Default smoke tests
