import requests, json

def get_api_zipcode(country, news_outlet):
    url = "https://newsapi.org/v2/" \
              "top-headlines?country={}&apiKey=6db89d56e492480593a9e23072586219".format(country)
    req = requests.get(url)
    req = req.json()
    title = desc = link = ""
    articles = req["articles"]

    for article in articles:
        if article["source"]["name"] == news_outlet:
            title = article["title"]
            desc = article["description"]
            link = article["url"]
    res = [title, desc, link]
    jsonRes = json.dumps(res)

    return jsonRes

    
    
print(get_api_zipcode("us", "CNN"))