
#!/usr/bin/env bash
set -e
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export XPASS_PASS=${XPASS_PASS:-xpass}
uvicorn main:app --host 0.0.0.0 --port 8000
