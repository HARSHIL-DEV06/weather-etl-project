import os
import requests
from dotenv import load_dotenv

def fetch_data():
    load_dotenv()
    url = os.getenv("API_KEY")
    print("Connecting with weather API...")
    
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print("Data fetched!!")
            raw_data = res.json()
            return raw_data
        else:
            print(f"Failed to fetch the data: {res.status_code}")
            return None
        
    except Exception as e:
        print(f"Error occur. {e}")
        return None

if __name__ == "__main__":
    data = fetch_data()
    if data:
        print(data)