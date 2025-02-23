#!/bin/bash

# check if virtual environment was already set
if [ ! -d ".venv" ]; then
	echo "Virtual Environment not found, creating one..."
	python3 -m venv .venv --clear
fi

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -e .

echo "Installation complete!"

echo ""
echo "To use clillm, activate the virtual environment:"
echo "source .venv/bin/activate"
echo "Then, run your CLI command:"
echo "clillm --help"
