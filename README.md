# Warframe-Twitch-Fetcher
Grabs warframe streamers and opens them up in multitwitch for loot drops





idea from @jancodes





changed by @eucalyptwos

changed

1.you need to get bearer token cause twitch api had been changed


paste
curl -X POST "https://id.twitch.tv/oauth2/token?client_id=<your client_id>&client_secret=<your client_secret>&grant_type=client_credentials"
on cmd to get token

you can get client id and client secret from  https://dev.twitch.tv/console/apps

2.you can use this for all games.
***but you have to enter full name.
***default value is "warframe"

3.reduced number of multitwitch stream from 20 to 5

4.fit code for changed api

5.reduced the amount of streamers the twitch API pulls

require python version higher than 3.7

paste
pip install wheel
and
pip install twitch-python
on cmd to get libraries















