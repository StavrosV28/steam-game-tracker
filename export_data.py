import requests
import csv
import creds

api_key = creds.steam_api
profile_id = creds.profile_id

url = (
    f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    f"?key={api_key}&steamid={profile_id}&include_appinfo=1&format=json"
)


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=[])
my_json = response.json()
our_data = []


game_count = my_json['response']['game_count']

for x in my_json['response']['games']:
    listing = [
        x['appid'],
        x['name'],
        x['img_icon_url'],
        x['playtime_forever'],
        x['rtime_last_played'],
        game_count]
    
    our_data.append(listing)


print(our_data)

