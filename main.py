from time import sleep
import requests

while True:
    sleep(900)
    r = requests.get("https://ytmusic-uf.herokuapp.com/youtube-data/despacito")
    print(r.status_code)
    