#Ransom Galaxy PICS

import requests
import json
from IPython.display import Image, display

# NASA API endpoint URL
apod_url = "https://api.nasa.gov/planetary/apod"

# Your NASA API key
api_key = " " #use API Key/..

# Parameters for the API request
params = {
    "api_key": api_key,
    "count": 5,  # Number of images to retrieve (adjust as needed)
    "thumbs": False  # Set to False for high-resolution images
}

try:
    # Make the API request
    response = requests.get(apod_url, params=params)
    response.raise_for_status()  # Raise an exception if the request is unsuccessful

    # Parse the response as JSON
    data = response.json()

    # Process the retrieved images
    for item in data:
        image_title = item["title"]
        image_url = item["url"]
        display(Image(url=image_url, width=600))
        print(f"Title: {image_title}")
        print("\n")

except requests.exceptions.HTTPError as err:
    print(f"Error fetching images: {err}")
