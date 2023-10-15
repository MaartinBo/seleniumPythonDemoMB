@echo off

rem Specify the path to the /tests folder using Unix-style path
set "TESTS_PATH=%CD%\tests"

rem Change the current directory to the /tests folder
cd /d "%TESTS_PATH%"

rem Run 'pytest' to execute all tests. You can also use the -m flag to specify which test cases you want to run.
pytest -m checkout

rem List of available tags:
rem 'login' 'checkout' 'register' 'billing'


