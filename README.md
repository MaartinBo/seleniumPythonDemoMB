# selenium_python_mb

## Technologies Used
- Python
- Selenium
- Pytest
- Allure

## Test Website
- [mb-qa.eu](https://mb-qa.eu/)

## Getting Started
To set up the project, you can manually install all the required packages listed in the `requirements.txt` file or run the following command:
```bash
pip install -r requirements.txt
```
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
