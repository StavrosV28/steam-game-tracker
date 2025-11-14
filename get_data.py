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
        
        
        