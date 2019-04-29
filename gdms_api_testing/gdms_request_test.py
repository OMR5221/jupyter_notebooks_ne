import requests

r = requests.get("https://gdms.windlogics.com/api/site/", verify=False, proxies={"https": "https://webproxyjb.fpl.com:8080"})
print(r.text)
