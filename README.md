
# X‑PASS PoC

FastAPI + Selenium proof‑of‑concept that:
1. Creates an order
2. Automates login @ store.x-pass.io/xpass01/home
3. Clicks purchase flow
4. Marks order as paid

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export XPASS_PASS=xpass
uvicorn main:app --reload
```

## Endpoints
- POST /orders  `{ "item":"Concert","qty":2,"amount_cents":18000 }`
- POST /orders/{id}/pay/site  (runs Selenium bot)

**Warning**: bot assumes certain CSS selectors (.buy-ticket, #checkout).
Adjust as needed.
