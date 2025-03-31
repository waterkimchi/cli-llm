#!/bin/bash

# check if virtual environment was already set
if [ ! -d ".venv" ]; then
	if command -v virtualenv &>/dev/null; then
		echo "virtualenv found. Using virtualenv to create virtual environment."
		virtualenv venv
	elif command -v python3 -m venv &>/dev/null; then
		echo "venv (built-in) found. Using venv to create virtual environment."
		python3 -m venv venv
	else
		echo "Neither virtualenv nor venv found.  Please install one of them."
		exit 1 # Exit with an error code
	fi
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -e .

echo "Installation complete!"

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
RESET='\033[0m'

clear
echo ""
echo ""
echo "${RED}   ________    ____            __    __    __  ___${RESET}"
echo "${YELLOW}  / ____/ /   /  _/           / /   / /   /  |/  /${RESET}"
echo "${GREEN} / /   / /    / /   ______   / /   / /   / /|_/ /${RESET}"
echo "${BLUE}/ /___/ /____/ /   /_____/  / /___/ /___/ /  / /${RESET}"
echo "${MAGENTA}\\____/_____/___/           /_____/_____/_/  /_/${RESET}"
echo ""

echo "${CYAN}To use clillm, activate the virtual environment:${RESET}"
echo "${YELLOW}source .venv/bin/activate${RESET}"
echo "${GREEN}Then, run your CLI command:${RESET}"
echo "${BLUE}clillm --help${RESET}"

deactivate
