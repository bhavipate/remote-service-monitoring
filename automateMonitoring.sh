#!/bin/bash

echo "Updating package lists..."
sudo apt update

echo "Installing Python3 and pip..."
sudo apt install -y python3 python3-pip

echo "Installing Python3 virtual environment..."
sudo apt install -y python3-venv

echo "Setting up Flask application directory..."
mkdir -p flask_app && cd flask_app

echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing Flask and flask_cors..."
pip install Flask flask_cors

echo "Downloading service.txt..."
curl -o service.txt https://raw.githubusercontent.com/A7ryan/Lyrcon_Cloud_DevOps_Internship_Tasks/main/monitorRemoteVMServices/service.txt

echo "Downloading checkServices.py..."
curl -o checkServices.py https://raw.githubusercontent.com/A7ryan/Lyrcon_Cloud_DevOps_Internship_Tasks/main/monitorRemoteVMServices/checkServices.py

echo "Running checkServices.py..."
python3 checkServices.py
