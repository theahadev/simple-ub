@echo off
python3 -m pip install --upgrade pip
python3 -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt