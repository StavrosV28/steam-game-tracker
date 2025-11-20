import requests
import csv
import datetime
import creds

api_key = creds.steam_api
profile_id = creds.profile_id

# Provided URL to fetch specific game data from my profile
url = (
    f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    f"?key={api_key}&steamid={profile_id}&include_appinfo=1&include_played_free_games=1&format=json"
)


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Make GET request to SteamAPI
response = requests.request("GET", url, headers=headers, data=[])
response_json = response.json()

data = []

# Provide organization for CSV file
csv_header = ['app_id', 'name', 'img_icon', 'playtime(hrs)', 'last_played']

# Just to showcase total games owned
game_count = response_json['response']['game_count']

# Go through response and extract the specified keys
for x in response_json['response']['games']:
    last_played = x.get('rtime_last_played', 0)
    # converts UNIX timestamp from SteamAPI to readable calendar date
    calendar_date = datetime.datetime.fromtimestamp(last_played).strftime('%Y-%m-%d')
    
    parsed_data = [
        x['appid'],
        x['name'],
        x['img_icon_url'],
        round(x['playtime_forever'] / 60, 1),
        calendar_date]
    
    data.append(parsed_data)

# Write extracted data into the CSV file
with open('my_steam.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(csv_header)
    writer.writerows(data)

# Everythings working
print('All good')

