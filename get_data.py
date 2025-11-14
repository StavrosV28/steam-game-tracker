import requests
import json
import creds



def get_game_library(api_key, user_id):
        url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={creds.steam_api}&steamid={creds.profile_id}&format=json"
        response = requests.get(url)
        
        data = response.json()
        # Parse JSON response to get game details
        if "response" in data and "games" in data["response"]:
            games = data["response"]["games"]
            return [game["appid"] for game in games]
        else:
            print("Failed to retrieve game library...")
            return[]
        

def get_game_details(api_key, app_ids):
    # looping through each id in the lsit
    for id in app_ids:
        url = f"https://store.steampowered.com/api/appdetails?appids={id}"
        response = requests.get(url)
        data = response.json()
        
        # Sends the GET request and converts response to JSON
        if data and str(id) in data and data[str(id)]["Success"]:
            name = data[str(id)]["data"]["name"]
            review_score = data[str(id)]["data"]["metacritic"]["score"] if "metacritic" in data[str(id)]["data"] else "N/A"
            # Pulling game name, id, and metacritic score
            print(f"Game: {name} (APP ID: {id}), Review Score: {review_score}")
        else:
            print("Failed to retrieve game details for App ID: {id}")
            print(data) # For troubleshooting
        