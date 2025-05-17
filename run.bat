
@echo off
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
set XPASS_PASS=%XPASS_PASS:xpass%
uvicorn main:app --host 0.0.0.0 --port 8000
