"""
Example: Fetching Solar Data from NOAA
This demonstrates the data acquisition layer of the architecture.
"""

import requests
import matplotlib.pyplot as plt

def fetch_noaa_example():
    """Fetches and displays recent solar flare data from NOAA."""
    url = "https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Extract the most recent flare from each class
        recent_flares = {}
        for flare in data:
            flare_class = flare.get('class', 'NONE')
            # Keep the most recent one for each class
            if flare_class not in recent_flares:
                recent_flares[flare_class] = flare
        
        print("[EXAMPLE] Most recent flare per class:")
        for cls, flare in recent_flares.items():
            print(f"  {cls}-class: {flare['begin_time']}")
            
        return recent_flares
        
    except Exception as e:
        print(f"[EXAMPLE] Error fetching data: {e}")
        return {}

if __name__ == "__main__":
    fetch_noaa_example()
