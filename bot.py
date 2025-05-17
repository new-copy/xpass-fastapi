
import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL      = "https://store.x-pass.io/xpass01/home"
PASSWORD = os.getenv("XPASS_PASS", "xpass")

def pay_with_stripe(amount_cents: int):
    # Stub for Stripe PaymentIntent
    print(f"[Stripe] Charging ${amount_cents/100:.2f} … succeeded!")
    return {"status": "succeeded", "tx_ref": "ch_test_" + str(int(time.time()))}

def checkout_ticket():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    # 1) password input
    pwd_box = driver.find_element(By.NAME, "password")
    pwd_box.send_keys(PASSWORD)
    pwd_box.submit()

    # 2) wait and click buy button (assumes class name)
    time.sleep(2)
    ticket_btn = driver.find_element(By.CSS_SELECTOR, ".buy-ticket")
    ticket_btn.click()

    qty_box = driver.find_element(By.NAME, "quantity")
    qty_box.clear(); qty_box.send_keys("2")
    driver.find_element(By.ID, "checkout").click()

    time.sleep(2)
    receipt = pay_with_stripe(18000)
    driver.quit()
    return receipt
