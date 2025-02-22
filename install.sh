#!/bin/bash

set -e

echo "Creating virtual environment..."
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip within the virtual environment (good practice)
echo "Upgrading pip..."
pip install --upgrade pip

# Install project dependencies (from requirements.txt or setup.py)
echo "Installing dependencies..."

# install from setup.py
pip install -e .

echo "Copying .env file..."
if [ -f ".env" ]; then
	cp .env .venv/lib/python3.9/site-packages/clillm/.env # Adjust path if needed
	# cp .env .venv/clillm/.env # if clillm is at the root of the venv
else
	echo "Warning: please create a .env file following the .env.example for the node to run."
fi

echo "Running post-installation configuration (if any)..."
# Add any commands here, e.g., setting up config files, etc.
# For example, create a default config file:
# if [ ! -f ~/.clillm_config ]; then
#   cp clillm/default_config.ini ~/.clillm_config
# fi

echo "Installation complete!"

echo ""
echo "To use clillm, activate the virtual environment:"
echo "source .venv/bin/activate"
echo "Then, run your CLI command:"
echo "clillm --help"
