import requests
import json
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# API endpoint URL
apod_url = "https://api.nasa.gov/planetary/apod"

# Parameters
api_key = " "  #use API key/..

# Request headers
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

# Request parameters
params = {
    "api_key": api_key
}

# Send GET request to the API
response = requests.get(apod_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    apod_data = json.loads(response.text)
    
    # Retrieve the APOD details
    title = apod_data['title']
    explanation = apod_data['explanation']
    url = apod_data['url']
    
    # Retrieve the APOD image
    image_response = requests.get(url)
    image = Image.open(BytesIO(image_response.content))
    
    # Display the APOD
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)
    plt.show()
    
    print("\nExplanation: ", explanation)
else:
    print("Error:", response.status_code)

