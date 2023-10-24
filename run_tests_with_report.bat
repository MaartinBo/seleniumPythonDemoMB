@echo off

rem Get the current date and time in ISO 8601 format
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do set "DATE=%%c%%a%%b"
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set "TIME=%%a%%b"
set "DATE_WITH_TIME=%DATE%_%TIME%"

rem Specify the path to the /tests folder using Unix-style path
set "TESTS_PATH=%CD%\tests"

rem Navigate to the /tests folder with double-quotes
cd /d "%TESTS_PATH%"

rem Run pytest with Allure report
pytest -m login --alluredir "%TESTS_PATH%\allure-report"

rem Generate Allure report
allure serve "%TESTS_PATH%\allure-report"

rem Open the Allure report in the default web browser
allure open "%TESTS_PATH%\allure-report"
