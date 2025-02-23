#!/bin/bash

set -e

if [ ! -d ".venv" ]; then
	echo ".venv directory not found. Creating..."
	echo "Creating virtual environment..."
	python3 -m venv .venv --clear
fi
# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip within the virtual environment (good practice)
echo "Upgrading pip..."
pip install --upgrade pip

# Install project dependencies (from requirements.txt or setup.py)
echo "Installing dependencies..."

# install from setup.py
pip install -e .

echo "Running post-installation configuration (if any)..."
# Add any commands here, e.g., setting up config files, etc.
# For example, create a default config file:
# if [ ! -f ~/.clillm_config ]; then
#   cp clillm/default_config.ini ~/.clillm_config
# fi
clear
echo "Installation complete!"
echo "      _ _       _ _           "
echo "  ___| (_)     | | |_ __ ___  "
echo " / __| | |_____| | | '_ \` _ \ "
echo "| (__| | |_____| | | | | | | |"
echo " \___|_|_|     |_|_|_| |_| |_|"

echo ""
echo "To use clillm, activate the virtual environment:"
echo "source .venv/bin/activate"
echo "Then, run your CLI command:"
echo "clillm --help"

source .venv/bin/activate
