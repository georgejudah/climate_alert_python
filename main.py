import requests
from twilio.rest import Client
#Key is not valid
api_key = "7f1d131edaed4226310f200f286e35f5"
account_sid = "ACb293168ec0a681c1ad0e59f4bca025a5"
auth_token = '7b79140020ab32734b611b56c66cbdf3'
OWN_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
parames = {
    "lat": 11.121,
    "lon": 78.65,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

data = requests.get(OWN_endpoint, params=parames)
data.raise_for_status()
weather_data = data.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body="It's going to rain.Remember carry an umbrella with you today 🌂🌧",
        from_='+12084174958',
        to='+919361158520'
    )
    print(message.status)
