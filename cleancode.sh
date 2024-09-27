#!/bin/bash

set -e

BASE_DIR="."

: "${VIRTUAL_ENV?Python virtual env must be active}"

echo "Executing isort..." && isort $BASE_DIR
echo "Executing black..." && black $BASE_DIR
echo "Executing flake8..." && flake8 $BASE_DIR --exclude ".venv/*","tests/*"