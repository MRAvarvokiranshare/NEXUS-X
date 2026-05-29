#!/bin/bash

clear

echo "Installing NEXUS Requirements..."

pkg update -y
pkg upgrade -y

pkg install python -y

pip install -r requirements.txt

echo ""
echo "NEXUS Installed Successfully!"
echo ""
echo "Run:"
echo "python main.py"
