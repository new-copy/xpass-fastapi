
import datetime, itertools

class OrderRepo:
    def __init__(self):
        self._counter = itertools.count(1)
        self._orders = {}

    def create(self, item, qty, amount_cents):
        oid = next(self._counter)
        self._orders[oid] = {
            "id": oid,
            "item": item,
            "qty": qty,
            "amount_cents": amount_cents,
            "status": "CREATED",
            "created_at": datetime.datetime.utcnow().isoformat()+"Z"
        }
        return self._orders[oid]

    def get(self, oid):
        return self._orders.get(oid)

    def mark_paid(self, oid, tx_ref):
        if oid in self._orders:
            self._orders[oid]["status"] = "PAID"
            self._orders[oid]["tx_ref"] = tx_ref
            self._orders[oid]["paid_at"] = datetime.datetime.utcnow().isoformat()+"Z"
        return self._orders.get(oid)
