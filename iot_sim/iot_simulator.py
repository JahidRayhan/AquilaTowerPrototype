import requests, random, time

URL = "http://127.0.0.1:8000/receive_data"

while True:
    data = {
        "product_id": random.choice(["P101","P102","P103"]),
        "stock_level": random.randint(20, 300),
        "temperature": round(random.uniform(22.0, 35.0), 1),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        r = requests.post(URL, json=data)
        print("Sent:", data, "| Response:", r.status_code)
    except Exception as e:
        print("Error:", e)
    time.sleep(5)
