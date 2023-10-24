#!/bin/bash

# Get the current date and time in ISO 8601 format
DATE_WITH_TIME=$(date "+%Y%m%d_%H%M%S")

# Specify the path to the /tests folder using Unix-style path
TESTS_PATH="$(pwd)/tests"

# Navigate to the /tests folder with double-quotes
cd "$TESTS_PATH"

# Run pytest with Allure report
pytest -m login --alluredir "$TESTS_PATH/allure-report"

# Generate Allure report
allure serve "$TESTS_PATH/allure-report"

# Open the Allure report in the default web browser
allure open "$TESTS_PATH/allure-report"
