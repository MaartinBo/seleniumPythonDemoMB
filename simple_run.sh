#!/bin/bash

# Specify the path to the /tests folder using Unix-style path
TESTS_PATH="$(pwd)/tests"

# Change the current directory to the /tests folder
cd "$TESTS_PATH"

# Run 'pytest' to execute all tests. You can also use the -m flag to specify which test cases you want to run.
pytest -m checkout
# list of all tags
# 'login' 'checkout' `register` `billing`

