import requests
from functools import lru_cache

app_name = "hackaton2024_2"

@lru_cache(maxsize=100)
def nominatim_search(query):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": query,
        "format": "json",
        "limit": 1,
        "addressdetails": 1,
    }
    
    headers = {
        "User-Agent": f"{app_name}/1.0 (doruchan@gmail.com)"  # Replace with your app name
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Status code: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response content: {response.text}")
        
        result = response.json()
        print(f"Parsed JSON: {result}")
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

def search(query):
    
    # Perform the search
    results = nominatim_search(query)

    if results is not None:
        if results:
            place = results[0]
            print(f"Name: {place['display_name']}")
            print(f"Latitude: {place['lat']}")
            print(f"Longitude: {place['lon']}")
            return place
        else:
            print("Search returned an empty list. The place might not be found.")
    else:
        print("No results found.")


if __name__ == "__main__":
    search_query = input("Enter a place to search: ")
    search(search_query)
