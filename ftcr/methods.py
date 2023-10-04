import pymongo
import requests


def check_mongo():
    try:
        client = pymongo.MongoClient("mongodb://thedash:dash1234@vm-360-mongo2:27017/iptv_analytics?replicaSet=rs0")
        # Close the connection
        client.close()

        # If you reached this point, the connection was successful
        return True
    except pymongo.errors.ConnectionFailure as e:
        # Handle connection failure (e.g., log the error)
        print(f"MongoDB Connection Error: {e}")
        return False


def check_api():

    # Define the API URL and parameters
    api_url = "http://217.165.211.39:5045/rcDetails"
    params = {
        "startdate": "2023-10-01",
        "enddate": "2023-10-02",
        "usecase_id": 10,
        "user_id": 3
    }

    try:
        # Make the GET request
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and process the API response here
            data = response.json()  # Assuming the response is in JSON format
            print("API Response:")
            print(data)
        else:
            print(f"API request failed with status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"API request error: {e}")