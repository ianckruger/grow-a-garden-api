import requests
import schedule
import time


# Configurations
Target_SEED = ""
# Discord_Webhook_Url = 
API_URL = "https://gagapi.onrender.com/seeds"


def check_seed_stock():
    print("🔄 Checking Grow a Garden stock...")
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()


        available = [item.get("name") for item in data]
        
        # this will be a discord notification
        print(f"Current stock: {available}")

        if(Target_SEED in available):
            print(f"{Target_SEED} is in stock.")
            # maybe send a notification for this only?

    except Exception as e:
        print(f"Error fetching data: {e}")

check_seed_stock()

schedule.every(5).minutes.do(check_seed_stock)

print("press Ctrl+C to stop running")

while True:
    schedule.run_pending()
    time.sleep(1)