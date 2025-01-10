import requests
import json

def emotion_detector(text_to_analyze):
    # Define the API endpoint and headers
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Define the input JSON structure
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    try:
        # Send the POST request
        response = requests.post(URL, json=input_json, headers=headers)

        # Log the response details for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        # Parse the response
        response_data = json.loads(response.text)

        if response.status_code == 200:
            # Extract the required data (adapt to the actual structure)
            emotions = response_data.get('document', {}).get('emotion_predictions', {})
            print(f"Extracted Emotions: {emotions}")

            # Return the emotion data
            return emotions

        elif response.status_code == 400:
            # Handle 400 errors with debugging info
            return {"error": f"Bad Request: {response.text}"}

        else:
            # Handle unexpected errors
            return {"error": f"Unexpected response code: {response.status_code}, Response: {response.text}"}
    
    except Exception as e:
        # Catch and log any exceptions
        return {"error": str(e)}
