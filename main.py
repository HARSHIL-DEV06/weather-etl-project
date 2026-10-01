from extract import fetch_data
from transform import transform_weather_data
from load import weather_data


def run_pipeline():
    print("ETL Pipeline Running......")
    raw_data = fetch_data()
    if not raw_data:
        print("Pipeline Stopped: Extraction Failed.")
        return
    
    cleaned_data = transform_weather_data(raw_data)
    if not cleaned_data:
        print("Pipeline Stopped: Transformation Failed.")
        return
    
    weather_data(cleaned_data)
    
    print("--- Pipeline Finish Successfully!! ---")
    


if __name__ == "__main__":
    run_pipeline()