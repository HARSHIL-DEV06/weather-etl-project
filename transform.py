def transform_weather_data(raw_data):
    current = raw_data.get("current_weather",{})
    
    if not current:
        print("We are unable to get your request")
        return None
    cleaned_data = {
        "temperature" : current.get("temperature"),
        "windspeed" : current.get("windspeed"),
        "timestamp" : current.get("time")
    }
    
    print("data transform Successfully!!")
    return cleaned_data


if __name__ == "__main__":
    test_data = {
        'latitude': 19.0, 
        'longitude': 72.875, 
        'current_weather': {
            'temperature': 29.5, 
            'windspeed': 11.2, 
            'time': '2023-10-27T12:00'
        }
    }
    result = transform_weather_data(test_data)
    print(result)