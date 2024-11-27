import requests
import os

def extract_text_from_image(image_path, output_txt_path):
    api_key = "K87549615388957"  
    url = "https://api.ocr.space/parse/image"
    
    # Ensure the provided image file exists
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    try:
        # Open the image file in binary mode
        with open(image_path, 'rb') as f:
            # Send a POST request to the OCR.space API
            response = requests.post(
                url,
                files={'filename': f},
                data={'apikey': api_key}
            )
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        result = response.json()
        extracted_text = result.get("ParsedResults", [{}])[0].get("ParsedText", "")
        
        if not extracted_text:
            print("No text detected in the image.")
            return
        
        # Create the output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_txt_path), exist_ok=True)
        
        # Save the extracted text to the specified file
        with open(output_txt_path, 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        
        print(f"Text successfully saved to {output_txt_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error with OCR API request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
image_path = "easy-extract/images/brsr-pg.png"  # Replace with your image file path
output_txt_path = "easy-extract/outputs/extracted_text.txt"  # Replace with your desired output file path
extract_text_from_image(image_path, output_txt_path)
