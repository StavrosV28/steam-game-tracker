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
response_json = response.json()

data = []

csv_header = ['APP_ID', 'NAME', 'IMG_ICON', 'PLAYTIME', 'LAST_PLAYED']

game_count = response_json['response']['game_count']

for x in response_json['response']['games']:
    parsed_data = [
        x['appid'],
        x['name'],
        x['img_icon_url'],
        x['playtime_forever'],
        x['rtime_last_played'],
        game_count]
    
    data.append(parsed_data)

with open('my_steam.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(csv_header)
    writer.writerows(data)

print('All good')

