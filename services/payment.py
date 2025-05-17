
class StripeStub:
    def charge(self, amount_cents: int):
        print(f"[Stripe] Charging ${amount_cents/100:.2f} … succeeded!")
        return {"status":"succeeded","tx_ref":"ch_stub_"+str(amount_cents)}
