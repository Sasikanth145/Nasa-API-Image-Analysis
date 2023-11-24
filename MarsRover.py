#MARS Rover
import requests
import json
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# API endpoint URL
api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

# Parameters
api_key = "a4fpHga5Mzddp3l6xtwwqT2P5dPcXeCpEwaCSAGn"  # Replace with your NASA API key
rover_name = "curiosity"
sol = 1000  # Martian sol (day) to retrieve photos from

# Request headers
headers = {
    "User-Agent": "",
    "Content-Type": "application/json"
}

# Request parameters
params = {
    "api_key": api_key,
    "sol": sol
}

# Send GET request to the API
response = requests.get(api_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)
    
    # Retrieve the photos
    photos = data['photos']
    
    if len(photos) > 0:
        # Display the first photo
        first_photo = photos[0]
        img_url = first_photo['img_src']
        image_response = requests.get(img_url)
        image = Image.open(BytesIO(image_response.content))
        
        # Display the photo
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        
        print("Camera:", first_photo['camera']['full_name'])
        print("Earth Date:", first_photo['earth_date'])
    else:
        print("No photos available for the given sol.")
else:
    print("Error:", response.status_code)

