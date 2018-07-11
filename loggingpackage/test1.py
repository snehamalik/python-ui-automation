import requests

url = 'https://api.healthkart.com/api/catalog/results/?st=1&catPrefix=hfd-drnk-acv&pageNo=1&plt=1'
r = requests.get(url)
if (r.status_code == 200):
    x = r.json()
    print(x['results']['filters'])
    if len(x['results']['filters']) >0:
        print("Filters are coming")

    else:
        print("Filter are not coming")
        n=requests.get("https://api131.healthkartqa.com/api/edge/cluster/memory/cache/reload/10")
        if (n.status_code == 200):
            print("Filters has been refreshed")
        else:
            print("Error while memcache refreshing")


