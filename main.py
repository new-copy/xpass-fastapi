
import os
from fastapi import FastAPI, HTTPException
from services.order import OrderRepo
from services.payment import StripeStub
from bot import checkout_ticket

repo = OrderRepo()
stripe_stub = StripeStub()

app = FastAPI(title="X‑PASS PoC API")

@app.post("/orders")
def create_order(item: str, qty: int, amount_cents: int):
    return repo.create(item, qty, amount_cents)

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = repo.get(order_id)
    if not order: raise HTTPException(404)
    return order

@app.post("/orders/{order_id}/pay/card")
def pay_card(order_id: int):
    order = repo.get(order_id)
    if not order: raise HTTPException(404)
    receipt = stripe_stub.charge(order["amount_cents"])
    repo.mark_paid(order_id, receipt["tx_ref"])
    return {"msg": "paid", **receipt}

@app.post("/orders/{order_id}/pay/site")
def pay_via_site(order_id: int):
    order = repo.get(order_id)
    if not order: raise HTTPException(404)
    receipt = checkout_ticket()
    repo.mark_paid(order_id, receipt["tx_ref"])
    return {"msg": "paid", **receipt}
