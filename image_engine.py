from PIL import Image
import requests
import io
from dotenv import load_dotenv
import os

load_dotenv()

# Define the ImageGenerator class for Hugging Face API
class ImageGenerator:
    def __init__(self) -> None:
        self.api_url = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
        self.headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE')}"}
    
    def generate_image(self, prompt):
        payload = {
            "inputs": prompt,
            # "negative_prompt": "ugly, distorted, low quality"
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        
        # Debugging: Print response status and content type
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content Type: {response.headers.get('Content-Type')}")

        # Check for valid response
        if response.status_code == 200 and response.headers.get('Content-Type').startswith('image'):
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))
            return image
        else:
            # Print the error message if not a valid image
            print("Error: Invalid response received from API")
            print(response.text)  # Print the text content of the response for debugging
            raise Exception("Failed to generate image from API")