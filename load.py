import os
import psycopg2 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def weather_data(cleaned_data):
    try:
        conn = psycopg2.connect(
            dbname="weather_db",
            user="postgres",
            password=os.getenv("DB_PASSWORD"),
            host = "localhost",
            port = "5432"
        )
    # craete a cursor object to exceute SQL command
        cur = conn.cursor()
    
        insert_query = """
           INSERT INTO weather_data (city,temperature,windspeed,recorded_at)
           VALUES (%s,%s,%s,%s);
         """
        record_to_insert = (
         "Mumbai",
         cleaned_data["temperature"], 
         cleaned_data["windspeed"], 
         cleaned_data["timestamp"]
        )
    
        cur.execute(insert_query,record_to_insert)
        conn.commit()
    
        print("Data Successfully Loaded into the Database..")
      # Close the connection
        cur.close()
        conn.close()
         
    except Exception as e:
        print(f"database Error: {e}")
        
if __name__ == "__main__":
    # Test with dummy data
    sample_data = {'temperature': 29.5, 'windspeed': 11.2, 'timestamp': '2023-10-27T12:00'}
    weather_data(sample_data)
        